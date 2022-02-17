import json
from collections import Counter
from Textual import textual
import PyPDF2 as pdf

class_object = textual()

def json_parser(filename):
    '''
    Parsing method for JSON files
    Code from class
    '''
    f = open(filename)
    raw = json.load(f)
    text = raw['text']
    words = text.split(" ")
    wc = Counter(words)
    num = len(words)
    f.close()
    return {'wordcount': wc, 'numwords': num, 'raw': words}

def txt_parser(filename):
    '''
    Parsing method for .txt files
    Code by Ethan
    '''
    f = open(filename)
    read_f = f.read()
    read_f = textual.filter_punct(read_f)
    words = read_f.split(' ')
    wc = Counter(words)
    num = len(words)
    f.close()
    return {'wordcount': wc, 'numwords': num, 'raw': words}

def pdf_parser(filename):
    '''
    Parsing method for PDF files
    Code by Ethan and Rithesh
    '''
    f = open(filename, 'rb')
    pdfObj = pdf.PdfFileReader(f)
    
    text = ''
    for page in range(pdfObj.numPages):
        new_page = pdfObj.getPage(page)
        new_text = new_page.extractText()
        text = text + new_text
    
    words = textual.filter_punct(text)
    wc = Counter(words)
    num = len(words)
    f.close()
    return {'wordcount': wc, 'numwords': num, 'raw': words}