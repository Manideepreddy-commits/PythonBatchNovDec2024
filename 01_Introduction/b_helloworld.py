

#!usr/bin/python
"""
purpose: Basic pep 8 Guidelines and 
         shebang line

PEP:Python Enhancement Proposal
PEP 8: Coding Style

This is docstring

"""
#print as a statement in python02
#print"Hello world!"

#print as a funtion in python 2&3
print("Hello wolrd!")
print(True)
print("True",123,None)

def wishes(name):
    wish="How are you{0}?".format(name)
    print(wish)

wishes("uday")