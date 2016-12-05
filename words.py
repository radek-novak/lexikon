#!/usr/bin/env python
# coding: utf-8
# run with PYTHONIOENCODING=utf-8

import sys
import re
import codecs

# not used, but possibly interesting http://www.nltk.org/

# http://www.clips.ua.ac.be/pages/pattern-de
from pattern.de import lemma, tag, predicative, singularize

# possible parts of speech:
# PRP$, FW, VBN, WDT, JJ, WP, DT, RP, NN, TO, PRP,
# RB, NNS, NNP, VB, WRB, CC, LS, CD, IN, MD, UH
part_of_speech_command = {
    'PRP$': lambda word: predicative(word), # pronomina
    'VBN': lambda word: lemma(word), # verba
    'DT': lambda word: predicative(word), # pronomina
    'VB': lambda word: lemma(word), # verba
    'NN': lambda word: singularize(word), # nomina
    'JJ': lambda word: predicative(word) # preposice
}

pattern_word = re.compile('[a-zA-Z]')
pattern_punctuation = re.compile(ur'[—\-|«»…–<>]')

def transform(tagword):
    word = tagword[0]
    part = tagword[1]
    # if part == 'VBN':
    #     print tagword

    # word must contain some letters
    if not bool(pattern_word.match(tagword[0])):
        return None

    # everything else than nouns should be lowecase
    if part != 'NN':
        word = word.lower()

    if part in part_of_speech_command:
        return part_of_speech_command[part](word)
    else:
        return word

def main(filepath):
    text = ''

    with codecs.open(filepath, 'r', 'utf-8') as f:
        text = f.read()

    text = pattern_punctuation.sub(' ', text)
    tagged_words = tag(text)

    word_counts = {}

    for tagword in tagged_words:
        transformed_word = transform(tagword)

        if transformed_word == None:
            continue

        if transformed_word in word_counts:
            word_counts[transformed_word] += 1
        else:
            word_counts[transformed_word] = 1


    tuple_list = sorted(word_counts.items(), key=lambda tupl_word: word_counts[tupl_word[0]], reverse=True)

    for tupl in tuple_list:
        print tupl[1], tupl[0]


if __name__ == '__main__':
    main(sys.argv[1])
