"""
https://leetcode.com/problems/add-and-search-word-data-structure-design/

211. Add and Search Word - Data structure design
Medium

Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)

search(word) can search a literal word or a regular expression string
containing only letters a-z or .. A . means it can represent any one
letter.

Example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

Note:
    You may assume that all words are consist of lowercase letters a-z.
"""


from addsearchword.addsearchword import WordDictionary


def test_3_basic():
    wd = WordDictionary()

    wd.addWord("a")

    assert wd.search("a")

    assert not wd.search("i")

    assert not wd.search("at")

    assert wd.search(".")

    assert not wd.search(".n")


def test_4_basic():
    wd = WordDictionary()

    wd.addWord("at")

    assert not wd.search("a")

    assert not wd.search("i")

    assert wd.search("at")

    assert not wd.search(".")

    assert not wd.search(".n")

    assert wd.search("..")

    assert wd.search("a.")

    assert not wd.search(".f")


def test_6_basic():
    wd = WordDictionary()

    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    assert not wd.search("pad")

    assert wd.search("bad")

    assert wd.search(".ad")

    assert wd.search("b..")

