def main():
    english_words = input("Input the sentence in English: ").lower().split()
    pig_latin_words = map(convert_to_pig_latin, english_words)
    print(' '.join(pig_latin_words))
def convert_to_pig_latin(word):
    i = 0
    vowels = ['a', 'e', 'i', 'o','u','y']
    if word[0] in vowels:
        word += 'yay'
    else:
        while word[0] not in vowels:
            word = word[1:] + word[0]
        word += 'ay'
    return word

main()
