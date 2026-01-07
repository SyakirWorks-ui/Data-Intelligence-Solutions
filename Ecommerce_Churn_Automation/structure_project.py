import os

def create_project_structure():
    # Nama folder utama project
    project_name = "Ecommerce_Churn_Automation"
    
    # Struktur folder yang dibutuhkan
    folders = [
        f"{project_name}/data/raw",          # Tempat naruh file CSV asli dari Kaggle
        f"{project_name}/data/processed",    # Tempat simpan hasil cleaning (otomatis)
        f"{project_name}/notebooks",         # Untuk eksperimen (file .ipynb)
        f"{project_name}/src",               # Script utama Python (.py) untuk otomasi
        f"{project_name}/reports/logs",      # Catatan otomatis (validation logs)
        f"{project_name}/reports/figures",   # Grafik hasil analisis
        f"{project_name}/models",            # Tempat simpan model AI (.pkl atau .joblib)
    ]
# File kosong sebagai placeholder
    files = {
        f"{project_name}/src/automation_pipeline.py": "# Script utama untuk Cleaning & Prediction",
        f"{project_name}/src/utils.py": "# Fungsi pembantu (helper functions)",
        f"{project_name}/requirements.txt": "pandas\nnumpy\nscikit-learn\nmatplotlib\nseaborn",
        f"{project_name}/README.md": "# Ecommerce Customer Churn Automation Project"
    }

    # Membuat folder
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Membuat file
    for file_path, content in files.items():
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(content)
            print(f"Created file: {file_path}")

    print("\n✅ Struktur Project Berhasil Dibuat!")

if __name__ == "__main__":
    create_project_structure()