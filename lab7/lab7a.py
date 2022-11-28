#from match import *
#from books import db

db = [[['författare', ['john', 'zelle']],
       ['titel', ['python', 'programming', 'an', 'introduction', 'to',
                  'computer', 'science']],
       ['år', 2010]],
      [['författare', ['armen', 'asratian']],
       ['titel', ['diskret', 'matematik']],
       ['år', 2012]],
      [['författare', ['j', 'glenn', 'brookshear']],
       ['titel', ['computer', 'science', 'an', 'overview']],
       ['år', 2011]],
      [['författare', ['john', 'zelle']],
       ['titel', ['data', 'structures', 'and', 'algorithms', 'using',
                  'python', 'and', 'c++']],
       ['år', 2009]],
      [['författare', ['anders', 'haraldsson']],
       ['titel', ['programmering', 'i', 'lisp']],
       ['år', 1993]]]


def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    # try:
    #     print(seq[0])
    # except:
    #     print("Mupp sekvens:" , seq)
    # try:
    #     print(pattern[0])
    # except:
    #     print("Muppmönster:", pattern)
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


# def search(pattern, seq):
#     """An expanded version of the match function
#     which can search with nested patterns"""

#     if not seq: # If the sequence is empty return an empty list
#         return []

#     if match(seq[0], pattern): # If the first element is a match
#                                  # return that element together with
#                                  # the result of searching the rest of 
#                                  # sequence
#         return [seq[0]] + search(pattern, seq[1:])

#     else: # If the first element is not a match, search the rest
#           # of the sequence
#         print("hej3")
#         return search(pattern, seq[1:])

def search(pattern, seq):
    # result = []
    # for element in seq:
    #     if match(element, pattern):
    #         result.append(element)
    return [i for i in seq if match(i,pattern)]
    # return result

#print(search(db, ['--', ['titel', ['&', '&']], '--']))

#print(search([['författare', ['&', 'zelle']],
#                    ['titel', ['--', 'python', '--']], ['år', '&']], db))
# print(search(db, ['--', ['år', 2042], '--']))
#    == [['författare', ['anders', 'haraldsson']],
#       ['titel', ['programmering', 'i', 'lisp']],
#       ['år', 1993]]

if __name__ == "__main__":
    assert search(['--', ['titel', ['&', '&']], '--'], db) == [[['författare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['år', 2012]]]
    assert search(['--', ['ar', 2042], '--'], db) == []
    assert search([['författare', ['&', 'zelle']], ['titel', ['--', 'python', '--']], ['år', '&']], db) == [[['författare', ['john', 'zelle']],
    ['titel',
    ['python',
    'programming',
    'an',
    'introduction',
    'to',
    'computer',
    'science']],
    ['år', 2010]],
    [['författare', ['john', 'zelle']],
    ['titel',
    ['data',
    'structures',
    'and',
    'algorithms',
    'using',
    'python',
    'and',
    'c++']],
    ['år', 2009]]]
    
    assert search(['--'], [['hej', 'då'], ['då', 'hej']]) == [['hej', 'då'], ['då', 'hej']] #Vid '--' matchar båda huvudelementen
    assert search(['hej', '&', 'då'], db) == [] # Pattern doesnt match seq
    assert search([], db) == [] # If pattern is empty
    assert search([], []) == [] # If seq and pattern is empty
    assert search(['hej'], []) == [] # If seq is empty
    assert search(['--', '--', 'a', '&', 'b', '--'], ['a.b']) # Checking that all symbols work
    print("Search has passed all tests")