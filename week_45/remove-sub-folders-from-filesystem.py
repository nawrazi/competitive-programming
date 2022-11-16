# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Node:
    def __init__(self):
        self.children = {}
        self.folder = ''

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        system = [folder.split('/') for folder in folders]
        trie = Node()
        
        for folder in system:
            node = trie
            for file in folder:
                if file not in node.children:
                    node.children[file] = Node()
                node = node.children[file]
            node.folder = folder
            
        def isRoot(idx, folder, node):
            if node.folder:
                return idx == len(folder)
            return isRoot(idx + 1, folder, node.children[folder[idx]])
        
        roots = []
        for folder in system:
            if isRoot(0, folder, trie):
                roots.append('/'.join(folder))
                
        return roots
    
