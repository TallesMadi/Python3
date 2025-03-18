# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

ROOT_PATH = Path(__file__).parent
ORGINAL_PASTE = ROOT_PATH / r'pdf'
NEW_PASTE = ROOT_PATH / 'novos_arquivos'

REPORT_BACEN = ORGINAL_PASTE / r'R20230210.pdf'
NEW_PASTE.mkdir(exist_ok=True)

reader = PdfReader(REPORT_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)

page0 = reader.pages[0]
image0 = page0.images[0]

# print(page0.extract_text())
# print(len(page0.images))
# with open(NEW_PASTE / image0.name, 'wb') as image:
#     image.write(image0.data)

writer = PdfWriter()
writer.add_page(page0)

# with open(NEW_PASTE / 'new_pdf.pdf', 'wb') as fp:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(fp)

merger = PdfMerger()

files = [
    NEW_PASTE / 'page0.pdf',
    NEW_PASTE / 'new_pdf.pdf',
]

for file in files:
    merger.append(file)

merger.write(NEW_PASTE / 'merged.pdf') 
merger.close()
