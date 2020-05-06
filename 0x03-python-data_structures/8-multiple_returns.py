#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ''):
        sub = (len(sentence), None)
    else:
        sub = (len(sentence), sentence[0])
    return (sub)
