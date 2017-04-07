#Question:
#Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

def Number_Freq(words):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet += alphabet.upper()
    alphabet += "0123456789"
    alphabet += " "

    print(alphabet)

    for character in words:
        if character not in alphabet:
            words = words.replace(character,"")

    words = words.split()

    freqs = {}

    for word in words:
        if freqs.get(word):
            freqs[word] = freqs[word] + 1
        else:
            freqs[word] = 1

    for word in sorted(freqs):
        print(word,":",freqs[word])

Number_Freq("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")
