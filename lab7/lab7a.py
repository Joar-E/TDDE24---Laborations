
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
    """Returns a list of all matched parts of the given sequence"""
    
    return [i for i in seq if match(i, pattern)]



if __name__ == "__main__":
    assert search([['författare', ['--']], ['titel', ['--', 'python', '--']], ['år', '&']], db) ==\
        [[['författare', ['john', 'zelle']], 
        ['titel', ['python', 'programming', 'an', 'introduction', 'to', 'computer', 'science']],
        ['år', 2010]], [['författare', ['john', 'zelle']],
        ['titel', ['data', 'structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']],
        ['år', 2009]]]

    assert search([['författare', '--'], '--'], db) == db

    assert search(['--', ['&', ['diskret', 'matematik']], '--'], db) ==\
        [[['författare', ['armen', 'asratian']], \
            ['titel', ['diskret', 'matematik']], \
                ['år', 2012]]]

    assert search(['--', ['år', 2009], '--'], db) ==\
        [[['författare', ['john', 'zelle']],
       ['titel', ['data', 'structures', 'and', 'algorithms', 'using',
                  'python', 'and', 'c++']],
       ['år', 2009]]]

    assert search([], db) == []

    print('The search function has passed all tests!')