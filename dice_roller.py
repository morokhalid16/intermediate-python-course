
import random 
def main():
  dice_rolls=2
  dice_sum=0
  for i in range(dice_rolls):
	  
   roll=random.randint(1,6)
   dice_sum+=1
   print(f'you roll a {roll} ')
  print(f' you have rolled {dice_sum} ')
if __name__== "__main__":
  main()
