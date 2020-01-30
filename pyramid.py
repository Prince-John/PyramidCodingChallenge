# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:59:45 2019

@author: Prince John
"""

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def is_pyramid(word):
    """This method takes a string input which is in lowercase and without any whitespaces and returns a boolean
    value. """
    freq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
            'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for i in word:
        freq[i] += 1  # finds the frequency of each letter in the word.

    # sanatizing the freq by removeing any zeros and sorting
    freq_list = [value for value in freq.values() if value != 0]
    freq_list.sort()

    if freq_list[0] != 1:  # to eliminate any words where no letters have a freq of one
        return False

    for i in range(0, len(freq_list) - 1):  # checks if all the frequencies are in a strict order with a difference
        # of one.
        if freq_list[i + 1] - freq_list[i] != 1:
            return False

    return True


def sanitize_word(word):
    """This method returns a string in lowercase and trims any white space."""
    word = word.strip()
    word = word.lower()
    return word


class PyramidWord(Resource):
    def get(self, word):
        word = sanitize_word(word)
        return jsonify(is_pyramid(word))


api.add_resource(PyramidWord, '/<string:word>')

if __name__ == '__main__':
    app.run(debug=True)

