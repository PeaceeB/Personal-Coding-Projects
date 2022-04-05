print("General Knowledge Test")

playing = input("Hi! Welcome to the General Knowledge Test. Do you want to play?  ")
if playing.lower() != "yes":
    print("Aww, that sucks. Hope to see you again soon")
    quit()
print("Great! Let's begin :)")
score = 0
print("Round 1: Category - Celebrities")

answer1 = input("Which one of these Kardashian sisters is the oldest?\nA: Kourtney\nB: Kim\nC: Khloe\nYour Answer: ")
if answer1.upper() == "A":
    print("CORRECT")
    score += 1
elif answer1.upper() != "A":
    print("INCORRECT!")

answer1 = input("In which decade was Madonna born?\nA: 50s\nB: 60s\nC: 70s\nYour Answer: ")
if answer1.upper() == "A":
    print("CORRECT")
    score += 1
elif answer1.upper() != "A":
    print("INCORRECT!")

answer1 = input("What is Polo G's real first name?\nA: Ralph\nB: Taurus\nC: Tyrone\nYour Answer: ")
if answer1.upper() == "B":
    print("CORRECT")
    score += 1
elif answer1.upper() != "B":
    print("INCORRECT!")

answer1 = input("What album did Rod Wave release in March 2021?\nA: Pray 4 Love\nB: P.T.S.D\nC: SoulFly\nYour Answer: ")
if answer1.upper() == "C":
    print("CORRECT")
    score += 1
elif answer1.upper() != "C":
    print("INCORRECT!")

answer1 = input("What is Drake's sons name?\nA: Aubrey\nB: Adonis\nC: Unknown\nYour Answer: ")
if answer1.upper() == "B":
    print("CORRECT")
    score += 1
elif answer1.upper() != "B":
    print("INCORRECT!")

answer1 = input("In what year did Prince William marry Kate Middleton?\nA: 2010\nB: 2011\nC: 2012\nYour Answer: ")
if answer1.upper() == "B":
    print("CORRECT")
    score += 1
elif answer1.upper() != "B":
    print("INCORRECT!")

print("Your got", str(score), "out of 5 questions correct in this round")
playing2 = input("Do you want to continue to the next round?: ")
if playing2.lower() =="yes":
    print("Great! Let's gooo!")
elif playing2.lower() != "yes":
    print("Thanks for playing! Hope to see you again soon")

print("\nRound 2: Category - Geography")
answer1 = input("If you were visting the Taj Mahal, what country would you have to travel to?\nA: India\nB: China\nC: Bangladesh\nYour Answer: ")
if answer1.upper() == "A":
    print("CORRECT")
    score += 1
elif answer1.upper() != "A":
    print("INCORRECT!")

answer1 = input("What is the capital of Spain?\nA: Barcelona\nB: Madrid\nC: Milan\nYour Answer: ")
if answer1.upper() == "A":
    print("CORRECT")
    score += 1
elif answer1.upper() != "A":
    print("INCORRECT!")

answer1 = input("What colour in the dot in the middle of the Japanese flag\nA: Red\nB: Blue\nC: There's no dot\nYour Answer: ")
if answer1.upper() == "A":
    print("CORRECT")
    score += 1
elif answer1.upper() != "A":
    print("INCORRECT!")

answer1 = input("How many countries are in the continent Africa?\nA: 50\nB: 64\nC: 54\nYour Answer: ")
if answer1.upper() == "C":
    print("CORRECT")
    score += 1
elif answer1.upper() != "C":
    print("INCORRECT!")

answer1 = input("What river is the longest in the world?\nA: Nile River\nB: Amazon River\nC: Yangtze River\nYour Answer: ")
if answer1.upper() == "A":
    print("CORRECT")
    score += 1
elif answer1.upper() != "A":
    print("INCORRECT!")
answer1 = input("What is the largest continent in the world?\nA: Africa\nB: North America\nC: Asia\nYour Answer: ")
if answer1.upper() == "C":
    print("CORRECT")
    score += 1
elif answer1.upper() != "C":
    print("INCORRECT!")

print("You scored", str(score), "out of 5")
print("Game Finished, Thanks for playing!!!")