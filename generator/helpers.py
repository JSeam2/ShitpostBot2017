import unidecode
import string
import random
import time
import math
import torch

all_characters = string.printable
n_characters = len(all_characters)

def read_file(filename):
    _file = unidecode.unidecode(open(filename).read())
    return _file, len(_file)

# Turn a string into a tensor
def char_tensor(string):
    tensor = torch.zeros(len(string)).long()
    for c in range(len(string)):
        try:
            tensor[c] = all_characters.index(string[c])

        except:
            continue

    return tensor

def time_since(since):
    s = time.time() - since
    m = math.floor(s/60)
    s -= m * 60
    return '%dm %ds' % (m, s)
