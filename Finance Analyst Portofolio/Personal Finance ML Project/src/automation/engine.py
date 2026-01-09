import pandas as pd
import numpy as np
import os
import joblib
from datetime import datetime

class RiskAutomationEngine:
    def __init__(self, model_path, data_path, output_dir):
        """
        Inisialisasi mesin otomasi risiko.
        """
        self.model_path = model_path
        self.data_path = data_path
        self.output_dir = output_dir
        self.model = None
        self.df = None

    def load_resources(self):
        """Memuat model AI dan data terbaru."""
        print(f"[{datetime.now()}] 🔄 Memuat sumber daya...")
        try:
            if os.path.exists(self.model_path):
                self.model = joblib.load(self.model_path)
                print("✅ Model AI berhasil dimuat.")
            else:
                print("⚠️ Warning: Model .pkl tidak ditemukan. Menggunakan logika rule-based saja.")
            
            if os.path.exists(self.data_path):
                self.df = pd.read_csv(self.data_path)
                self.df.columns = self.df.columns.str.strip()
                print(f"✅ Data nasabah berhasil dimuat: {len(self.df)} baris.")
            else:
                raise FileNotFoundError(f"Data tidak ditemukan di {self.data_path}")
        except Exception as e:
            print(f"❌ Error saat memuat data: {e}")

    def calculate_risk_score(self, row):
        """Logika perhitungan skor risiko (Skala 0-100)."""
        try:
            # Kontribusi Credit Score (50%)
            c_score = (row['credit_score'] / 850) * 50
            # Kontribusi DTI (50% - Semakin kecil DTI semakin besar poin)
            dti_score = (1 - min(row['debt_to_income_ratio'], 1)) * 50
            return round(c_score + dti_score, 2)
        except:
            return 0

    def get_decision(self, row):
        """Logika pengambilan keputusan otomatis."""
        score = row['risk_score']
        if score >= 85:
            return "✅ AUTO-APPROVE (Elite)", "Penawaran Platinum Card"
        elif score >= 65:
            return "✅ AUTO-APPROVE (Standard)", "Penawaran Reguler"
        elif score >= 40:
            return "⚠️ MANUAL REVIEW", "Kirim ke Tim Analis"
        else:
            return "❌ AUTO-REJECT", "Kirim Konseling Keuangan"

    def run_pipeline(self):
        """Menjalankan seluruh alur otomasi dari awal sampai akhir."""
        if self.df is None:
            self.load_resources()

        print(f"[{datetime.now()}] ⚙️ Memproses otomasi risiko...")
        
        # 1. Hitung Skor Risiko
        self.df['risk_score'] = self.df.apply(self.calculate_risk_score, axis=1)
        
        # 2. Tentukan Kategori Risiko
        self.df['risk_category'] = pd.cut(
            self.df['risk_score'], 
            bins=[0, 40, 65, 85, 100], 
            labels=['High Risk', 'Medium', 'Low Risk', 'Elite']
        )
        
        # 3. Keputusan & Tindakan Otomatis
        decisions = self.df.apply(self.get_decision, axis=1)
        self.df['system_decision'], self.df['recommended_action'] = zip(*decisions)

        # 4. Filter Alert Kritis (Red Flags)
        alerts = self.df[self.df['debt_to_income_ratio'] > 0.6].copy()
        
        # 5. Simpan Hasil
        os.makedirs(self.output_dir, exist_ok=True)
        self.df.to_csv(f"{self.output_dir}/automated_decisions_final.csv", index=False)
        alerts.to_csv(f"{self.output_dir}/critical_alerts_log.csv", index=False)
        
        print(f"[{datetime.now()}] ✨ Otomasi Selesai! Laporan tersimpan di {self.output_dir}")

if __name__ == "__main__":
    # Inisialisasi Path secara absolut dan bersih
    # Kita ambil path file ini, lalu naik 3 tingkat ke folder utama proyek
    current_file_path = os.path.abspath(__file__)
    automation_dir = os.path.dirname(current_file_path) # src/automation
    src_dir = os.path.dirname(automation_dir)           # src
    BASE_DIR = os.path.dirname(src_dir)                 # Root Project
    
    # Definisikan path dengan sangat hati-hati
    # Pastikan nama file sesuai dengan yang ada di folder data/processed/
    MODEL_PATH = os.path.join(BASE_DIR, "models", "random_forest_risk_model.pkl")
    DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "personal_finance_final_ml.csv")
    OUTPUT_DIR = os.path.join(BASE_DIR, "reports", "automation_outputs")
    
    # Jalankan engine
    engine = RiskAutomationEngine(
        model_path=MODEL_PATH,
        data_path=DATA_PATH,
        output_dir=OUTPUT_DIR
    )
    
    engine.run_pipeline()