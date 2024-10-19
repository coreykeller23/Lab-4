"""
Author:Corey Keller
File Name:lab4
Version:1.0
Creation:2.19.24
Purpose:Convert a gold amount into other types of dnd currency based on user input
"""

#import utility file
import dndCurrencyConv

#begin asking for user input
name=input("What is your name?\n")
goldAmounts=input("Hello " + name + ". Please enter how much gold you have.\n")
silverAmounts=input("Please enter how much silver you have.\n")
platinumAmounts=input("Please enter how much platinum you have.\n")
electAmounts=input("Please enter how much electrum you have\n")
copperAmounts=input("Please enter how much copper you have\n")

#convert from string to float
goldAmounts=float(goldAmounts)
silverAmounts=float(silverAmounts)
platinumAmounts=float(platinumAmounts)
electAmounts=float(electAmounts)
copperAmounts=float(copperAmounts)

#convert your Amounts variables to a gold amount so the functions recognize the user input as a gold value
silverAmounts=dndCurrencyConv.silverTogold(silverAmounts)
platinumAmounts=dndCurrencyConv.platTogold(platinumAmounts)
electAmounts=dndCurrencyConv.electTogold(electAmounts)
copperAmounts=dndCurrencyConv.copperTogold(copperAmounts)

#combine all amounts into gold currency for ease of conversion
userTotal=dndCurrencyConv.allGold(goldAmounts,silverAmounts,platinumAmounts,electAmounts,copperAmounts)

#ask what coin type to convert to
userConvert=input("What would you like to convert your coins to?\n").lower()
if userConvert=="gold":
    print("You have " + str(dndCurrencyConv.goldTogold(userTotal)) + " gold.")
elif userConvert=="silver":
    print("You have " + str(dndCurrencyConv.goldToSilver(userTotal)) + " silver.")
elif userConvert=="platinum":
    print("You have " + str(dndCurrencyConv.goldToPlat(userTotal)) + " platinum.")
elif userConvert=="electrum":
    print("You have " + str(dndCurrencyConv.goldToElect(userTotal)) + " electrum.")
elif userConvert=="copper":
    print("You have " + str(dndCurrencyConv.goldToCopper(userTotal)) + " copper.")
else:
    print("Invalid coin type, execution aborted")