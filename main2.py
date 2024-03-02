import os
import subprocess

# Folder containing the .epub files
epub_folder = 'c:\\epub'
pdf_folder = 'c:\\pdf'

# Ensure the output folder exists
os.makedirs(pdf_folder, exist_ok=True)

# Convert each .epub file to .pdf
for file_name in os.listdir(epub_folder):
    if file_name.endswith('.epub'):
        epub_path = os.path.join(epub_folder, file_name)
        pdf_path = os.path.join(pdf_folder, file_name.replace('.epub', '.pdf'))
        subprocess.run(['ebook-convert', epub_path, pdf_path], check=True)

print('Conversion complete.')
