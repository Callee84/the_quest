import random

print("Welcome to the Quest!\n")

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
name = input("What's your name? ")
print("Welcome", name, "!\n")


print("This is tale about a exiting journey across the mythical lands of")
print("'PythWorld'.")
print("You can cross path with some intresting beeings")
print("and will have to make some hard choices along your choosen path.")
print("But be aware... Your choices has consequences!\n")
print("HINT - Be sure to type in your choosen answers who is provided for you in (bracets)")
print("This in important. If you don't do this, you will lose!")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


"""
Defining quiz-game to be called nested inside the quest.
"""

# def hangman()

# defining the quiz for use under - Sneak - beach 

def quiz():
"""
This function is a quiz which is called in the in the Quest '
under - Sneak - beach
"""

    print("Welcome then, to my impossible quiz....")

    playing = input("Do you feel like you can beat me? ")

    if playing.lower() != "yes":
        quit()

    print("Okey then....")
    print("But don't come crying to me when you fail....")

    # To keep the right answers from user

    score = 0

    # Questions

    answer = input("Let's start up with an easy one...  What's 2 + 2? ")
    if answer == "4":
        print("Well done! There's some hope after all... ")
        score += 1
    else:
        print("Ha! And you thougth you could beat me?")
        print("The answer is 4.")


    answerTwo = input("What's more, 5 ants or 4 elephants? ").lower()
    if answer == "5 ants" or "5" or "ants":
        print("Correct, but that wheren't a hard question! ")
        score += 1
    else:
        print("Nope, you had a 50% chance and still got it wrong!")
        print("The answer was 5 ants.")


    answerThree = input(
        "What was to the left of the bridge you just passed?\n").lower()
    if answer == "beach":
        print("Okey, that's right. But here comes some harder questions! ")
        score += 1
    else:
        print("Nope. You're just a lot of talk huh? Not that smart?")
        print("The answer was this beach.")

    print("I hope you know you Lord of the rings...")
    answerFour = input(
        "What was the name of the hobbit who took the ring to Mordor? ").lower()
    if answer == "frodo":
        print("Hmmm, still easy questions. Don't get cocky!")
        score += 1
    else:
        print("Nope! Well, unleast you're pretty... ")
        print("The answer was Frodo.")


    answerFive = input("Last question. A simple one... Who's the best? ").lower()
    if answer == "You" or "Me":
        print("Yeah, Okey... You beat me. I guess you do got some skill. ")
        score += 1
    else:
        print("So close to beating me. But I was never worried. I'm the best!")


    print("Well, you got " + str(score) + " questions right!")


# Start of the quest

while True:
    print("Let's go for a walk! You never know what you might find.")

    user_input = input(
        "Ready? (yes) or (no) \n").lower()
    if user_input == "yes":
        print("")
        print("Lovely! Let's Go!\n")
        break

    elif user_input == "no":
        print("Are you sure? It's really a lovely day!")
        continue
    else:
        print("No, No, No. Remember... ")
        print("Be sure to type in your choosen answers")
        print("who is provided for you in (bracets)")
        print("You only get this warning. Fail this inside the quest and you lose!")
        continue

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

# Chioce One - Talk or sneak

print("")
print("You come to a river. There's a man guarding the only bridge.")
print(("He looks quite big and almost dangeorus from this far out."))

choiceOne = input(
     "Do you (talk) to the guard or du you try to (sneak) past? \n").lower()
    
# The Talk - Choice One

