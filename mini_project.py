"""The initial investigation, test program."""

import random
random.seed()

vertices = ["0", "1", "2", "3", "4"]
recordings = []

for i in range(10):
    a = 0
    b = 1 #just for the step numbers in the print
    annie_the_ant = vertices[a]
    print()
    print("Step 0: Annie the ant is on", annie_the_ant)
    
    for i in range(7):
        if random.randrange(1, 11) > 5: #There's a 50% chance of the integer chosen being greater than 5
            #Ant moves anticlockwise
            a = a + 1
            if a == 5:
                a = 0
            annie_the_ant = vertices[a] 
        else:
            #Ant moves clockwise
            a = a - 1
            if a == -6:
                a = -1
            annie_the_ant = vertices[a]
            
        print("Step ", b, ": Annie the ant is on ", annie_the_ant, sep="")
        b = b + 1  
        
    recordings.append(annie_the_ant)
    print(recordings)
    
print("Annie lands on vertex 0 ", recordings.count("0") / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 1 ", recordings.count("1") / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 2 ", recordings.count("2") / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 3 ", recordings.count("3") / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 4 ", recordings.count("4") / 10 * 100, "% of the time.", end="")




print("\n\n\n\n")
"""The initial investigation."""

import random
random.seed()

vertices = [0, 1, 2, 3, 4]
recordings = []

for i in range(1000000):
    a = 0
    annie_the_ant = vertices[a]
    
    for i in range(7):        
        if random.randrange(1, 11) > 5: #There's a 50% chance of the integer chosen being greater than 5
            #Ant moves anticlockwise
            a = a + 1
            if a == 5:
                a = 0
            annie_the_ant = vertices[a]            
        else:
            #Ant moves clockwise
            a = a - 1
            if a == -6:
                a = -1
            annie_the_ant = vertices[a]
            
    recordings.append(annie_the_ant)
    
print("Annie lands on vertex 0 ", recordings.count(0) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 1 ", recordings.count(1) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 2 ", recordings.count(2) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 3 ", recordings.count(3) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 4 ", recordings.count(4) / 1000000 * 100, "% of the time.", end="")




print("\n\n\n\n")
"""Variation on the number of steps."""

import random
random.seed()

vertices = [0, 1, 2, 3, 4]
recordings = []

for i in range(1000000):
    a = 0
    annie_the_ant = vertices[a]
    
    for i in range(60):
        if random.randrange(1, 11) > 5: #There's a 50% chance of the integer chosen being greater than 5
            #Ant moves anticlockwise
            a = a + 1
            if a == 5:
                a = 0
            annie_the_ant = vertices[a]
        else:
            #Ant moves clockwise
            a = a - 1
            if a == -6:
                a = -1
            annie_the_ant = vertices[a]
            
    recordings.append(annie_the_ant)
    
print("Annie lands on vertex 0 ", recordings.count(0) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 1 ", recordings.count(1) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 2 ", recordings.count(2) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 3 ", recordings.count(3) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 4 ", recordings.count(4) / 1000000 * 100, "% of the time.", end="")




print("\n\n\n\n")
"""Variation on the number of vertices."""

import random
random.seed()

vertices = [0, 1, 2, 3, 4, 5, 6]
recordings = []

for i in range(1000000):
    a = 0
    annie_the_ant = vertices[a]
    
    for i in range(7):
        if random.randrange(1, 11) > 5: #There's a 50% chance of the integer chosen being greater than 5
            #Ant moves anticlockwise
            a = a + 1
            if a == 7:
                a = 0
            annie_the_ant = vertices[a]
        else:
            #Ant moves clockwise
            a = a - 1
            if a == -8:
                a = -1
            annie_the_ant = vertices[a]
            
    recordings.append(annie_the_ant)
    
print("Annie lands on vertex 0 ", recordings.count(0) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 1 ", recordings.count(1) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 2 ", recordings.count(2) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 3 ", recordings.count(3) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 4 ", recordings.count(4) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 5 ", recordings.count(5) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 6 ", recordings.count(6) / 1000000 * 100, "% of the time.", end="")




print("\n\n\n\n")
"""Variation moving Annie onto a cube, test program."""

import random
random.seed()

vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
recordings = []

for i in range(10):
    a = 0
    b = 1
    annie_the_ant = vertices[a]
    print("Step 0: Annie the ant is on", annie_the_ant)
    
    for i in range(7):
        x = random.randrange(0,10)
        if x > 6:
            #ant moves anticlockwise on the current square
            a = a + 1
            if a == 4:
                a = 0
            if a == 9:
                a = 5
            annie_the_ant = vertices[a]
        if x < 4:
            #Ant moves clockwise on the current square
            a = a - 1
            if a == -1:
                a = 3
            if a == 4:
                a = 8
            annie_the_ant = vertices[a]
        if 3 < x < 7:
            #Ant moves to the other square
            a = a + 5
            if a == 10:
                a = 0
            if a == 11:
                a = 1
            if a == 12:
                a = 2
            if a == 13:
                a = 3 
            annie_the_ant = vertices[a]
            
        print("Step ", b, ": Annie the ant is on ", annie_the_ant, end="")
        b = b + 1
        print()
        
    recordings.append(annie_the_ant)
    print(recordings)
    
print("Annie lands on vertex 0 ", recordings.count(0) / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 1 ", recordings.count(1) / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 2 ", recordings.count(2) / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 3 ", recordings.count(3) / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 5 ", recordings.count(5) / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 6 ", recordings.count(6) / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 7 ", recordings.count(7) / 10 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 8 ", recordings.count(8) / 10 * 100, "% of the time.", end="")




print("\n\n\n\n")
"""Variation moving Annie onto a cube."""

import random
random.seed()

vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
recordings = []

for i in range(1000000):
    a = 0
    annie_the_ant = vertices[a]
    
    for i in range(7):
        x = random.randrange(0,10)
        if x > 6:
            #ant moves anticlockwise on the current square
            a = a + 1
            if a == 4:
                a = 0
            if a == 9:
                a = 5
            annie_the_ant = vertices[a]
        if x < 4:
            #Ant moves clockwise on the current square
            a = a - 1
            if a == -1:
                a = 3
            if a == 4:
                a = 8
            annie_the_ant = vertices[a]
        if 3 < x < 7:
            #Ant moves to the other square
            a = a + 5
            if a == 10:
                a = 0
            if a == 11:
                a = 1
            if a == 12:
                a = 2
            if a == 13:
                a = 3 
            annie_the_ant = vertices[a]
            
    recordings.append(annie_the_ant)
    
print("Annie lands on vertex 0 ", recordings.count(0) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 1 ", recordings.count(1) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 2 ", recordings.count(2) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 3 ", recordings.count(3) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 5 ", recordings.count(5) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 6 ", recordings.count(6) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 7 ", recordings.count(7) / 1000000 * 100, "% of the time.", end="")
print()
print("Annie lands on vertex 8 ", recordings.count(8) / 1000000 * 100, "% of the time.", end="")




