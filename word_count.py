#enter via keyboard a phrase, output number of words, only counting letters
phrase = input('Enter a phrase: ')
filtered_phrase = ''
words = []
count = 0

for i in range(len(phrase)): #leaves only letters and spaces
    if phrase[i].isalpha() or phrase[i].isspace(): #if in this position i = simbol or space
        filtered_phrase = filtered_phrase + phrase[i]

words = filtered_phrase.split(' ')

for i in range(len(words)):
    if words[i].isalpha():
        count += 1

print('The entered phrase has', count,'words')
