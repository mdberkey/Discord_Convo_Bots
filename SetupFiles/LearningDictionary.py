
file = open("Source_Words.txt")
string = file.read()


# creates dictionary of words in Markov Chain fashion
def learn(dict, input):
    tokens = input.split(" ")
    for i in range(0, len(tokens) - 1):
        currentWord = tokens[i]
        nextWord = tokens[i + 1]

        if currentWord not in dict:
            # adds new word to dictionary
            dict[currentWord] = {nextWord: 1}
        else:
            # word is already in dictionary
            allNextWords = dict[currentWord]

            if nextWord not in allNextWords:
                # adds new future state word to dictionary
                dict[currentWord][nextWord] = 1
            else:
                # increases frequency to state word already in dictionary
                dict[currentWord][nextWord] = dict[currentWord][nextWord] + 1
    return dict


dictionary = {}
dictionary = learn(dictionary, string)
print(dictionary)
