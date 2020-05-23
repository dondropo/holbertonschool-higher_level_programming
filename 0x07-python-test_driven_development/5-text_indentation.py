#!/usr/bin/python3
def text_indentation(text):
    if not type(text) is str:
        raise TypeError("text must be a string")

    sp_chars = [':', '.', '?']
    if type(text) is not str:
        raise TypeError("text must be a string")
    idx = 0
    for j in text:
        if j in sp_chars:
            if text[idx + 1] is " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1

    idx = 0
    for j in text:
        if j in sp_chars:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1
    print(text, end='')
