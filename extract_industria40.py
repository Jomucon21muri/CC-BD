#!/usr/bin/env python3
"""
Script para extraer contenido del PDF de Industria 4.0 y Big Data
"""

import pdfplumber
import os

def extract_industria40_pdf():
    """Extrae el contenido del PDF de Industria 4.0"""
    
    pdf_path = r'Bigdata\Presentacion-Teoria-industria 4.0.pdf'
    output_path = r'Bigdata\Presentacion-Teoria-industria-4.0-extracted.txt'
    
    print(f"Extrayendo: {pdf_path}")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"Total de páginas: {total_pages}")
            
            full_text = []
            
            for i, page in enumerate(pdf.pages, 1):
                print(f"Procesando página {i}/{total_pages}...", end='\r')
                
                # Extraer texto
                text = page.extract_text()
                
                if text:
                    full_text.append(f"\n{'='*60}\n")
                    full_text.append(f"PÁGINA {i}\n")
                    full_text.append(f"{'='*60}\n\n")
                    full_text.append(text)
                    full_text.append("\n")
            
            # Guardar todo el texto
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(''.join(full_text))
            
            print(f"\n✓ Extracción completada")
            print(f"  Páginas procesadas: {total_pages}")
            print(f"  Archivo generado: {output_path}")
            print(f"  Tamaño: {len(''.join(full_text))} caracteres")
            
            return output_path
            
    except Exception as e:
        print(f"\n✗ Error al procesar {pdf_path}: {str(e)}")
        return None

if __name__ == '__main__':
    print("="*60)
    print("EXTRACCIÓN DE PDF - INDUSTRIA 4.0 Y BIG DATA")
    print("="*60 + "\n")
    
    extracted_file = extract_industria40_pdf()
    
    if extracted_file:
        print(f"\n✅ Proceso completado exitosamente!")
        print(f"\n📄 Archivo listo para integrar: {extracted_file}")
    else:
        print(f"\n❌ Error en la extracción")
