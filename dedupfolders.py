# Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in the file system.

# For example, ["one", "two", "three"] represents the path "/one/two/three".
# Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical. If two or more folders are identical, then mark the folders as well as all their subfolders.

# For example, folders "/a" and "/b" in the file structure below are identical. They (as well as their subfolders) should all be marked:
# /a
# /a/x
# /a/x/y
# /a/z
# /b
# /b/x
# /b/x/y
# /b/z
# However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be considered identical even with the added folder.
# Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.

# Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order.

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.delete = False

    def add(self, word):
        curr = self
        for c in word:
            curr = curr.children[c]

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()
        for path in sorted(paths):
            root.add(path)
        def serialize(t):
            if not t.children:return ""
            s = []
            for folder, child in t.children.items():
                s.append(folder + '(' + serialize(child) +')')
            key = "".join(s)
            seen[key].append(t)
            return key

        seen = defaultdict(list)
        serialize(root)

        for nodes in seen.values():
            if len(nodes) >= 2:
                for node in nodes:node.delete= True
        def dfs(root, path):
            for folder, child in root.children.items():
                if not child.delete:
                    curr = path + [folder]
                    res.append(curr)
                    dfs(child, curr)
        res = []
        dfs(root, [])
        return res

paths= [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
s = Solution()
print("Expected Output: [["d"],["d","a"]]")
print("Actual Output: ",s.deleteDuplicateFolder(paths))
