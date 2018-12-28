
import  random
import  copy



class puzzleProblem:

    def __init__(self,initialState = None):
        self.puzzle = []
        if (initialState != None):
            self.setpuzzle(initialState)
        else:
            temppuzzle = []
            for i in range(9):
                temppuzzle.append(i)
            random.shuffle(temppuzzle)
            self.puzzle=[[temppuzzle[(i*3) + j] for j in range(3)] for i in range(3)]
    def setpuzzle(self,puzzlet):
        self.puzzle=copy.deepcopy(puzzlet)

    def getpuzzle(self):
        return self.puzzle

    def getsuccessors(self):
        successors = []
        for i in range(3):
            for j in range(3):
                sucrow = i
                succol = j
                if(self.puzzle[sucrow][succol] == 0):
                    if(succol >0):
                        puzzlet = copy.deepcopy(self.getpuzzle())
                        puzzlet[sucrow][succol] = puzzlet[sucrow][succol-1]
                        puzzlet[sucrow][succol-1] = 0
                        successors.append(puzzlet)
                    if(succol <2):
                        puzzlet = copy.deepcopy(self.getpuzzle())
                        puzzlet[sucrow][succol] = puzzlet[sucrow][succol+1]
                        puzzlet[sucrow][succol+1] = 0
                        successors.append(puzzlet)
                    if(sucrow <2):
                        puzzlet = copy.deepcopy(self.getpuzzle())
                        puzzlet[sucrow][succol] = puzzlet[sucrow+1][succol]
                        puzzlet[sucrow+1][succol] = 0
                        successors.append(puzzlet)
                    if(sucrow >0):
                        puzzlet = copy.deepcopy(self.getpuzzle())
                        puzzlet[sucrow][succol] = puzzlet[sucrow-1][succol]
                        puzzlet[sucrow-1][succol] = 0
                        successors.append(puzzlet)
        return successors

def objectivefunc(puzzlev):
    func = 0
    for i in range(3):
        for j in range(3):
            currow = i
            curcol = j
            if(puzzlev[currow][curcol] != 0):
                number = puzzlev[currow][curcol]
                correctrow = int(number/3)
                correctcol = number % 3
                func += (abs(correctrow - currow) + abs(correctcol - curcol))
    return func

def hillclimbing(puzzlev = None):
    currentpuzzle = puzzleProblem(puzzlev)
    succesors = currentpuzzle.getsuccessors()
    bestsuccesors = currentpuzzle.getpuzzle()
    lowescost = objectivefunc(bestsuccesors)
    while(True):
        while(succesors.__len__() > 0):
            temppuzzle = succesors.pop()
            tempcost = objectivefunc(temppuzzle)
            if(lowescost > tempcost):
                bestsuccesors = temppuzzle
                lowescost = tempcost
        if (bestsuccesors == currentpuzzle.getpuzzle()):
            break
        currentpuzzle.setpuzzle(bestsuccesors)
    return currentpuzzle.getpuzzle()


testpuzzle=puzzleProblem()
print(objectivefunc(testpuzzle.getpuzzle()))
testpuzzle.setpuzzle(hillclimbing(testpuzzle.getpuzzle()))
print(testpuzzle.getpuzzle())
print(objectivefunc(testpuzzle.getpuzzle()))


