from match import match
from books import db

def search(seq: list(), pattern: list())-> list():
    """An expanded version of the match function
    which can search with nested patterns"""

    if not seq: # If the sequence is empty return an empty list
        return []

    if match(seq[0], pattern): # If the first element is a match
                                 #return that element together with
                                 # the result of searching the rest of 
                                 # sequence
        return [seq[0] + search(seq[1:], pattern)]

    else: # If the first element is not a match, seacrh the rest
          # of the sequence
        return search(seq[1:], pattern)