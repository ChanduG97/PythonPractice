### 8. Two words are anagrams if they contain all of the same letters, but in a different order. For example, “evil” and “live” are anagrams because each contains one e, one i, one l, and one v. Create a program that reads two strings from the user, determines whether or not they are anagrams, and reports the result.

str1 = input('Enter the first sentance: ')
str2 = input('Enter the second sentance: ')
len1 = len(str1)
len2 = len(str2)
count = 0
for i in str1.lower():
    for j in str2.lower():
        if i in j:
            count+=1
        continue
if count == len1 and count == len2 and len1 == len2:
    print('The word',str1,"and",str2,'is an Anagram')
else:
    print('The word',str1,"and",str2,'is not an Anagram')