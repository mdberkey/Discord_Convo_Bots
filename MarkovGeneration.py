import random
import ast

# reads dictionary.txt
dictionaryFile = open("dictionary.txt", "r")
contents = dictionaryFile.read()
dictionary = ast.literal_eval(contents)
dictionaryFile.close()


# generates a unique string using the markov chain values
class generation:
    def main(self):
        lastWord = '3u9fh27d31r'            # random string unlikely to appear in dictionary
        finalAnswer = ''
        counter = 0
        randNumA = random.randint(1, 4)     # set to about 1-4 sentences to output

        for i in range(1, 10000):
            newWord = getNextWord(lastWord, dictionary, self)
            if newWord.endswith('.') or newWord.endswith('!') or newWord.endswith('?'):
                counter += 1
            finalAnswer = finalAnswer + " " + newWord
            lastWord = newWord
            if counter >= randNumA:
                break
        return finalAnswer


def getNextWord(lastWord, dict, self):
    if lastWord not in dict:
        # selects a new starting word for a new sentence
        newWord = randomSelect(dict)
        return newWord
    else:
        # selects next word from the dictionary's list
        newWord = weightedSelect(lastWord, dict, self)
        return newWord


# returns a random word from the dictionary
def randomSelect(dict):
    randInt = random.randint(0, len(dict) - 1)
    newWord = list(dict.keys())[randInt]
    return newWord


# returns the next random word in the markov chain using weighted values
def weightedSelect(lastWord, dict, self):
    weightedList = []

    for word in dict[lastWord]:
        weightInt = dict[lastWord][word]

        # adds more weight to words that appear in self
        if word in self:
            weightInt += (weightInt * 10)

        for i in range(0, weightInt):
            weightedList.append(word)
    randInt = random.randint(0, len(weightedList) - 1)
    return weightedList[randInt]
