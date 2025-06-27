from random import randint as ri
print("Please view the code for a disclaimer.")
print("Press ENTER to generate another key.")

"""DISCLAIMER: I DO NOT CONDONE PIRACY.
Windows 95 has been abandonware for a long time
and all valid OEM keys are long since generated.
The key algorithm is available online for free.
This is just a small project, not indended for spreading piracy."""

def createKey():
    day = ri(100,366)
    year = ri(95, 99)
    dev0 = ri(0,9)
    dev0b = ri(0,9)
    dev0c = ri(0,9)
    dev0d = ri(0,9)
    dev0e = ri(0,9)
    while ((dev0+dev0b+dev0c+dev0d+dev0e) % 7) != 0:
        dev0 = ri(0,9)
        dev0b = ri(0,9)
        dev0c = ri(0,9)
        dev0d = ri(0,9)
        dev0e = ri(0,9)
    random = ri(10000,99999)
    key =str(day)+str(year)+"-OEM-00"+str(dev0)+str(dev0b)+str(dev0c)+str(dev0d)+str(dev0e)+"-"+str(random)
    return key
while True:
    key = createKey()
    input(key)