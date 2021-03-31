import random
print("Статистика = ", end=' ')
stats = []
attributes = 5
for i in range(attributes):
    r = random.randint(60, 80)
    stats.append(r)
    print(stats[i], end=' ')
print('\n\t[1] - strength \
        \n\t[2] - dexterity\
        \n\t[3] - intelligence\
        \n\t[4] - wisdom\
        \n\t[5] - charisma')
select = int(input('Choose:'))
select -= 1
stats[select] += random.randint(5, 15)
print(stats)
for i in range(len(stats)):
    if(select == i):
        continue
    stats[i] -= random.randint(5, 15)
for i in range(attributes):
    print(stats[i], end=' ')
fireball = [12, 15, 28, 10, 5]
lightning = [7, 13, 15, 30, 10]
silence = [23, 10, 12, 7, 18]
fire_ward = [20, 23, 14, 6, 17]
print('\n\t[f] - fireball\
        \n\t[l] - lightning\
        \n\t[s] - silence\
        \n\t[fw] - fire ward')

print('ok')
has_power_to_play = True
while(has_power_to_play):
    chosenCombo = []
    while (0 == len(chosenCombo)):
        combo = input("\nChoose combo:\t")
        if(combo == "f"):
            chosenCombo = fireball
        elif(combo == "l"):
            chosenCombo = lightning
        elif(combo == "s"):
            chosenCombo = silence
        elif(combo == "fw"):
            chosenCombo = fire_ward
        else:
            print("You must choose only f or l or s or fw")
    print("Your remainder:")
    for i in range(attributes):
        result = stats[i] - chosenCombo[i]
        stats[i] = result
        print(result)
        if(result < 0):
            print("Sorry, you don't have enough power")
            has_power_to_play = False
