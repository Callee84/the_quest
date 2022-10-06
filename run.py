
"""
The quest is a multiple chioce game where the user make choice along the way.
"""

name = input("What's your name? ")
print("Welcome", name, "!\n")

print("This is tale about a exiting journey across the mythical lands of PythWorld.")
print("You can cross path with some intresting beeings and will have to make some hard choices along your choosen path.")
print("But be aware... Your choices has consequences!\n")
print("HINT - Be sure to type in your choosen answere who is provided for you in (bracets)")

while True:
    user_input = input(
        "Let's go for a walk! You never know what you might find. Ready? ").lower()
    if user_input == "yes":
        print("Lovely! Let's Go!")
        break

    elif user_input == "no":
        print("Are you sure? It's really a lovely day!")
        continue
    else:
        print("Sorry, I didn't catch that: Could you type again?")
        continue

choiceOne = input(
    "You come to a river. There's a man guarding the only bridge. Do you (talk) to the guard or du you try to (sneak) past? ").lower()
if choiceOne == "talk":
    print("The guard seems to be in a good mood today and let you pass. But before he let you go, he gave you a knife and told you 'Stay away from the beach. It's dangerous!")

elif choiceOne == "sneak":
    print("Nice call... You were able to sneak past the guard.")
    answer = input("You were able to dodge the guard and sneek over to the other side. \nIf you look to the right it's a nice (beach) and to your left there is a (forest). \nWhere do you go? ")
