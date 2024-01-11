# ways - Trie and other
class WordDictionary(object):

    def __init__(self):
        self.lst = []
        


    def addWord(self, word):
        self.lst.append(word)

    def search(self, word):

        """
        :type word: str
        :rtype: bool
        """
        
