"""
1) extract_data: Extracts <div class = "comments"> tags in the data extracted from facebook.
2) process_txt: Extracts the sentences 
3) write_file: Transfers the sentences to a csv file default file name is "FBextract.csv"

"""

from __future__ import print_function
import csv
import os
import random
import math
random.seed(1337)

import nltk.data
from bs4 import BeautifulSoup

#Specify location of timeline.htm file here
fb_data = './Data/html/timeline.htm'


def extract_data(input_file):
    """
    Extracts data from the input_file '../../timeline.htm'
    looks out <div class = "comment"> and extracts the following comment information
    Dumps the comments in to a file, checks whether file already exists.

    :param input_file: specify location of 'timeline.htm' (str)
    :param output_file: specify the output filename (str)
    :return: data: list of strings
    """

    # Opens file and closes, stores the file in output
    print("Reading {}...".format(input_file))
    with open(input_file,"r") as f:
        output = f.read()
    print("Read Complete\n")



    # Parse output string data using BeautifulSoup
    print('Extracting <div class="comment">')
    soup = BeautifulSoup(output, "html.parser")
    extract_div = soup.find_all("div", {"class":"comment"})
    print('Extract Complete\n')



    # Extract_div now contains a list of bs4.element.Tag
    # Parse into list of strings and output into csv file
    # Use nltk to split into sentences and collect the sentences
    sentence_detector = nltk.data.load("tokenizers/punkt/english.pickle")
    sentences = []

    print('Parsing Sentences')
    for item in extract_div:
        # Split item if there are \n characters
        new_item = item.text.split("\n")

        # Split into sentences using nltk
        for text in new_item:
            temp = sentence_detector.tokenize(text)

            # Filter out some useless tokens
            for tokens in temp:
                if tokens != "!" and tokens != "?" and tokens != "'," and \
                tokens != '"""' and tokens != "..." and tokens != "),":
                    sentences.append(tokens)

    print('Parse Sentences Complete\n')


    # Split the sentences into 3 parts 60% train, 20% valid, 20% test
    print('Shuffling sentences')
    random.shuffle(sentences)
    print('Shuffle complete\n')

    train_list = sentences[0:math.floor(len(sentences)*0.6)]
    valid_list = sentences[math.floor(len(sentences)*0.6):math.floor(len(sentences)*0.8)]
    test_list = sentences[math.floor(len(sentences)*0.8):len(sentences)]

    # Output the list of parsed sentences into train.txt valid.txt test.txt consolidate.txt
    with open("train.txt", 'w', newline='') as train:
        for item in train_list:
            train.write("{}\n".format(item))

    with open("valid.txt", 'w', newline='') as valid:
        for item in valid_list:
            valid.write("{}\n".format(item))

    with open("test.txt", 'w', newline='') as test:
        for item in test_list:
            test.write("{}\n".format(item))

    with open("consolidate.txt", 'w', newline='') as consolidate:
        for item in sentences:
            consolidate.write("{}\n".format(item)


if __name__ == "__main__":
    extracted_data = extract_data(fb_data)

