import random

class PuzzleWord:
    def __init__(self):
        self.nameSource = []

    def wordFromSource(self):

        with open("names.csv", "r") as file:
            counter = 0
            for splitted in file:
                splitted = splitted.strip().split(",")
                if splitted == 'Name':
                    continue
                else:
                    self.nameSource.append(splitted[1])

                    counter += 1
                    if counter == 50:
                        break


        randNum = random.randint(1, 48)
        self.nameChoice = self.nameSource[randNum].lower()
        print(self.nameChoice, ' name')

    def letterInStar(self):
        starWord = ['*' for i in range(len(self.nameChoice))]
        print(starWord)
        point = 0
        while '*' in starWord:

            latter = input("Enter your latter : ")
            try:
                global indPos
                if latter not in starWord:
                    indPos = self.nameChoice.lower().index(latter)
                    starWord[indPos] = latter
                    print(starWord)
                    point += 1
                elif latter in starWord:
                    indPos = self.nameChoice.index(latter, indPos+1)
                    starWord[indPos] = latter
                    print(starWord)
                    point += 1
            except Exception as e:
                print('Invalid Value')
                point -= 1
        print("point : ",point)
        print('Perfect !!')



if __name__=='__main__':
    while True:
        p = PuzzleWord()
        p.wordFromSource()
        p.letterInStar()