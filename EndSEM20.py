# 20. Replace vowels with '*'
s = "education"
for vowel in 'aeiouAEIOU':
    s = s.replace(vowel, '*')
print(s)