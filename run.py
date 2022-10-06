
"""
The quest is a multiple chioce game where the user make choice along the way.
"""

name = input("What's your name? ")
print("Welcome", name, "!\n")

print("This is tale about a exiting journey across the mythical lands of 'PythWorld'.")
print("You can cross path with some intresting beeings")
print("and will have to make some hard choices along your choosen path.")
print("But be aware... Your choices has consequences!\n")
print("HINT - Be sure to type in your choosen answers who is provided for you in (bracets)")
print("This in important. If you don't do this, you will lose!")

def quiz()

# Start of the quest

while True:
    print("Let's go for a walk! You never know what you might find.")

    user_input = input(
        "Ready? (yes) or (no) \n").lower()
    if user_input == "yes":
        print("Lovely! Let's Go!\n")
        break

    elif user_input == "no":
        print("Are you sure? It's really a lovely day!")
        continue
    else:
        print("No, No, No. Remember... ")
        print("Be sure to type in your choosen answers who is provided for you in (bracets)")
        print("You only get this warning. Fail this inside the quest and you lose!")
        continue

# Chioce One - Talk or sneak

print("You come to a river. There's a man guarding the only bridge.")
print(("He looks quite big and almost dangeorus from this far out."))

choiceOne = input(
     "Do you (talk) to the guard or du you try to (sneak) past? \n").lower()
    
# The Talk - Choice One

if choiceOne == "talk":

    print("")
    print("The guard seems to be in a good mood today and let you pass.")
    print("But before he let you go, he gave you a knife and told you")
    print("-'Stay away from the beach. It's dangerous!'")
    print("Well past the brigde you look to your left and see a (beach)")
    print("and to your right you see a (forest).")
    chioceOneTwo = input("Where do you go? ").lower()
        
    # The talk - Choice two 

    if chioceOneTwo == "beach":
        print("")
        print("You get to the lovely beach and see a the back of a man.  ")
        print("You say 'Hey mister, what a lovely day', the man turns around and...")
        print("IT'S DEATH HIMSELF!!! He says ")
        print("-'I've been waiting for you.")
        print("But since it's such a lovely day as you say it is,")
        print("I will give you a second chance on life. ")
        print("Just guess this five letter word.' ")

        # The talk - Choice three
        
        choiceOneThree = input("Are you ready? (Yes) or (no) \n").lower()

        if choiceOneThree == "yes":
            quiz()

        elif choiceOneThree == "no":
            print("Death says")
            print("-'Well then. I'm glad! You have accepted your faith.")
            print("From here on out you shall be known as the fearless!'") 


        

    elif chioceOneTwo == "forest":
        print("")
        print("You reach the forest and you come across som mushrooms.")
        print("You don't know if these mushrooms are poisones or not")
        print("But you are quite hungry after you little walk.")
        input("Do you (pick) them up or do you (leave) them? ").lower()
        



# Sneak - Choice one

elif choiceOne == "sneak":

    print("")
    print("Nice call... You were able to sneak past the guard.")
    print("You were able to dodge the guard and sneek over to the other side.")
    print("If you look to the right it's a nice (beach)")
    print("and to your left there is a (forest).")
    answer = input("Where do you go? ").lower()

