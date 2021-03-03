import re

# re = regular expression
# def: A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings,
# using a specialized syntax held in a pattern.

myre = re.compile('a+b+')

examples = ['ab', 'aab', 'abb', 'aaabbb', 'ca', 'abab']

for e in examples:
    if myre.match(e):
        ismatch = True
    else:
        ismatch = False
    print(f"{e} -> {ismatch}")