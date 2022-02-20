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
        
        # calculating avg sentence polarity 
        
        for sent in speech:
            polar = TextBlob(sent).sentiment.polarity
            sum1 += polar
        return sum1 / len(speech)


    @staticmethod
    def avg_subj(speech):
        '''
        Takes in speech string and returns average subjectivity as float
        Code by Rithesh
        '''
        sum1 = 0
        
        # calculate avg sentence sebjectivity 
        for sent in speech:
            sub = TextBlob(sent).sentiment.subjectivity
            sum1 += sub
        return sum1 / len(speech)

    @staticmethod
    def filter_punct(text):
        '''
        Filters punctuation and replaces with proper character (blank or space)
        Code by Ethan and Rithesh
        '''
        text = text.lower()
        punctuation_to_blank = [',', ':', ";", "?", '<', '>', ".", "'", '"', '`']
        for character in punctuation_to_blank:
            text = text.replace(character, '')

        punctuation_to_space = ['\n', '-']
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
        return {'wordcount': wc, 'numwords': num, 'raw': words, 
                'vocab size': vocab_size, 'sentence length': sentence_length}
    
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

    def word_count_sankey(self, word_list=None, k=5):
        '''
        Generates Sankey Diagram to show how words link together
        Code by Ethan
        '''
        pass

    @staticmethod
    def combine_txt(txt_list):
        new_text = ''
        for txt in txt_list:
            text_file = open(txt, encoding='utf-8')
            text = text_file.read()
            new_text = new_text + text

            text_file.close()
        return new_text