import pandas as pd
import numpy as np
import joblib
import os
import sys

class ChurnPipeline:
    def __init__(self):
        # OTOMATIS: Deteksi base directory proyek berdasarkan lokasi script ini
        # Ini akan menunjuk ke folder 'Ecommerce_Churn_Automation'
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Definisi Path Absolut (Bebas error lokasi terminal)
        self.input_path = os.path.join(self.base_dir, 'data', 'raw', 'data_ecommerce_customer_churn.csv')
        self.model_path = os.path.join(self.base_dir, 'models', 'churn_rf_model.pkl')
        self.output_dir = os.path.join(self.base_dir, 'data', 'processed')
        self.output_path = os.path.join(self.output_dir, 'final_predictions.csv')

    def load_data(self):
        if not os.path.exists(self.input_path):
            print(f"❌ ERROR: File data tidak ditemukan di: {self.input_path}")
            sys.exit(1)
        return pd.read_csv(self.input_path, sep=';')

    def clean_data(self, df):
        cols_to_fix = ['Tenure', 'WarehouseToHome', 'DaySinceLastOrder']
        for col in cols_to_fix:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
                df[col] = df[col].fillna(df[col].median())
        
        if 'PreferedOrderCat' in df.columns:
            df['PreferedOrderCat'] = df['PreferedOrderCat'].str.strip().replace('Mobile Phone', 'Phone')
        return df

    def preprocess_and_predict(self, df):
        if not os.path.exists(self.model_path):
            print(f"❌ ERROR: Model (.pkl) tidak ditemukan di: {self.model_path}")
            sys.exit(1)
            
        model = joblib.load(self.model_path)
        
        # Mengambil fitur yang digunakan saat training (numerik + encoded)
        # Menghapus kolom target jika ada
        X = df.drop(columns=['Churn', 'Churn_Prediction', 'Churn_Probability'], errors='ignore')
        
        # Sederhanakan kategori untuk prediksi cepat
        cat_cols = X.select_dtypes(include=['object']).columns
        for col in cat_cols:
            X[col] = pd.factorize(X[col])[0] # Cara cepat encoding untuk pipeline
            
        df['Churn_Prediction'] = model.predict(X)
        df['Churn_Probability'] = model.predict_proba(X)[:, 1]
        return df

    def run(self):
        print("\n" + "="*40)
        print("🚀 STARTING AUTOMATED CHURN PIPELINE")
        print("="*40)
        
        # 1. Load
        data = self.load_data()
        print(f"✅ Data Loaded: {data.shape[0]} rows")
        
        # 2. Clean
        cleaned_data = self.clean_data(data)
        print("✅ Data Cleaned and Imputed")
        
        # 3. Predict
        final_df = self.preprocess_and_predict(cleaned_data)
        print("✅ Prediction Successful")
        
        # 4. Save
        os.makedirs(self.output_dir, exist_ok=True)
        final_df.to_csv(self.output_path, index=False, sep=';')
        print("="*40)
        print(f"🎉 SUCCESS! Result saved to:\n{self.output_path}")
        print("="*40 + "\n")

if __name__ == "__main__":
    pipeline = ChurnPipeline()
    pipeline.run()