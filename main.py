from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

def highest_bidder(bidders):
  
  max_value = 0
  max_key = None
  
  for key, value in bidders.items():
    if value > max_value:
      max_value = value
      max_key = key

  print(f"The highest bidder is {max_key} with a value of ${max_value}")

bidders = {}
more_bidders = True

while more_bidders == True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: "))

  bidders.update({name: bid})

  ask_more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
  if ask_more_bidders == "no":
    more_bidders = False
  else:
    clear()

clear()

#print(bidders)

highest_bidder(bidders)
    
    


