# !pip install PyPDF2
import PyPDF2
import re

# Uso do PyPDF2
def pdf_to_text(pdf_path, page_start, page_end):
    text = ""
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(page_start, page_end):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Formatar as linhas de forma que comece com os termos
def filter_page_number(lines, page_regex):
    # Extract page numbers
    '''
    Detalhe para alguns PDFs: a quebra de linha ou página
    que retiramos aqui pode estar dentro das linhas (ou seja nao
    podemos deletar a linha toda). Ajustar.
    '''
    return [l for l in lines if not page_regex.match(l)]

#------------------>  Older Functions

# Transformar em tripla
def transform_to_triple(lines, delimiter_regex, rdf_predicate):
    # Mudar aqui para a tripla
    output_lines = []
    # Use a função sub() para fazer a substituição
    for line in lines:
        line = re.sub(delimiter_regex, rdf_predicate, line, count=1)
        output_lines.append(line)

    return output_lines