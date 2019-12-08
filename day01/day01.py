
def addFuel(mass):
    return int(int(mass) / 3) - 2

absFuel = 0

with open("day01/mass.txt") as f:
    for line in f:
        newFuel = addFuel(int(line))
        absFuel += newFuel
        while addFuel(newFuel) > 0:
            newFuel = addFuel(newFuel)
            absFuel += newFuel

print(absFuel)

#mass = input("Masse eingeben:")

