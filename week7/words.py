file = open('document.txt')
lines = file.readlines()

find_word = input('Give a word: ').strip().lower()

counter = 0
for line in lines:
    line = line.strip().lower()
    if len(line) > 0:
        words = line.split()
        counter += words.count(find_word)
    
print(f"The word '{find_word}' exists {counter} times in the document. ")
