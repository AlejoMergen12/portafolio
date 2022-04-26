#Juego de adivinar el número.
import random

attemptsMade = 0

print(myName:= input("Hello! What's your name? : "))

number = random.randint(1, 20)
print('Well, ' + myName + ", I'm thinking of a number between 1 and 20.")

while attemptsMade < 6:
    print('Try to guess.') 

    estimate = int(input())

    attemptsMade += 1

    if estimate < number:
         print('Your estimate is too low.')

    elif estimate > number:
        print('Your estimation is very high')

    elif estimate == number: 
        break

if estimate == number:
    print('Nice job, ' + myName + ' you guessed my number ' + str(attemptsMade) + ' attempts' )

elif estimate != number:
    print('Well no. The number I was thinking of was ' + str(number))