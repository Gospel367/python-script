import random

sure = ''
try_again = ''
perm_list = []
permutation = ''
takeoff = 20
points = 0
listy = []
money = 0
total_money = []
save = 0

print(f"points: {points}")
print(f"Money in savings: {save}\n\n")


'''if game_choice == 1:
	print(f'Chosen option {game_choice}')
else:
	quit
	#print('Wrong input')'''

while try_again != 'n':
    sure_ans = random.randint(0, 99)
    limit = random.randint(1, 4)
    print(f"Limit: {limit}")
    print("AVAILABLE GAMES! \n 1. 2sure \n 2. Permutation \n3. Exit\n")
    game_choice = int(input('Choose a Game: '))

    if game_choice == 1:
        amount_to_play_with = int(input('Enter amount: '))
        total_money.append(amount_to_play_with)
        print(f"{total_money}\n SURE ANS: {sure_ans}\n{list(range(0,100))}")
        sure = int(input('Pick ya number: '))
        accrued_money = sum(total_money)

        if (accrued_money/limit) >= (5000) or sure == sure_ans:
            save = save + accrued_money/2
            leftover = accrued_money/2
            sure == sure_ans
            print("The right answer is: {sure_ans}\nVoila! You win\n")
            print(f"Money in savings: {save}\n\n")
            print(f'earning: {accrued_money}')
            print(f'reward: {leftover}')
            points = 0
            save = save
            total_money = []
            continue

        else:
            print('sorry, you loose\n')
            points = points + 1
            print(points)
            print(f"Money in savings: {save}\n\n")

    elif game_choice == 2:
        pointer = 0
        amount_to_play = int(input('Enter amount: '))
        total_money.append(amount_to_play)
        sum_money = sum(total_money)
        print(sum_money)

        randomlist = list(random.sample(range(0, 99), k=5))
        print(randomlist)

        First_Number = int(input("Choose First Number: "))
        Second_Number = int(input("Choose Second Number: "))
        Third_Number = int(input("Choose Third Number: "))
        perm_list.append(First_Number)
        perm_list.append(Second_Number)
        perm_list.append(Third_Number)

        print(f"Your selected numbers are: {First_Number}, {Second_Number}, {Third_Number}")
        for i in perm_list:
            if i in randomlist:
                pointer = pointer + 1
                #print(f"total point is {pointer}")
            else:
                pointer = pointer

        if pointer == 2 and sum_money >= (2 * amount_to_play):
            reward = sum_money/3
            print(f"The right numbers are: {randomlist}\nCongrats! You won {reward}")
            pointer = 0
            reward = 0
            total_money = []

        elif pointer == 3 and sum_money >= (2 * amount_to_play):
            reward = sum_money/2
            print(f"Congrats! You won {reward}")
            pointer = 0
            reward = 0
            total_money = []

        else:
            print(f"We are sorry! You just lost!")
            print(pointer)
            print(sum_money)
            #print('No point added')
            #print(f"Total points: {pointer}")

    else:
        quit

        try_again = input('Play again now? (y/n)')
