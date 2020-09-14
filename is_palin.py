def is_palin(word):
    reversed_word = word[::-1]
    if word == reversed_word: # if word == word[::-1]
        return True
    return False

print(is_palin("sajid"))
print(is_palin("madam"))