def initializeInput():
    input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,
           23,1,23,13,27,2,6,27,31,1,5,31,35,2,10,35,39,1,6,
           39,43,1,13,43,47,2,47,6,51,1,51,5,55,1,55,6,59,2,
           59,10,63,1,63,6,67,2,67,10,71,1,71,9,75,2,75,10,79,
           1,79,5,83,2,10,83,87,1,87,6,91,2,9,91,95,1,95,5,99,
           1,5,99,103,1,103,10,107,1,9,107,111,1,6,111,115,1,
           115,5,119,1,10,119,123,2,6,123,127,2,127,6,131,1,
           131,2,135,1,10,135,0,99,2,0,14,0]

    return input
            #intcode[1] = 12
            #intcode[2] = 2

def runIntcomputer(noun:int, verb:int):

    intcode = initializeInput()
    intcode[1] = noun
    intcode[2] = verb

    for element in range(0,len(intcode),4):
        if intcode[element] == 1:
            intcode[intcode[element+3]] = intcode[intcode[element+1]] + intcode[intcode[element+2]]
        elif intcode[element] == 2:
            intcode[intcode[element+3]] = intcode[intcode[element+1]] * intcode[intcode[element+2]]
        elif intcode[element] == 99:
            break
        else:
            continue

        if intcode[0] == 19690720:
            print(100*noun+verb)


for element1 in range(0,100):
    for element2  in range(0,100):
        runIntcomputer(element1, element2)