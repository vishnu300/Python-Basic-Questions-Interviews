import streamlit as st
from io import BytesIO
import pdfrw

def compress_pdf(input_pdf, output_pdf):
    
    with pdfrw.PdfReader(BytesIO(input_pdf)) as pdf:
        pdfopti = pdfrw.optimization.OptimizationOptions()
        pdfopti.image_compression_options.compress_images = True
        pdf.optimize_resources(pdfopti)

        with BytesIO() as output:
            pdf.write(output)
            return output.getvalue()

def main():
    st.title("PDF Compressor")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        compressed_pdf = compress_pdf(bytes_data, "compressed.pdf") 

        st.success("PDF Compressed!")

        st.download_button(
            label="Download Compressed PDF",
            data=compressed_pdf,
            file_name="compressed_" + uploaded_file.name,
            mime='application/pdf'
        )

if __name__ == '__main__':
    main()
