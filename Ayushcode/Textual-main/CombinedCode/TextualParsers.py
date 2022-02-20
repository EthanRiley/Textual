import json
from collections import Counter
from Textual import textual
import PyPDF2 as pdf
import pandas as pd


class_object = textual()

def json_parser(filename):
    '''
    Parsing method for JSON files
    Code from class
    '''
    f = open(filename)
    raw = json.load(f)
    text = raw['text']
    prewords = textual.filter_punct(text)
    words = textual.filter_words(prewords, textual.load_stop_words())
    wc = Counter(words)
    num = len(words)
    vocab_size = textual.unique_per_100(words)
    sentence_length = textual.find_words_per_sentence(text, words)
    f.close()
    return {'wordcount': wc, 'numwords': num, 'raw': words, 'text': filename, 
            'vocab size': vocab_size, 'sentence length': sentence_length}

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
    
    prewords = textual.filter_punct(text)
    words = textual.filter_words(prewords, textual.load_stop_words())
    vocab_size = textual.unique_per_100(words)
    sentence_length = textual.find_words_per_sentence(text, words)
    wc = Counter(words)
    num = len(words)
    f.close()
    return {'wordcount': wc, 'numwords': num, 'raw': words, 'text': filename, 
            'vocab size': vocab_size, 'sentence length': sentence_length}

def txt_parser(filename):
    f = open(filename)
    text = f.read()
    prewords = textual.filter_punct(text)
    words = textual.filter_words(prewords, textual.load_stop_words())
    wc = Counter(words)
    num = len(words)
    vocab_size = textual.unique_per_100(words)
    sentence_length = textual.find_words_per_sentence(text, words)

    f.close()
    return {'wordcount': wc, 'numwords': num, 'raw': words, 'text': filename, 
            'vocab size': vocab_size, 'sentence length': sentence_length}

def dict_df(dict):
    dict_items = dict.items()
    data_list = list(dict_items)

    df = pd.DataFrame(data_list)

    return df


def combined_df(list_of_songs):
    final_df = pd.DataFrame()
    for song in list_of_songs:
        if song[-3:] == "txt":
            song_dict = txt_parser(song)
            df = dict_df(song_dict)
            final_df.append(df)

        elif song[-3:] == "pdf":
            song_dict = pdf_parser(song)
            df = dict_df(song_dict)
            final_df.append(df)

        elif song[-3:] == "son":
            song_dict = json_parser(song)
            df = dict_df(song_dict)
            final_df.append(df)

    # ASSERT STATEMENT HERE else print("type not supported")
