#love calculator

#counter
POINTS = 0
print ("Welcome to the love calculator")
Love1 = input("Please enter the first persons name\n")
Love2 = input("Please enter the second persons name\n")

L1 = (len(Love1))
L2 = (len(Love2))

S1 = (Love1[:1])
S2 = (Love2[:1])

#letters comparison
if L1 == L2:
    POINTS = POINTS + 20

if S1 == "a" or "e" or "i" or "o" or "u":
    POINTS = POINTS + 5
else:
    POINTS = POINTS + 2.5
if S2 == "a" or "e" or "i" or "o" or "u":
    POINTS = POINTS + 5
else:
    POINTS = POINTS + 2.5

print (POINTS)
