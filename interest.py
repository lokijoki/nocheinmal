import random
from googletrans import Translator
translator = Translator()
lowerNumber = int(input())
upperNumber = int(input())
trialNumber = int(input())
trialStart = 0
while trialStart <= trialNumber:
    nomerRandom = random.randint(lowerNumber, upperNumber)
    print(translator.translate(nomerRandom, dest= 'de'))
    answerNumber = int(input())
    if answerNumber == nomerRandom:
        print("Ok")
    else:
        print("No, the answer was", nomerRandom)
    trialStart = trialStart + 1

