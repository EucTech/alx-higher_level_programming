#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    for i in sentence:
        if i == "":
            i[0] = None
        else:
            return length, i[0]
