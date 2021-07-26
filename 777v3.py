import random
counttxt = "You have ${}"
count = 10000
x = 0

game_active = True
print("you start with $10,000")

while game_active != False:
    spendtxt = input("type the amount of money you want to gamble \"ie 500\" or type q to quit ")

    str(spendtxt)

    if (spendtxt == "q"):
        print("quitting game")
        break


    spend = int(spendtxt)
    count -=spend

    x = (random.randrange(0,1000))

    if (x == 777):
        print("TRIPLE SEVENS BABY!!!")
        count = count + (spend * 100)
        print (counttxt.format(f"{count:,}"))

    elif (x >= 1 and x <= 200):
        print("one diamond")
        count = count + (spend * 1.5)
        print (counttxt.format(f"{count:,}"))

    elif (x >= 201 and x <= 300):
        print("two diamonds")
        count = count + (spend * 2)
        print (counttxt.format(f"{count:,}"))

    elif (x >= 301 and x <= 350):
        print("three diamonds")
        count = count + (spend * 3)
        print (counttxt.format(f"{count:,}"))

    elif (x >= 351 and x <= 550):
        print("nugget biscuit")
        count = count + (spend * .5)
        print (counttxt.format(f"{count:,}"))

    elif (x >= 551 and x <= 580):
        print("iron ingot")
        count = count + (spend * 5)
        print (counttxt.format(f"{count:,}"))

    elif (x >= 581 and x <= 590):
        print("emerald")
        count = count + (spend * 10)
        print (counttxt.format(f"{count:,}"))

    else:
        print("whoops you bust :(")
        print (counttxt.format(f"{count:,}"))

    if (count < 1):
        print("Oh No your broke (GAME OVER)")
