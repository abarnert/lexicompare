# lexicompare
Simple wrapper to make any iterable compare lexicographically against any other.

If you have two iterables of (possibly) different types, or of a type that doesn't 
compare like sequence types do, and you want to compare them the same way 
sequences compare, just wrap one in lexicompare.

The name is short for "lexicographical compare", because that's what sequences do.

    >>> (1,2,3) == [1,2,3]
    False
    >>> lexicompare(1,2,3) == [1,2,3]
    True
    >>> (1,2,3) == lexicompare([1,2,3])
    True
    >>> (1,2) < [1,2,3]
    TypeError: '<' not supported between instances of 'tuple' and 'list'
    >>> lexicompare(1,2) < [1,2,3]
    True

