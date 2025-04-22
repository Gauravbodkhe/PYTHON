# 18. Words starting with vowels
words = ["apple", "banana", "orange", "umbrella", "cat"]
for word in words:
    if word[0].lower() in 'aeiou':
        print(word)