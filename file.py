import random

random_number = random.randint(1,100)
remaining_attemps = 6
score = 100
attent_count = 0
 print("guess a number between 1 and 100")
 print(f"your starting score: {score}")

while(remaining_attemps>0):
  guess = input("your guess: ")
   print("enter your number between 1 and 100")
    continue
   attent_count+=1
   if(guess == random_number):
     print(f"congrat u  you correct broi! {attent_count}")
     print(f"your total score is: {score}")
      break
   elif guess<random_number:
      print("try large number")
   else:
      print("try a smaller number")
   remaining_attemps-=1
   score-=10
   if(remaining_attemps>0):
     print(f"remaining attemps: {remaining_attemps}")
     ptint(f"current score: {score}")
   else:
       print(f"your total score score: {score}")
