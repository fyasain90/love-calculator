print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = (name1 + name2).lower()

T = names.count("t")
R = names.count("r")
U = names.count("u")
E = names.count("e")

L = names.count("l")
O = names.count("o")
V = names.count("v")

true = T + R + U + E
love = L + O + V + E

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coe and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
