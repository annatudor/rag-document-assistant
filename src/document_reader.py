from pathlib import Path
from pypdf import PdfReader

def check_file_type(file_path):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    if path.suffix.lower() not in ['.txt', '.pdf']:
        raise ValueError(f"Unsupported file type: {path.suffix}. Only .txt and .pdf files are supported.")
    return path.suffix.lower()

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = []
    for page in reader.pages:
        text.append(page.extract_text() or "")
    return "\n".join(text)

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_documents(directory_path):
    directory = Path(directory_path)
    file_info = []
    for file_path in directory.iterdir():
        if not file_path.is_file() or file_path.suffix.lower() not in ['.txt', '.pdf']:
            continue
        if check_file_type(file_path) == '.txt':
            text = read_txt(file_path)
        else:
            text = read_pdf(file_path)
        file_info.append({"source": file_path.name, "text": text})
    return file_info
