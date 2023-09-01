import ReadPDF
import re
import PyPDF2

# Function to check if a word starts with a vowel
def starts_with_vowel(word):
    return re.match(r"^[aeiouAEIOU]", word) is not None

input_pdf_path = "words.pdf"
output_pdf_path = "output.pdf"

# Open the input PDF
try:
    with open(input_pdf_path, "rb") as input_pdf:
        pdf_reader = PyPDF2.PdfReader(input_pdf)
        num_pages = len(pdf_reader.pages)

        vowel_words = []

        # Loop through each page and extract text
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Tokenize content into words
            words = re.findall(r'\b\w+\b', text)

            # Find words starting with vowels
            vowel_words.extend([word for word in words if starts_with_vowel(word)])
except FileNotFoundError:
    print(input_pdf_path, "not found.")
    exit()

# Create an output PDF with the vowel words
output_pdf = PyPDF2.PdfWriter()

for word in vowel_words:
    output_pdf.add_page(PyPDF2.PageObject.create_blank_page(width=100, height=100))
    output_pdf.pages[-1].mergePage(pdf_reader.pages[0])
    output_pdf.pages[-1].insert_text(word, 10, 10)

with open(output_pdf_path, "wb") as output_pdf_file:
    output_pdf.write(output_pdf_file)

print("Vowel words inserted into", output_pdf_path)
