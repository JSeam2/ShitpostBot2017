import torch
import os
import argparse
import string
import random

from django.conf import settings

from .nnModel import *
from .helpers import *

def generate(decoder, prime_str="A", predict_len = 100, temperature = 0.8, cuda = False):
    hidden = decoder.init_hidden(1)
    prime_input = Variable(char_tensor(prime_str).unsqueeze(0))

    if cuda:
        hidden = hidden.cuda()
        prime_input = prime_input.cuda()

    predicted = prime_str

    for p in range(len(prime_str) -1):
        _, hidden = decoder(prime_input[:,p], hidden)

    inp = prime_input[:,-1]

    for p in range(predict_len):
        output, hidden = decoder(inp, hidden)

        output_dist = output.data.view(-1).div(temperature).exp()
        top_i = torch.multinomial(output_dist, 1)[0]

        predicted_char = all_characters[top_i]
        predicted += predicted_char

        inp = Variable(char_tensor(predicted_char).unsqueeze(0))

        if cuda:
            inp = inp.cuda()

    return predicted


def generate_web():
    rnnmodel = CharRNN(n_characters, 100, n_characters, 2)
    save_file = os.path.join(settings.BASE_DIR, "generator", "consolidate.pt")
    rnnmodel.load_state_dict(torch.load(save_file))
    random_char = random.choice(string.ascii_letters)
    return generate(rnnmodel, prime_str = random_char)

# for standalone script

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('filename', type=str)
    argparser.add_argument('-p', '--prime_str', type=str, default='A')
    argparser.add_argument('-l', '--predict_len', type=int, default=50)
    argparser.add_argument('-t', '--temperature', type=float, default=0.8)
    argparser.add_argument('--cuda', action='store_true')
    args = argparser.parse_args()

    rnnmodel = CharRNN(n_characters, 100, n_characters, 2)
    save_file = args.filename
    rnnmodel.load_state_dict(torch.load(save_file))
    del args.filename
    #decoder.eval()
    print(generate(rnnmodel))
