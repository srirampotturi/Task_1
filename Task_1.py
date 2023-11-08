import random;
class RPSGame:
    def user(self):
        l=["rock","paper","scissor"]
        s=input("Enter Your Choice [rock,paper,scissor] : ")
        while s not in l:
            print("Invalid input!")
            break
        return s
    def computer(self):
        l=["rock","paper","scissor"]
        c=random.choice(l)
        return c
    def winning(self,s,c):
        if s==c:
            return "It is Tie!"
        elif (s=="rock" and c=="scissor") or (s=="paper" and c=="rock") or (s=="scissor" and c=="paper"):
            return "You WinS!"
        else:
            return "Computer Wins!"

game=RPSGame()      
while True:
    user=game.user()
    computer=game.computer()
    print("User Choice is ",user)
    print("Computer Choice is ",computer)
    result=game.winning(user,computer)
    print(result)
    ch=input("Do you want play again?(Yes/No) : ")
    p=ch.lower()
    if p=="yes" or p=="y":
        continue
    else:
        print("Thanks for playing")
        break