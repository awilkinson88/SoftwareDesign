import string
import random
from bisect import *

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def make_book_list(filename,skip_header=True):
    fp = file(filename)
    all_the_words = []

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        line = line.replace('-', ' ')
        x = line.split()
        all_the_words.extend(x)

    return all_the_words

def markov(all_the_words,prefix_count):

    final_dict = {}
    for i in range(len(all_the_words)-prefix_count-1):
        process_word(i, all_the_words, final_dict, prefix_count)
    return final_dict

def process_word(i, all_the_words, final_dict, prefix_count):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    prefixes = tuple(all_the_words[i:i + prefix_count])
    freq = final_dict.get(prefixes,{})
    nextword = all_the_words[i + prefix_count + 1]
    freq[nextword] = freq.get(nextword, 0) + 1
    final_dict[prefixes] = freq


def sample_words(all_the_words,prefix_count):
    num = random.randint(0,len(all_the_words)-1)
    preflist = []
    for i in range(prefix_count):
        word = all_the_words[num+i]
        preflist.append(word)
    prefixes = tuple(preflist)
    return prefixes


def wordsmash(prefixes,prefix_count,sample_size):
    # wordsmash((preflist[(prefix_count-1)],nextword),prefix_count,sample_size)
    while sample_size > 1:
        prefsuf_map = markov(all_the_words,prefix_count)
        sample_size = sample_size -1
        preflist = list(prefixes)
        try:
            suffixes = prefsuf_map[prefixes]
        except KeyError:
            suffixes = sample_words(all_the_words,1)
        sufflist = list(suffixes)
        num2 = random.randint(0,len(sufflist)-1)
        nextword = sufflist[num2]
        print nextword
        wordsmash((preflist[prefix_count],nextword),prefix_count,sample_size)
        break



prefix_count = 2
all_the_words = make_book_list('emma.txt')
prefsuf_map = markov(all_the_words,prefix_count)
startpref =  sample_words(all_the_words,prefix_count)
print startpref
wordsmash(startpref,1,10)