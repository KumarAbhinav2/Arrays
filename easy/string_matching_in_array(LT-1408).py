"""
Given an array of string words. Return all strings in words which is substring of another word in any order.
String words[i] is substring of words[j], if can be obtained removing some characters to
left and/or right side of words[j]

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
"""

def stringMatching_baisc(words):
    res = set()
    for index, value in enumerate(words):
        if value in '$'.join(words[:index]+words[index+1]):
            res.add(value)
    return res

def stringMatching(words):
    # using trie concept
    def add(word):
        node = trie
        for c in word:
            node = node.setdefault(c, {})

    def get(word):
        node = trie
        for c in word:
            if node.get(c) is None: return False
        return True

    words.sort(key=len, reverse=True)
    trie, result = {}, []
    for word in words:
        if get(word): result.append(word)
        for i in range(len(word)):
            add(word[i:])
    return result

print(stringMatching(["mass","as","hero","superhero"]))