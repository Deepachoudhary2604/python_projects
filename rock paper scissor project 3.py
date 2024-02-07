import random
print("what do you chhose? type 0 for rock, 1 for paper and 2 for scissor")
rock='''   ________
---------'_________)
            (___________)
            (__________)
            (_________)
---------(________)'''
paper=  '''________
---------'_______________)
                 ______________)
            _________________)
            (_______________)
---------(_____________)'''
scissor='''________
---------'__________)______
                 ______________)
            _________________)
            (_________)
---------(________)'''
choice=int(input())
if choice==0:
    print(rock)
elif choice==1:
    print(paper)
elif choice==2:
    print(scissor)
else:
    print("enter valid choice")
print("computer choose")
computer_choice=random.randint(0,2)
if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(paper)
elif computer_choice==2:
    print(scissor)
if choice==computer_choice:
    print("its a tie")
if choice==0:
    if computer_choice==1:
        print("you lose")
    elif computer_choice==2:
        print("you win")
if choice==1:
     if computer_choice==0:
        print("you win")
     elif computer_choice==2:
        print("you lose")
if choice==2:
    if computer_choice==0:
        print("you lose")
    elif computer_choice==1:
        print("uou win")











