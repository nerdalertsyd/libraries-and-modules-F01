#---------------------------------
#Modules Formative 1
#Sydney Loerzel
#March 10, 2020
#Module 2 (member)
#---------------------------------

#-------------Lists---------------

superm = {'Taeyong':'NCT', 'Mark':'NCT', 'Kai':'EXO', 'Baekhyun':'EXO',}

#-----------Functions-------------

def member():
    print("Choose a member")
    choice = input("choose a number from 0 to 3")
    if choice == '0':
        print("You chose Taeyong")
        print("He is a member of", superm['Taeyong'])
        print("His full name is Lee Tae-yong")
        print("Taeyong is the leader of NCT 127")
        print("His specialty is rapping but he is a main dancer and sub-vocalist")
        print("TY is the visual and center of the group.")
        print("TY looks mean but he's a big sweetheart")
        print("He has Mysophobia")
    elif choice == '1':
        print("You choose Mark")
        print("He is a member of", superm['Mark'])
        print("His full English name is Mark Lee")
        print("His Korean name is Lee Min-hyung")
        print("Mark is a rapper, and songwriter")
        print("He is also one of the main dancers and a sub-vocalist")
        print("Based out of South Korea, Mark is Canadian born")
        print("He was roasted once by Gorden Ramsey over a fried egg")
    elif choice == '2':
        print("You choose Kai")
        print("He is a member of", superm['Kai'])
        print("His full name is Kim Jong-in")
        print("He is a main dancer, vocalist, and rapper")
        print("Kai is also the face/center of the group")
        print("Kai is a people person friends with many other group members")
    elif choice == '3':
        print("You choose Baekhyun")
        print("He is a member of", superm['Baekhyun'])
        print("His full name is Byun Baek-hyun")
        print("Baekhyun is the leader of Super M")
        print("He is one of the main vocalists")
        print("Fans and himself call him Bacon")

goodbye = '잘 보내세요(jal bonaeseyo)'