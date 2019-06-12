# The function separates adjacent meaningful words with the help of a dictionary.
def ReconstitutedSentences(s, d):
    s = s.lower()
    sentence = ""
    tempJ = 0
    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            if s[i:j] in d and tempJ < j:
                tempJ = j
        if s[i:tempJ] in d:
            sentence += s[i:tempJ] + " "

    return sentence


def main():
    s = "itwastethebestoftimes"
    d = {"the", "there", "of", "car", "waste", "fish", "cat", "dog", "is", "a", "and", "it", "was", "best", "times"}
    print("The string: ", s)
    print("Corrected string: ", ReconstitutedSentences(s, d))


if __name__ == '__main__':
    main()