import os
import torch
import csv

class Dictionary(object):
    def __init__(self):
        self.word2idx= {}
        self.idx2word = []

    def add_word(self, word):
        if word not in self.word2idx:
            self.idx2word.append(word)
            self.word2idx[word] = len(self.idx2word) - 1
        return self.word2idx[word]

    def __len__(self):
        return len(self.idx2word)


class Corpus(object):
    def __init__(self, path):
        """
        Path is the file path to the .csv file containing:w
        all the messages
        """
        self.dictionary = Dictionary()
        self.train, self.valid, self.text = self.tokenize(path)

    def tokenize(self, path)
        """
        Tokenizes the list of strings in the csv file
        """
        assert os.path.exists(path)

        # Add words to the dictionary
        with open(path, 'r') as f:
            tokens = 0
            f
