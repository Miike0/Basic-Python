def palindrome(word):
    word = word.replace(' ','').lower()
    if word == word[::-1]:
        return True
    else:
        return False



def main():
    word = input("Write a word: ")
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome")


if __name__ == '__main__':
    main()