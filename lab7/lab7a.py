#from match import *
from books import db

def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
        
    elif pattern[0] == '--':

        if match(seq, pattern[1:]):
            return True

        elif not seq:
            return False

        else:
            return match(seq[1:], pattern)

    

    elif not seq:
        return False

    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])

    elif seq[0] == pattern[0]:
        if len(seq) == 1:
            return True
        else:
            return match(seq[1:], pattern[1:])

    elif isinstance(pattern[0], list):
        if isinstance(seq[0], list):
            if match(seq[0], pattern[0]) and match(seq[1:], pattern[1:]):
                return True
        else:
            return False
    else:
        return False



def search(pattern, seq):
    """An expanded version of the match function
    which can search with nested patterns"""

    if not seq: # If the sequence is empty return an empty list
        print("hej1")
        return []

    if match(seq[0], pattern): # If the first element is a match
                                 # return that element together with
                                 # the result of searching the rest of 
                                 # sequence
        print("hej2")
        return [seq[0]] + search(pattern, seq[1:])

    else: # If the first element is not a match, search the rest
          # of the sequence
        print("hej3")
        return search(pattern, seq[1:])


# def search(pattern, seq):
#     result = []
#     for element in seq:
#         if match(element, pattern):
#             result.append(element)
#     return result

#print(search(db, ['--', ['titel', ['&', '&']], '--']))

#print(search([['författare', ['&', 'zelle']],
#                    ['titel', ['--', 'python', '--']], ['år', '&']], db))
# print(search(db, ['--', ['år', 2042], '--']))
#    == [['författare', ['anders', 'haraldsson']],
#       ['titel', ['programmering', 'i', 'lisp']],
#       ['år', 1993]]