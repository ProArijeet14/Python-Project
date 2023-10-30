playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit() 
print("Okay let's play :)")

answer = input("what does CPU stands for:- ")
if answer == "Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("what does GPU stands for:- ")
if answer == "Graphical Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("what does ALU stands for:- ")
if answer == "Arthmetic Logic Unit":
    print("Correct!")
else:
    print("Incorrect!")