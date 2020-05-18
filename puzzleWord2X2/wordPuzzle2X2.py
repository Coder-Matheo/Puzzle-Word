import random
import numpy as np


class PuzzleWord:
    def __init__(self):
        self.nameSuorce = []
        self.notEqLetter = []

    def nameFromSource(self):

        with open("names.csv", "r") as file:
            counter = 0
            for splitted in file:
                splitted = splitted.strip().split(",")
                if splitted == 'Name':
                    continue
                else:
                    self.nameSuorce.append(splitted[1])

                    counter += 1
                    if counter == 50:
                        break


        firstListName = []
        secondListName = []
        for idFirst in range(40):
            randNumFir = random.randint(1, 48)
            randNumSec = random.randint(1, 48)

            nameChoiceFir = self.nameSuorce[randNumFir]
            nameChoiceSec = self.nameSuorce[randNumSec]
            firstListName.insert(0, nameChoiceFir)
            secondListName.insert(0, nameChoiceSec)




        for idFirst, self.firstWord in enumerate(firstListName):
            for idSecond, self.secondWord in enumerate(secondListName):
                pass

        for val in firstListName[idFirst]:
            for val2 in secondListName[idSecond]:

                self.notEqLetter.insert(0, val.upper())
                self.notEqLetter.insert(0, val2.upper())
        #print('first word: ',self.firstWord.upper())
        #print('second word: ',self.secondWord.upper())
        #print('length: ',len(np.unique(self.notEqLetter)))
        print(np.unique(self.notEqLetter))


    def putLetterInStar(self):
        point = 0
        if len(np.unique(self.notEqLetter)) <= 10:
            starFirsWord = ['*' for i in range(len(self.firstWord))]
            starSecondWord = ['*' for i in range(len(self.secondWord))]
            print(starFirsWord)
            while '*' in starFirsWord:
                letter = input('Enter your letter: ').upper()
                try:
                    global indPos1
                    if letter not in starFirsWord and len(letter) == 1:
                        indPos1 = self.firstWord.upper().index(letter)
                        starFirsWord[indPos1] = letter
                        print(starFirsWord)
                        point += 1
                    elif letter in starFirsWord and len(letter) == 1:
                        indPos1 = self.firstWord.upper().index(letter,indPos1+1)
                        starFirsWord[indPos1] = letter
                        print(starFirsWord)
                        point += 1
                    if '*' not in starFirsWord:
                        print('your point: ',point)
                        print('perfect !!')
                        print()

                except:
                    point -= 1
                    print('Invalid input')
            else:
                print(starSecondWord)
                while '*' in starSecondWord:
                    letter = input('Enter your letter: ').upper()
                    try:
                        global indPos2
                        if letter not in starSecondWord and len(letter) == 1:
                            indPos2 = self.secondWord.upper().index(letter)
                            starSecondWord[indPos2] = letter
                            print(starSecondWord)
                            point += 1
                        elif letter in starSecondWord and len(letter) == 1:
                            indPos2 = self.secondWord.upper().index(letter, indPos2 + 1)
                            starSecondWord[indPos2] = letter
                            print(starSecondWord)
                            point += 1
                        if '*' not in starSecondWord:
                            print('your point: ',point)
                            print("let's go")
                            print()

                    except:
                        print('Invalid input')

if __name__=='__main__':
    while True:
        p = PuzzleWord()
        p.nameFromSource()
        p.putLetterInStar()