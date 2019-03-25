numAlphons = 5000000
numVelons = 9000000
years = 0

while True:
    years += 1

    numAlphons *= 1.06

    if (years % 4 == 0):
        numVelons = numVelons * 1.05 - 500000
    else:
        numVelons *= 1.02

    if (numAlphons > numVelons):
        break

print("Za ", years, " godina ce Alphonci prestic Velonce.")
print("Broj Alphonaca ce biti  ", numAlphons)
print("Broj Velonaca ce biti  ", numVelons)








