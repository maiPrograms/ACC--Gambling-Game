### Leave this code! ###
import random
seed = input('Enter seed: ')
random.seed(seed)
### Do not make changes above this line! ###
amount_money = 10 # Starting amount of money
amount_max_money = 10 # This is my global value to keep track of total for later
amount_rolled = 0# Keeps track of how many times is being rolled



while amount_money >= 1: # while loop runs only when the global value amount_money is >=1
                          #Will break when the condition is >= 1 
  total_di = (random.randint(1,6) + random.randint(1,6)) # adding our two dice rolls
  
  amount_rolled += 1 #each roll is increasing the increment by 1
  if total_di == 7:
    amount_money += 4
  else: 
    amount_money -= 1



  if amount_money > amount_max_money: #Our global value amount_max_money changes to our
     amount_max_money = amount_money #global value amount_money when its greater than amount max_money


print (f"You rolled {amount_rolled} times before going broke.") # Lines 26 and 27 are my formatted strings 
print (f"The most you ever had was {amount_max_money} dollars.") # These have broken out of the loop
