import pdfplumber
import os
import json

pdf_folder = r"c:\Users\muril\OneDrive - Universidad internacional de valencia\2-MIND\cloud_computing"

pdfs = [
    "1-Tema1-CompUbicua.pdf",
    "2- Tema1-CompUbicua_cont.pdf",
    "2-3-Tema2-IntroduccionCloudComputing.pdf",
    "4-5 Tema3-ServiciosProveedoresCloud.pdf",
    "6 Tema4-MetodologiadeDesarrolloDespliegueAplicacionesParaNube.pdf"
]

all_content = {}

for pdf_file in pdfs:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    print(f"\n{'='*80}")
    print(f"Procesando: {pdf_file}")
    print(f"{'='*80}\n")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    full_text += f"\n--- Página {i+1} ---\n\n{text}\n"
            
            all_content[pdf_file] = full_text
            print(f"Extraídas {len(pdf.pages)} páginas")
            print(f"Primeros 500 caracteres:\n{full_text[:500]}")
            
    except Exception as e:
        print(f"Error procesando {pdf_file}: {e}")

# Guardar todo el contenido en archivos de texto
for pdf_name, content in all_content.items():
    output_file = pdf_name.replace('.pdf', '.txt')
    output_path = os.path.join(pdf_folder, output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n✓ Guardado: {output_file}")

print("\n✓ Extracción completa!")
