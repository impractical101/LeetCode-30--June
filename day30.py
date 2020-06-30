#Submitted by thr3sh0ld
#Complex prob using trie. Had to search for various threads. After hours this is the optimal easy to 
#understand code. Referred.
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.flag = False

class Solution:
    def __init__(self):
            self.root = TrieNode()
            self.result = []

    def insert(self, word):
            node = self.root
            for char in word:
                node = node.children[char]
            node.flag = True

    def findWords(self, mat, words):
            for i in words:
                self.insert(i)
            for j in range(len(mat)):
                for i in range(len(mat[0])):
                    self.dfs(self.root, mat, j, i)
            return self.result

    def dfs(self, node, mat, j, i, word=''):
            if node.flag:
                self.result.append(word)
                node.flag = False
            if 0 <= j < len(mat) and 0 <= i < len(mat[0]):
                char = mat[j][i]
                child = node.children.get(char)
                if child is not None:
                    word += char
                    mat[j][i] = None
                    self.dfs(child, mat, j + 1, i, word)
                    self.dfs(child, mat, j - 1, i, word)
                    self.dfs(child, mat, j, i + 1, word)
                    self.dfs(child, mat, j, i - 1, word)
                    mat[j][i] = char
