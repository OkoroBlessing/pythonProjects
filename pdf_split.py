import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the input PDF file  
    with open(input_pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        
        # Iterate through each page in the PDF
        for page_number in range(len(pdf_reader.pages)):
            # Create a new PDF writer for each page
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_number])
            
            # Write the page to a new PDF file
            output_pdf_path = os.path.join(output_folder, f'page_{page_number + 1}.pdf')
            with open(output_pdf_path, 'wb') as output_file:
                pdf_writer.write(output_file)

# Example usage
input_pdf_path = r"C:\Users\Blessing\Documents\admisson folder\documents.pdf"  # Replace 'input.pdf' with the path to your input PDF file
output_folder = r"C:\Users\Blessing\Documents\admisson folder\suffix"  # Replace 'output_folder' with the desired output folder
split_pdf(input_pdf_path, output_folder)
