print("Hey! Let's play Madlibs!")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

print("Hello", name, "! You are", age, "years old." )

if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with ", health, "health.")
        print("Let's play!")
        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice move! You move forward and reach a lake... Do you swim across or go around (across/around)? ")
            if ans == "around":
                print("Good job! You won the game.")
            else:
                print("Game Over! You were eaten by an alligator.")
        else: 
            print("Oops! You fell down and lost.")
    else:
        print("See you!")
else: 
    print("You aren't old enough to play. Bye!")
   