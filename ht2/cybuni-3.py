# def groupAna(groupAnagrams:list[str]) -> list[list[str]]:
#     resultAna = []
#     el = groupAnagrams.pop(0).split('')
#     for letter in el:
#         for word in groupAnagrams:
#             if letter not in word:
#                 resultAna.append(groupAnagrams[word])
# print(groupAna(["tsar", "rat", "tar", "star", "tars", "cheese"]))
def groupAnagrams(words):
    anagram_groups_dict = {}
    
    for word in words:
        sorted_word = tuple(sorted(word))
        if sorted_word in anagram_groups_dict:
            anagram_groups_dict[sorted_word].append(word)
        else:
            anagram_groups_dict[sorted_word] = [word]
    
    result = list(anagram_groups_dict.values())
    
    return result

input_words = ["tsar", "rat", "tar", "star", "tars", "cheese"]
result = groupAnagrams(input_words)
print(result)
