from pypdf import PdfReader


def read_file(file):
    reader = PdfReader(file)
    text = []
    for page in reader.pages:
        if page.extract_text():
            text.append(page.text())
    return '\n'.join(text)