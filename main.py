import os
import ebooklib
from ebooklib import epub

def convert_epub_to_pdf(epub_file_path, output_dir):
    """Converts an EPUB file to PDF and saves it in the output directory."""

    # Read the EPUB file
    book = epub.read_epub(epub_file_path)

    # Create a PDF document
    pdf_doc = ebooklib.create_pdf_document(book)

    # Get the EPUB file name without extension
    epub_file_name = os.path.splitext(os.path.basename(epub_file_path))[0]

    # Construct the output PDF file path
    output_pdf_path = os.path.join(output_dir, epub_file_name + ".pdf")

    # Write the PDF content to the file
    with open(output_pdf_path, "wb") as pdf_file:
        pdf_file.write(pdf_doc)

    print(f"Converted {epub_file_path} to {output_pdf_path}")

# Specify the EPUB folder and output directory
epub_folder = "c:\\epub"  # Replace with your actual EPUB folder path
output_dir = "c:\\pdf"  # Replace with your desired output directory

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate through EPUB files in the folder
for filename in os.listdir(epub_folder):
    if filename.endswith(".epub"):
        epub_file_path = os.path.join(epub_folder, filename)
        convert_epub_to_pdf(epub_file_path, output_dir)