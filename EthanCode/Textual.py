'''
filename: textual.py
description: Reusable nlp framework
author: Ethan Gilworth, Rithesh
'''
from collections import Counter, defaultdict
import random as rnd
import matplotlib.pyplot as plt
import json

class textual:
    
    version = "0.01"


    def __init__(self):
        self.data = defaultdict(dict)

    @staticmethod
    def filter_punct(text):
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
        character_count = 0
        word_count = 0
        # counts all the characters and letters in the speech
        for word in range(len(words)):
            word_count += 1
            character_count += len(words[word])
        
        return character_count / word_count

    @staticmethod
    def find_sentiment_count(words, sentiment_dict):
        count = 0
        for word in words.keys():
            if word in sentiment_dict:
                count += words[word]
        return count

    @staticmethod
    def filter_words(words, stop_words):
        fwords = []
        for word in words:
            if word not in stop_words:
                fwords.append(word)
        return fwords

    @staticmethod
    def find_words_per_sentence(unfiltered, filtered):
        # Take unfiltered data and then count the splits on .
        sentence_count = len(unfiltered.split('.'))
        word_count = 0
        # Count the words once more
        for i in range(len(filtered)):
            word_count += 1
            
        return word_count / sentence_count

    @staticmethod
    def unique_per_100(words):
        unique_words = len(Counter(words).keys())
        word_count = 0
        
        for i in range(len(words)):
            word_count += 1
        
        return (unique_words/word_count)*100

    @staticmethod
    def _default_parser(filename):
        '''
        results = {
            'wordcount': Counter('to be or not to be'.split(' ')),
            'numwords': rnd.randrange(10,50)
        }
        Silly parser from class
        '''
        results = {}
        return results
    
    def load_stop_words(self, stopfile):
        f = open(stopfile, encoding='utf8')
        raw = json.load(f)
        self.stop_words = raw

    def load_text(self, filename, label=None, parser=None):
        if parser is None:
            results = textual._default_parser(filename)
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