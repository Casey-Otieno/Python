a = "Red"
b=""
c = 0
d= 3
out_of_guesses= False
while b!= a and not(out_of_guesses):
    if c < d:
        b= input("Enter guess: ").lower
        c+= 1
    else:
        out_of_guesses= True
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You won!")