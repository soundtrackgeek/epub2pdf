import os
import pdfkit
import fitz  # Optional - For finer control over PDF layout

# Configuration for pdfkit
config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  # Adjust the path!

def convert_epub_to_pdf(input_file, output_file):
    """Converts an EPUB file to a PDF file.

    Args:
        input_file (str): Path to the input EPUB file.
        output_file (str): Path to the output PDF file.
    """

    # Basic conversion using pdfkit
    pdfkit.from_file(input_file, output_file, configuration=config)

    # Optional: Improve PDF layout with fitz
    if fitz:  # Check if fitz is installed
        doc = fitz.open(input_file)  # Open EPUB as a PyMuPDF document
        for page in doc:
            pix = page.get_pixmap()  # Render the page as an image
            pix.save(output_file.replace('.pdf', f'-page{page.number}.png'))  # Save the image
        doc.close()

        doc = fitz.open()  # Create a new PDF document
        for page_image in sorted(os.listdir(os.path.dirname(output_file))):
            if page_image.endswith('.png') and page_image.startswith(os.path.basename(output_file)[:-4]):
                img = fitz.open(os.path.join(os.path.dirname(output_file), page_image))
                rect = img[0].rect  # Full image dimensions
                pdf_page = doc.new_page(width=rect.width, height=rect.height)
                pdf_page.insert_image(rect, stream=img[0].get_image_data())
                os.remove(os.path.join(os.path.dirname(output_file), page_image))  # Cleanup
        doc.save(output_file)

if __name__ == '__main__':
    epub_folder = 'c:\\epub'

    # Ensure you have these libraries installed:
    # pip install pdfkit fitz-pymupdf

    for filename in os.listdir(epub_folder):
        if filename.endswith('.epub'):
            input_filepath = os.path.join(epub_folder, filename)
            output_filename = filename.replace('.epub', '.pdf')
            output_filepath = os.path.join(epub_folder, output_filename)
            convert_epub_to_pdf(input_filepath, output_filepath)
