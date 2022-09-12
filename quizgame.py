print("Welcome to the quiz!")

playing = input("Do you want to play : \n")

text = "SorrY WronG INput"
if text == "sorry wrong input":
    print(text.lower())
else:
    print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) \n")
score = 0

answer = input("What does CPU stands for? \n")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? \n")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? \n")
if answer.lower() == "Random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for? \n")
if answer.lower() == "power supply unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")
