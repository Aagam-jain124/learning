import PyPDF2

def merge_pdfs(input_pdfs, output_pdf):
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfFileMerger()

    try:
        # Loop through the input PDF files and append them to the merger
        for pdf_file in input_pdfs:
            pdf_merger.append(pdf_file)

        # Write the merged PDF to the output file
        with open(output_pdf, 'wb') as output_file:
            pdf_merger.write(output_file)

        print(f'Merged {len(input_pdfs)} PDF files into {output_pdf}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
    finally:
        # Close the PDF merger
        pdf_merger.close()

# Usage example
if __name__ == '__main__':
    input_files = [
        'pdf 1-Untitled document (1).pdf',
        'pdf 2- \', \'Circular - 2023 (2).pdf'
    ]  # Replace with your PDF file names
    output_file = 'merged.pdf'  # Replace with the desired output file name

    merge_pdfs(input_files, output_file)
