#---------------------------------
#Modules Formative 1
#Sydney Loerzel
#April 1, 2020
#Main code
#---------------------------------

#-------------Lists---------------

#-----------Functions-------------

import time
import sm
import member


def start():
    print("Before we get started, What is your name?")
    x = input("Please type your name ^.^")
    sm.intro(x)
    print("They are under the label", sm.entertainment)
        
def person():
    print("Lets look at a member and learn more about them!")
    print("We will look at one of the four most popular!")
    time.sleep(5)
    member.member()

def outro():
    print("Thank you for reading my TED Talk haha")
    print("Now you are informed about another group not BTS")
    print("For one last thing. Lets look at Have a nice day in korean ^.^")
    print(member.goodbye)

def main():
    start()
    person()
    outro()
    
main()