if choiceOne == "talk":

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("")
    print("The guard seems to be in a good mood today and let you pass.")
    print("But before he let you go, he gave you a knife and told you")
    print("-'Stay away from the beach. It's dangerous!'")
    print("Well past the brigde you look to your left and see a (beach)")
    print("and to your right you see a (forest).")
    chioceOneTwo = input("Where do you go? \n").lower()
        
    # The talk - Beach

    if chioceOneTwo == "beach":

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        print("You get to the lovely beach and see a the back of a man.  ")
        print("You say 'Hey mister, what a lovely day', the man turns around and...")
        print("IT'S DEATH HIMSELF!!! He says, ")
        print("-'I've been waiting for you.")
        print("But since it's such a lovely day as you say it is,")
        print("I will give you a second chance on life. ")
        print("Just guess this five letter word.' ")

        # The talk - Beach - quiz
        
        choiceOneThree = input("Are you ready? (Yes) or (no) \n").lower()

        if choiceOneThree == "yes":
            quiz()

        elif choiceOneThree == "no":
            print("Death says")
            print("-'Well then. I'm glad! You have accepted your faith.")
            print("From here on out you shall be known as the fearless!'") 

    # The talk - Forest

    elif chioceOneTwo == "forest":
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("")
        print("You reach the forest and you come across some mushrooms.")
        print("You don't know if these mushrooms are poisones or not")
        print("But you are quite hungry after you little walk.")
        choiceForestOne = input("Do you (pick) them up or do you (leave) them?\n").lower()

        # The talk - forest - pick

        if choiceForestOne == "pick":
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("")
            print("You picked up the mushrooms and start to walk to the edge of the forest")
            print("When you reach the edge you see a bench overlooking a fantastic view.")
            print("You decide to sit down for a while")
            print("and just when you are about eat some of your mushrooms")
            print("you see a hungry, angry wolf.")
            print("Do you (fight) him of with your knife,")
            choiceForestTwo = input("or du you try to (lure) him of with some mushrooms?\n").lower()

            # The talk - forest - pick - fight

            if choiceForestTwo == "fight":
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print("")
                print("After a long fight you manage to fight of the wolf.")
                print("But you have sustained injuries.")
                print("You try to walk but it hurts.")
                choiceForestThree = input("Do you go (home) or du you continue the (quest)?\n").lower()

                # The - forest - pick - fight - home

                if choiceForestThree == "home":
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                    print("")
                    print("You start you journey home again.")
                    print("With a lot of pain but even more will,")
                    print("you manage to walk through the forest.")
                    print("After a while you meet someone familiar -")
                    print("the guard from the bidge. He asks")
                    print("-'Do you still have my knife?")
                    choiceForestFour = input("(Yes or (no)?\n").lower()
                    
                    # The forest - pick - fight - home - yes

                    if choiceForestFour == "yes":
                        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                        print("")
                        print("The guard says 'You passed the test. As a reward you have earned")
                        print("this treasure! Follow this path back and you'll be back home in notime!")

                    # The forest - pick - fight - home - no

                    elif choiceForestFour == "no":
                        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                        print("")
                        print("")

                # The forest - pick - fight - quest

                elif choiceForestThree == "quest":
                    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                    print("")
                    print("Oh no! Your injuries is really taking it's toll")

            elif choiceForestTwo == "lure":
                print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                print("")

        elif choiceForestOne == "leave":
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("")
            print("You ignore the mushrooms and star walking.")
            print("After a while you notice that you're on a path you never been on before.")
            print("Just when you manage to find the edge of the forest you see a wolf.")
            print("The wolf is hungry and angry. He attacks you!")
            print("Do you (fight him of with your knife or")
            choiceForestWolf = input("do you (run)?")
        



# Sneak - Choice one

elif choiceOne == "sneak":

    print("")
    print("Nice call... You were able to sneak past the guard.")
    print("You were able to dodge the guard and sneek over to the other side.")
    print("If you look to the right it's a nice (beach)")
    print("and to your left there is a (forest).")
    
    # Sneak - Choice two
    
    choiceTwoTwo = input("Where do you go? ").lower()

    if choiceTwoTwo == "beach":
        print("")
        print("You get to the lovely beach and see a the back of a man.  ")
        print("You say 'Hey mister, what a lovely day', the man turns around and...")
        print("IT'S DEATH HIMSELF!!! He says, ")
        print("-'I've been waiting for you.")
        print("But since it's such a lovely day as you say it is,")
        print("I will give you a second chance on life. ")
        print("Just answer these five simple questions. ")
        print("If you get 4 answers right, I let you go free.")
        print("If not, you come with me. '")
    
        choiceTwoThree = input("Are you ready? (Yes) or (no)").lower()

        if choiceTwoThree == "yes":
            quiz()

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("")
print("So, how did you do?")
print("Did you have to answer some hard questions?")
print("Did you get the treasure?")
print("Or did you even get to be a god?")
print("Maybe you wish you've picked some other answers?")
print("Well, play again and see where the quest will take you this time...")