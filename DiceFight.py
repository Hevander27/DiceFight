import numpy as np

def rollDice(player_array):
    if len(player_array) == 4:
        limit = 3 if player_array[0] >= 3 else player_array[0]
    else:
        limit = 2 if player_array[0] >= 2 else player_array[0]

    for i in range(limit):
        if player_array[i+1] != -1:
            player_array[i+1] = np.random.randint(1, 6)
    return player_array

def playGame(atk_array, def_array):
    atk_max = max(atk_array[1:])
    def_max = max(def_array[1:])
    unit_atk = atk_array[0]
    unit_def = def_array[0]

    if atk_max > def_max:
        def_array[0] = unit_def - 1
        if unit_def <= 2:
            def_array[unit_def - 3] = -1
    elif def_max >= atk_max:
        atk_array[0] = unit_atk - 1
        if unit_atk <= 3:
            atk_array[unit_atk - 4] = -1

def convert_to_unicode(dice_values, unit_status):
    dice_symbols = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
    unit_symbols = ['⛏', '⚔️', '⛨', '⛨']

    dice_chars = [dice_symbols[val-1] if val != -1 else ' ' for val in dice_values[1:]]
    unit_chars = [unit_symbols[i] if i < unit_status[0] else '⛌' for i in range(4)]

    return dice_chars, unit_chars

input_units = int(input('Enter number of units: '))
print('Starting number of units: ', input_units)
atk_array = [input_units, None, None, None]
def_array = [input_units, None, None]

while True:
    stay_in_game = input('Continue Attack (Y/N): ')
    if str.lower(stay_in_game) != 'y':
        print("\033[1m" + "Attacker Forfeited\nGame Ended")
        break
    else:
        atk_array = np.array(rollDice(atk_array))
        def_array = np.array(rollDice(def_array))

        dice_chars_atk, unit_chars_atk = convert_to_unicode(atk_array, def_array)
        dice_chars_def, unit_chars_def = convert_to_unicode(def_array, atk_array)

        print("-------------------------------")
        print("Attacker:")
        print(f"Dice: {' '.join(dice_chars_atk)}")
        print(f"Units: {' '.join(unit_chars_atk)}")

        print("Defender:")
        print(f"Dice: {' '.join(dice_chars_def)}")
        print(f"Units: {' '.join(unit_chars_def)}")

        playGame(atk_array, def_array)

        print("-------------------------------")
        print(f"Attacker Units: {atk_array[0]}")
        print(f"Defender Units: {def_array[0]}")
        print("*******************************")

        if atk_array[0] == 0:
            print("\033[1m" + "Defender Wins\nGame Ended")
            break
        elif def_array[0] == 0:
            print("\033[1m" + "Attacker Wins\nGame Ended")
            break
