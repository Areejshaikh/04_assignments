import random
rolling_dice = 6 


def main():
    rolling_dice1 = random.randint(1 ,rolling_dice)
    rolling_dice2 = random.randint(1 ,rolling_dice)
    
    
    dice_total = rolling_dice1 + rolling_dice2
    
    print(f"Dice have {rolling_dice} sides each.")
    print(f"first die: {rolling_dice1}")
    print(f"Second die: {rolling_dice2}")

    print(f"Total of two dice: {dice_total}")
main()