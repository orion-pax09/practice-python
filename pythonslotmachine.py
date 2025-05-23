import random


def spin_row():
    symbol=["🍒"," 🍉","🍋" ,"🔔","⭐"]

    return [random.choice(symbol) for _ in range(3)]


def print_row(row):
    print("*************")
    print("|".join(row))
    print("*************")


def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet * 2
        elif row[0]=="🍉":
            return bet* 3
        elif row[0]=="🍋":
            return bet* 5
        elif row[0]=="🔔":
            return bet* 10
        elif row[0]=="⭐":
            return bet* 20
    return 0

def pmain():
    balance = 100


    print("****************************")
    print("...welcome to python slot...")
    print("symbol:🍒| 🍉| 🍋 |🔔| ⭐" )
    print("****************************")

    while balance > 0:
        print(f"the current balance is : Rs.{balance}")
        print("**************************************")
        bet=input("place your bet amount:")

        if balance <0:
            print("you are out of money.thank you for playing")

        if not bet.isdigit():
            print("please enter the valid number")
            continue


        bet=int(bet)


        if bet > balance:
            print("**************************************************************")
            print("insufficient fund.place bet less than or equal to your balance")
            print("**************************************************************")
            continue


        if balance <= 0:
            print("******************************")
            print("place a bet greater than Rs. zero")
            print("******************************")
            continue


        balance -= bet
        row = spin_row()
        print("spinning.....\n")
        print_row(row)
        print(f"You placed a bet of Rs. {bet}. The current balance is Rs. {balance}.")


        payout=get_payout(row,bet)
        if payout > 0:
            print(f"you won Rs.{payout}!")
            balance += payout
        else:
            print("sorry. you lost bet")

        play_again=input("do you want to spin again? yes(Y) or no(N):").upper().

        if play_again !="Y":
            break
     

        print(f"game over.your final balance is {balance}")
        print("******************************************")
print("********************************************")
print("You are out of money. Thank you for playing!")
print("********************************************")


if  __name__=="__main__":
    pmain()