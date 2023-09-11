def process_word(word):
    return word == "please"

if __name__ == '__main__':
    print("What is the magic word?")
    magic_word = "thank you"
    if process_word(magic_word):
        print("yes ",magic_word, " is the magic word")
    else:
        print("no that is not the magic word")