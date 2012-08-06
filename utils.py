import re

def replace_words(text, word_dic):
    '''Replace *text* with words defined in *word_dict*.
    
    >>> str = 'The quick brown fox jumped over the lazy dog'
    >>> replace_words(str, {'quick': 'slow', 'brown': 'green',
    ...                     'fox': 'dog', 'dog': 'camel'})
    'The slow green dog jumped over the lazy camel'

    >>> str = 'Foo, Bar'
    >>> replace_words(str, {'Foo': 'Bar', 'Bar':'Foo'})
    'Bar, Foo'

    '''
    rc = re.compile('|'.join((re.escape(i) for i in word_dic)))
    def translate(match):
        return word_dic[match.group(0)]
    return rc.sub(translate, text)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
