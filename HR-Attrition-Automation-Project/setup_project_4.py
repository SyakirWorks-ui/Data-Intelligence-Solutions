import os

def create_advanced_structure():
    # Nama folder utama proyek
    project_name = "HR-Attrition-Automation-Project"
    
    # Daftar struktur folder dan subfolder yang lebih detail
    structure = [
        os.path.join(project_name, 'data', 'raw'),        # Tempat dataset asli (Kaggle)
        os.path.join(project_name, 'data', 'processed'),  # Tempat dataset hasil cleaning Python
        os.path.join(project_name, 'notebooks'),          # Tempat file .ipynb
        os.path.join(project_name, 'dashboard'),          # Tempat file Power BI (.pbix)
        os.path.join(project_name, 'docs', 'images'),     # Tempat screenshot dashboard untuk GitHub
        os.path.join(project_name, 'docs', 'reports')     # Tempat laporan PDF/Word
    ]
    
    # Proses pembuatan
    for folder in structure:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"✅ Folder dibuat: {folder}")
        else:
            print(f"⚠️ Folder sudah ada: {folder}")

    # Membuat file README.md awal
    readme_path = os.path.join(project_name, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as f:
            f.write(f"# {project_name}\n\nProject deskripsi akan ditulis di sini.")
        print(f"✅ File README dibuat.")

if __name__ == "__main__":
    create_advanced_structure()
    print("\n🚀 Struktur Profesional Berhasil Disiapkan!")