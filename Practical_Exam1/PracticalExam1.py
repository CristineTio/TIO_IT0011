import string


def count_words (string):
    exclude = ['and', 'but', 'or', 'nor', 'for', 'so', 'yet', 'a', 'an', 'the',]
print(str("Enter a string: "))

words = str.split(",")
words_filtered = [word.lower() for word in words]

uniwords = set(words_filtered)
word_freq = [words_filtered.count(word) for word in uniwords]

lowercase_words = [word.islower() for word in words ]
upper_case_words = [word.isupper() for word in words]

sorted_lowerwords = sorted(lowercase_words.item(), key=lambda x: x[1], reverse=True)
sorted_upperwords = sorted(upper_case_words.item(), key=lambda x: x[1], reverse=True)

sorted_words = (sorted_lowerwords + sorted_upperwords)

print("String: ", string)
print("Total words filtered: ", sorted_lowerwords + sorted_upperwords)