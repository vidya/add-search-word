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


from collections import namedtuple

Node = namedtuple('Node', ['ch', 'end_of_word', 'next_nodes'])


class WordDictionary:
    def __init__(self):
        # init an empty trie
        self.root = []

    def addWord(self, word):
        word_len = len(word)
        if word_len == 0:
            return

        nodes = self.root
        for n, ch in enumerate(word):
            # check if ch occurs as a node in the trie
            match_found = False
            for node in nodes:
                if ch == node.ch:
                    match_found = True
                    nodes = node.next_nodes
                    break

            # no node in the trie for ch
            if not match_found:
                # create and add a node for ch
                node = Node(ch=ch, end_of_word=(n == word_len - 1), next_nodes=[])
                nodes.append(node)

                nodes = node.next_nodes

    def search(self, word):
        # return False if the trie has no nodes
        if not self.root:
            return False

        # return True if the word is an empty string
        if not word:
            return True

        # start the search at level 0 of the trie
        nodes_at_level = self.root
        word_len = len(word)

        # iterate over each char of the word
        for n, ch in enumerate(word):
            if ch == '.':
                # wild char match. Any char at this level would do.

                if n == word_len - 1:
                    # reached end of the word we are searching for
                    return any([n.end_of_word for n in nodes_at_level])

                # there are more chars in word
                next_level_nodes = [node.next_nodes for node in nodes_at_level]

                # look for the next char of the word at the next level of the trie
                nodes_at_level = []
                for nn in next_level_nodes:
                    nodes_at_level.extend(nn)

                continue

            # current char of the search word is not '.'
            if all([ch != n.ch for n in nodes_at_level]):
                return False

            # get a list of nodes containing the current char of the search word
            nodes_with_ch = [node for node in nodes_at_level if ch == node.ch]

            if n == word_len - 1:
                # reached end of the word we are searching for
                return any([n.end_of_word for n in nodes_with_ch])

            # look for the next char of the word at the next level of the trie
            nodes_at_level = []
            for cn in nodes_with_ch:
                nodes_at_level.extend(cn.next_nodes)


