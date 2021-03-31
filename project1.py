import random
print("------------------------------------------")
print("-----Rock, paper, scrissors-----")
print("Ласкаво просимо до ігри")
print("Ігра складається з 3-ох раундів")
print("Перемагає той, хто набере більше очок")
print("\t[r] - камінь\n\t[s] - папір\n\t[p] - ножиці")
print("------------------------------------------")

player_score = 0
player_select = 0
comp_score = 0
comp_select = 0
try_again = 0

print("------------- Старт ІГРИ ------------")

while(try_again != 'n'):
    for i in range(3):
        print("\t ------- Раунд №" + str(i+1) +" ------- ")
        comp_select = random.choice("rps")

        while True:
            player_select = input("\tВаш вибір: ")
            if (player_select == "r") or (player_select == "s") or (player_select == "p"):
                break
            else:
                print("Помилка! Виберіть клавішу(r, s, p) ")

        print("\t Комп'ютер: " + comp_select)
        if(player_select == comp_select):
            print("\tНічия\n")
        elif(player_select == 'r' and comp_select == 's'):
            player_score = player_score + 1
            print("\tТи виграв\n")
        elif (player_select == 'r' and comp_select == 'p'):
            comp_score += 1
            print("\tВиграв комп'ютер!\n")
        elif(player_select == 'p' and comp_select == 'r'):
            player_score += 1
            print("\tТи виграв\n")
        elif(player_select == 'p' and comp_select == 's'):
            comp_score += 1
            print("\tВиграв комп'ютер!\n")
        elif(player_select == 's' and comp_select == 'p'):
            player_score += 1
            print("\tТи виграв\n")
        elif (player_select == 's' and comp_select == 'r'):
            comp_score += 1
            print("\tВиграв комп'ютер!\n")
    print("\t -------------- Результат ігри -------------- \n")


    computer_wins = comp_score
    player_wins = player_score
    print("кількість перемог комп`ютера", comp_score)
    print("кількість перемог гравця", player_score)
    print("computer score =", comp_score)
    print("player score =", player_score)

    if(player_score > comp_score):
        print("\t Вітаємо, ти переміг!")
    elif(player_score < comp_score):
        print("\t Ви програли!")
    else:
        print("\tНічия!")

    print("\n\n\n\t\t\t\t\t------------------------------------------------------")
    try_again = input("\t\t\t\t\tХочите зіграти ще раз? --- Так (y) ---   --- Ні (n) ---")
    print("\n\t\t\t\t\t------------------------------------------------------")

