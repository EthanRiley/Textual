'''
filename: textual.py
description: Reusable nlp framework
author: Ethan Gilworth, Rithesh
'''
from collections import Counter, defaultdict
from distutils import text_file
import random as rnd
import matplotlib.pyplot as plt
import json
from pyparsing import WordStart
from textblob import TextBlob
from MakeSankey import make_sankey
import pandas as pd
import PyPDF2 as pdf
import plotly.graph_objects as go
import plotly.io as pio
import seaborn as sns

class textual:
    
    version = "0.01"


    def __init__(self):
        self.data = defaultdict(dict)

    @staticmethod
    def avg_polarity(speech):
        '''
        Takes in speech string and returns average polarity as float
        Code by Rithesh
        '''
        sum1 = 0
        # output list of sentences from speech 
        lst_of_sent = speech.split('\n')
        
        # calculating avg sentence polarity 
        
        for sent in lst_of_sent:
            polar = TextBlob(sent).sentiment.polarity
            sum1 += polar
        return sum1 / len(lst_of_sent)


    @staticmethod
    def avg_subj(speech):
        '''
        Takes in speech string and returns average subjectivity as float
        Code by Rithesh
        '''
        sum1 = 0
        lst_of_sent = speech.split('\n') 
        # calculate avg sentence sebjectivity 
        for sent in lst_of_sent:
            sub = TextBlob(sent).sentiment.subjectivity
            sum1 += sub
        return sum1 / len(lst_of_sent)

    @staticmethod
    def filter_punct(text):
        '''
        Filters punctuation and replaces with proper character (blank or space)
        Code by Ethan and Rithesh
        '''
        text = text.lower()
        punctuation_to_blank = [',', ':', ";", "?", '<', '>', ".", "'", '"', '`', '!', '(', ')', '*']
        for character in punctuation_to_blank:
            text = text.replace(character, '')

        punctuation_to_space = ['\n', '-', '—']
        for character in punctuation_to_space:
            text = text.replace(character, ' ')
            
        text = text.split(' ')
        new_list = []
        for i in range(len(text)):
            if text[i] != '':
                new_list.append(text[i])
            else:
                pass
        return new_list

    @staticmethod
    def find_avg_word_length(words):
        '''
        Finds average length of words
        Code by Ethan
        '''
        character_count = 0
        word_count = len(words)
        # counts all the characters and letters in the speech
        for word in range(len(words)):
            character_count += len(words[word])
        
        return character_count / word_count

    @staticmethod
    def find_sentiment_count(words, sentiment_dict):
        '''
        Method from Ethan's president analysis assignment. Likely to be deleted
        '''
        count = 0
        for word in words.keys():
            if word in sentiment_dict:
                count += words[word]
        return count

    @staticmethod
    def filter_words(words, stop_words):
        '''
        Filters out stop words from dictionary of words
        Code by Ethan
        '''
        fwords = []
        for word in words:
            if word not in stop_words:
                fwords.append(word)
        return fwords

    @staticmethod
    def find_words_per_sentence(unfiltered, filtered):
        '''
        Find average sentence length
        Code by Ethan
        '''
        # Take unfiltered data and then count the splits on .
        sentence_count = len(unfiltered.split('.'))
        word_count = len(filtered)
            
        return word_count / sentence_count

    @staticmethod
    def unique_per_100(words):
        '''
        Finds number of unique words per 100 words
        Code by Ethan
        '''
        unique_words = len(Counter(words).keys())
        word_count = len(words)
        return (unique_words/word_count)*100

    @staticmethod
    def default_parser(text):
        '''
        Parsing method for .txt files
        Code by Ethan
        '''
        prewords = textual.filter_punct(text)
        words = textual.filter_words(prewords, textual.load_stop_words())
        wc = Counter(words)
        num = len(words)
        vocab_size = textual.unique_per_100(words)
        sentence_length = textual.find_words_per_sentence(text, words)
        word_length = textual.find_avg_word_length(words)
        polarity = textual.avg_polarity(text)
        subj = textual.avg_subj(text)
        return {'wordcount': wc, 'numwords': num, 'raw': words, 'word length': word_length, 
                'polarity': polarity, 'subjectivity': subj, 'vocab size': vocab_size, 'sentence length': sentence_length}
    
    @staticmethod
    def load_stop_words(stopfile='CombinedCode/stop_words.json'):
        '''
        Loads stop words file for filtering method
        Code by Ethan
        '''
        f = open(stopfile, encoding='utf8')
        raw = json.load(f)
        f.close()
        return raw

    def load_text(self, filename, label=None, parser=None):
        if parser is None:
            results = textual.default_parser(filename, )
        else:
            results = parser(filename)

        if label is None:
            label = filename

        for k, v in results.items():
            self.data[k][label] = v 

    def compare_num_words(self):
        num_words = self.data['numwords']
        for label, nw in num_words.items():
            plt.bar(label, nw)
        plt.show

    def word_count_sankey(self, word_list=None, k=5, title='1'):
        '''
        Generates Sankey Diagram to show how words link together
        Code by Ethan
        '''
        df = textual.word_count_df(self.data['wordcount'], word_list, k)
        textual.make_sankey(df, 'Source', 'Target', 'Count', filename=title)


    @staticmethod
    def combine_txt(txt_list):
        '''
        Combines txt files into one large string
        Code by Ethan
        '''
        new_text = ''
        for txt in txt_list:
            text_file = open(txt, encoding='utf-8')
            text = text_file.read()
            new_text = new_text + text

            text_file.close()
        return new_text

    @staticmethod
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
        word_length = textual.find_avg_word_length(words)
        polarity = textual.avg_polarity(words)
        subj = textual.avg_subj(words)
        f.close()
        return {'wordcount': wc, 'numwords': num, 'raw': words, 'word length': word_length, 
                'polarity': polarity, 'subjectivity': subj, 'vocab size': vocab_size, 'sentence length': sentence_length}


    @staticmethod
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
        word_length = textual.find_avg_word_length(words)
        polarity = textual.avg_polarity(words)
        subj = textual.avg_subj(words)
        f.close()
        return {'wordcount': wc, 'numwords': num, 'raw': words, 'word length': word_length, 
                'polarity': polarity, 'subjectivity': subj, 'vocab size': vocab_size, 'sentence length': sentence_length}

    @staticmethod
    def txt_parser(filename):
        f = open(filename)
        text = f.read()
        prewords = textual.filter_punct(text)
        words = textual.filter_words(prewords, textual.load_stop_words())
        wc = Counter(words)
        num = len(words)
        vocab_size = textual.unique_per_100(words)
        sentence_length = textual.find_words_per_sentence(text, words)
        word_length = textual.find_avg_word_length(words)
        polarity = textual.avg_polarity(words)
        subj = textual.avg_subj(words)
        f.close()
        return {'wordcount': wc, 'numwords': num, 'raw': words, 'word length': word_length, 
                'polarity': polarity, 'subjectivity': subj, 'vocab size': vocab_size, 'sentence length': sentence_length}

    @staticmethod
    def dict_df(dict):
        dict_items = dict.items()
        data_list = list(dict_items)

        df = pd.DataFrame(data_list)

        return df.T
    
    @staticmethod
    def word_count_df(dict, word_list=None, k=5):
        df = pd.DataFrame()
        new_word_list = []
        if word_list != None:
                new_word_list = list(set(word_list+new_word_list))
                print(new_word_list)
        for item in dict.keys():
            for i in dict[item].most_common(k):
                new_word_list.append(i[0])
                new_word_list = list(set(new_word_list))
                for word in new_word_list:
                    new_row = {'Source':item, 'Target': word, 'Count':dict[item][word]}
                    df = df.append(new_row, ignore_index=True)       
        return df


    @staticmethod
    def combined_df(list_of_songs):
        final_df = pd.DataFrame()
        for song in list_of_songs:
            if song[-3:] == "txt":
                song_dict = textual.txt_parser(song)
                df = textual.dict_df(song_dict)
                final_df.append(df)

            elif song[-3:] == "pdf":
                song_dict = textual.pdf_parser(song)
                df = textual.dict_df(song_dict)
                final_df.append(df)

            elif song[-3:] == "son":
                song_dict = textual.json_parser(song)
                df = textual.dict_df(song_dict)
                final_df.append(df)

    @staticmethod
    def code_mapping(df, src, targ):
        """ map labels in src and targ columns to integers """
        labels = list(df[src]) + list(df[targ])
        #labels = sorted(list(set(labels)))
        
        #print(labels)
        
        codes = list(range(len(labels)))
        #print(codes)
        
        lcmap = dict(zip(labels, codes))
        #print(lcmap)
        
        df = df.replace({src: lcmap, targ: lcmap})
        #print(df)
        
        return df, labels

    @staticmethod
    def create_df(song_list):
        final_data = pd.DataFrame()

        for song in song_list:
            song_name = song.split('/')[2]
            song_name = song_name.split('.')[0]
            
            txt_string = textual.combine_txt(song)

            song_data = textual().load_text(txt_string, song_name)

            final_data = final_data.append(song_data)

        return final_data

    @staticmethod
    def make_sankey(df, src, targ, vals=None, filename='1', **kwargs):
        df, labels = textual.code_mapping(df, src, targ)
        
        
        if vals:
            value = df[vals]
        else:
            value = [1] * df.shape[0]
        
        
        link = {'source':df[src], 'target':df[targ], 'value':value}
        
        pad =kwargs.get('pad', 100)
        thickness = kwargs.get('thickness', 10)
        line_color = kwargs.get('line_color', 'black')
        width = kwargs.get('width', 2)

        node = {'pad':pad, 'thickness':thickness,
                'line':{'color':line_color, 'width':width},
                'label':labels}
        
        sk = go.Sankey(link=link, node=node)
        fig = go.Figure(sk)
        fig.write_image('sankey_{}.jpg'.format(filename))

    @staticmethod
    def make_boxplots(df, x_var, y_var):

        sns.set()

        fig, axes = plt.subplots(3, 2)

        artists = ['Drake', 'Kendrick', 'Kanye']

        for i in range(len(artists)):
            artist_name = artists[i]
            artist_albums = df.loc[df['Album_name'] == artist_name]
        
            sns.barplot(data=artist_albums, x=x_var, y=y_var, hue='Album_name', ax=axes[i])



        # sns_plot = sns.boxplot(data=df.loc[df['Artists'] == 'Drake'], x='Polarity', y='Subjectivity')
        # sns.boxplot(data=df.loc[df['Artists'] == 'Kanye'], x='Polarity', y='Subjectivity', ax=axes[0,1])
        # sns.boxplot(data=df.loc[df['Artists'] == 'Kendrick'], x='Polarity', y='Subjectivity', ax=axes[1,0])
        # sns_plot.figure.savefig("output.png")

