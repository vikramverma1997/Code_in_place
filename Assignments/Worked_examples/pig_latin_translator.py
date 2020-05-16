"""
Filename: pig_latin_translator
------------------------------
This program translates English language into Pig Latin language
"""

VOWELS = ['a', 'e', 'i', 'o', 'u']
PUNCTUATIONS = ['.', '?', '!']


def main():
    print('This program translates words/phrases from English to Pig Latin. To end the program. type EXIT')

    while True:
        user_input = input('Word/phrase to translate: ')

        if user_input == 'EXIT':
            break

        words_list = user_input.split(' ')
        output_string = ''

        for word in words_list:
            result_word, punctuation = delete_punctuation(word)

            if constant_sound(result_word[0]):
                first_vowel = find_first_vowel(result_word)
                first_vowel_index = result_word.find(first_vowel)
                if first_vowel != '':
                    translated_text = first_vowel + result_word[(first_vowel_index + 1):len(user_input)] + result_word[0:first_vowel_index] + 'ay' + punctuation + ' '
                else:
                    translated_text = result_word + 'ay' + punctuation + ' '
                output_string += translated_text
            if vowel_sound(result_word[0]):
                translated_text = result_word + 'yay' + punctuation + ' '
                output_string += translated_text

        print(output_string)


def delete_punctuation(input_word):
    out_word = ''
    punctuation = ''
    for char in input_word:
        if char.isalpha():
            out_word += char
        else:
            punctuation += char

    return out_word, punctuation


def constant_sound(char):
    return char.lower() not in VOWELS


def vowel_sound(char):
    return char.lower() in VOWELS


def find_first_vowel(word):
    first_vowel = ''
    for ch in VOWELS:
        if ch in word:
            first_vowel += ch
            break

    return first_vowel






if __name__ == '__main__':
    main()