import ast
import random

# reads emoticons.txt
emoticonsFile = open("emoticons.txt", "r")
contentsB = emoticonsFile.read()
emoticons = ast.literal_eval(contentsB)
emoticonsFile.close()


# returns a random emoji from the string
def getRandomEmoji():
    self = 0
    randNum = random.randint(0, 279)        # number of emojis in emoticons.txt
    for i in range(0, len(emoticons)):
        if randNum == i:
            return emoticons[i]
