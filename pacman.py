from colorama import *
import os
import msvcrt
import time
import random
import pickle

mapList = []
fullMap = []
consoleWidth = 80
consoleHeight = 24
enemies = []
eaten = []
wallN = 0
enemyN = 0
pac_pos = [1, 1]
score = 0
fullScore = 0
pointValue = 5
auto_save = True
game_result = 'running'
game_speed = 0.15
dirs = {1: 'd', 2: 's', 3: 'a', 4: 'w'}

# Mohammad Kaafy
# https://github.com/mkaafy/Pacman_Colorama

def game_loop():
    global game_result, score, pac_pos, fullMap, enemyN, enemies, eaten, game_speed, dirs, pointValue
    os.system("cls")
    print_back()
    print_walls()
    print_pac()
    print_enemies()
    print_dots()
    os.system("title " + "Score: " + str(score))
    while True:
        ch = msvcrt.getch()
        if (ch == 'd') or (ch == 's') or (ch == 'a') or (ch == 'w'):
            pac_dir = ch
            break
        elif ch == '\x1b':
            game_result = 'exit'
            break

    while game_result == 'running':
        time.sleep(game_speed)
        pac_can_move = False
        if pac_dir == 'd':
            next_pos = [pac_pos[0] + 1, pac_pos[1]]
            if next_pos[0] < consoleWidth:
                pac_can_move = True
        elif pac_dir == 's':
            next_pos = [pac_pos[0], pac_pos[1] + 1]
            if next_pos[1] < consoleHeight:
                pac_can_move = True
        elif pac_dir == 'a':
            next_pos = [pac_pos[0] - 1, pac_pos[1]]
            if 0 < next_pos[0]:
                pac_can_move = True
        elif pac_dir == 'w':
            next_pos = [pac_pos[0], pac_pos[1] - 1]
            if 0 < next_pos[1]:
                pac_can_move = True
        if pac_can_move:
            next_thing = fullMap[next_pos[1]][next_pos[0]]
            if next_thing == 'w':
                pass
            elif next_thing == 'e':
                pass
            elif next_thing == 'm':
                pass
            elif next_thing == 'd':
                score += pointValue
                os.system("title " + "Score: " + str(score))
                print Style.DIM + Back.MAGENTA + pos(pac_pos[0], pac_pos[1]) + ' '
                fullMap[pac_pos[1]][pac_pos[0]] = 'n'
                pac_pos = next_pos
                fullMap[pac_pos[1]][pac_pos[0]] = 'p'
                print Fore.LIGHTYELLOW_EX + Style.DIM + Back.MAGENTA + pos(pac_pos[0], pac_pos[1]) + 'G'
            elif next_thing == 'n':
                print Style.DIM + Back.MAGENTA + pos(pac_pos[0], pac_pos[1]) + ' '
                fullMap[pac_pos[1]][pac_pos[0]] = 'n'
                pac_pos = next_pos
                fullMap[pac_pos[1]][pac_pos[0]] = 'p'
                print Fore.LIGHTYELLOW_EX + Style.DIM + Back.MAGENTA + pos(pac_pos[0], pac_pos[1]) + 'G'

        if score == fullScore:
            game_result = 'winner'
            break

        if msvcrt.kbhit():
            key_press = msvcrt.getch()
            if key_press == '\x1b':
                game_result = 'exit'
                break
            elif key_press == 'd':
                pac_dir = 'd'
            elif key_press == 's':
                pac_dir = 's'
            elif key_press == 'a':
                pac_dir = 'a'
            elif key_press == 'w':
                pac_dir = 'w'
            elif key_press == 'p':
                while True:
                    char = msvcrt.getch()
                    if char == 'p':
                        break

        t = 0
        while t < enemyN:
            cur_pos = enemies[t]
            en_can_move = False
            next_move = dirs[random.randint(1, 4)]
            if next_move == 'd':
                next_pos = [cur_pos[0], cur_pos[1] + 1]
                if next_pos[1] < consoleWidth:
                    en_can_move = True
            elif next_move == 's':
                next_pos = [cur_pos[0] + 1, cur_pos[1]]
                if next_pos[0] < consoleHeight:
                    en_can_move = True
            elif next_move == 'a':
                next_pos = [cur_pos[0], cur_pos[1] - 1]
                if 0 < next_pos[1]:
                    en_can_move = True
            elif next_move == 'w':
                next_pos = [cur_pos[0] - 1, cur_pos[1]]
                if 0 < next_pos[0]:
                    en_can_move = True
            if en_can_move:
                where = fullMap[next_pos[0]][next_pos[1]]
                if where != 'w' and where != 'm' and where != 'e':
                    if where == 'p':
                        game_result = 'looser'
                        if eaten[t] == 'd':
                            to_print = '.'
                        elif eaten[t] == 'n':
                            to_print = ' '
                        print Fore.WHITE + Style.DIM + Back.MAGENTA + pos(cur_pos[1], cur_pos[0]) + to_print
                        print Fore.LIGHTYELLOW_EX + Style.DIM + Back.MAGENTA + pos(next_pos[1], next_pos[0]) + 'e'
                        time.sleep(1.5)
                        break
                    elif where == 'd':
                        fullMap[cur_pos[0]][cur_pos[1]] = eaten[t]
                        if eaten[t] == 'd':
                            to_print = '.'
                        elif eaten[t] == 'n':
                            to_print = ' '
                        print Fore.WHITE + Style.DIM + Back.MAGENTA + pos(cur_pos[1], cur_pos[0]) + to_print
                        eaten[t] = 'd'
                        fullMap[next_pos[0]][next_pos[1]] = 'e'
                        print Fore.LIGHTRED_EX + Style.DIM + Back.MAGENTA + pos(next_pos[1], next_pos[0]) + 'e'
                        enemies[t] = next_pos
                    elif where == 'n':
                        fullMap[cur_pos[0]][cur_pos[1]] = eaten[t]
                        if eaten[t] == 'd':
                            to_print = '.'
                        elif eaten[t] == 'n':
                            to_print = ' '
                        print Fore.WHITE + Style.DIM + Back.MAGENTA + pos(cur_pos[1], cur_pos[0]) + to_print
                        eaten[t] = 'n'
                        fullMap[next_pos[0]][next_pos[1]] = 'e'
                        print Fore.LIGHTRED_EX + Style.DIM + Back.MAGENTA + pos(next_pos[1], next_pos[0]) + 'e'
                        enemies[t] = next_pos
            t += 1

    finally_check()


def finally_check():
    global game_result, score, auto_save
    if game_result == 'winner':
        os.system('cls')
        os.system("title " + "You did it!")
        text = 'mode con: cols=' + '50' + ' lines=' + '19'
        os.system(text)
        print Style.BRIGHT + Fore.LIGHTGREEN_EX + "\nYou're a " + "winner!\n"
        print 'Your score: ' + str(score)
        print
        high_exists = os.path.isfile('high.txt')
        if high_exists:
            f = open('high.txt', 'r')
            highest = f.readline()
            f.close()
            if score >= highest:
                print '\nWOW! High Score!\n'
            save_high_score()
        else:
            print '\nWOW! High Score!\n'
            save_high_score()
        os.system('pause')
    elif game_result == 'looser':
        os.system('cls')
        os.system("title " + "Game Over")
        text = 'mode con: cols=' + '50' + ' lines=' + '19'
        os.system(text)
        print Style.BRIGHT + Fore.LIGHTRED_EX + "\nYou " + "lost!\n"
        print 'Your score: ' + str(score) + '\n'
        save_high_score()
        os.system('pause')
    elif game_result == 'exit':
        print_back()
        print
        if auto_save:
            save_game()
        else:
            print Fore.LIGHTWHITE_EX + "Game " + Fore.LIGHTRED_EX + "NOT " + Fore.LIGHTWHITE_EX + "saved.\n"
        os.system('pause')


def pos(x, y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'


def print_back():
    print '\033[32;45m' + Fore.LIGHTWHITE_EX
    os.system('cls')


def print_walls():
    for i in mapList:
        print Fore.LIGHTWHITE_EX + Style.DIM + Back.LIGHTCYAN_EX + pos(i[0], i[1]) + ' '


def print_dots():
    for i in range(0, consoleHeight):
        for j in range(0, consoleWidth):
            if fullMap[i][j] == 'd':
                print Style.DIM + Fore.WHITE + Back.MAGENTA + pos(j, i) + '.'


def print_enemies():
    for i in enemies:
        print Fore.LIGHTRED_EX + Style.BRIGHT + Back.MAGENTA + pos(i[1], i[0]) + 'e'


def print_pac():
    print Fore.YELLOW + Style.BRIGHT + Back.MAGENTA + pos(pac_pos[0], pac_pos[1]) + 'G'


def reset_some_global_vars():
    global mapList, fullMap, consoleWidth, consoleHeight, enemies, eaten, wallN, enemyN
    global pac_pos, score, fullMap, fullScore, game_result
    mapList = []
    fullMap = []
    consoleWidth = 80
    consoleHeight = 24
    enemies = []
    eaten = []
    wallN = 0
    enemyN = 0
    pac_pos = [1, 1]
    score = 0
    fullScore = 0
    game_result = 'running'


def set_things_up():
    # Set the Console Size Variables
    global consoleWidth, consoleHeight
    try:
        a = mapList[0]
        consoleWidth = a[0]
        consoleHeight = a[1]
    except:
        print Fore.LIGHTCYAN_EX + '\nBad Map file. Check it please!'
        print Fore.LIGHTCYAN_EX + 'Hint: Maybe Width or Height is incorrect.'
        return False

    # Apply the Console size
    text = 'mode con: cols=' + str(consoleWidth) + ' lines=' + str(consoleHeight)
    os.system(text)

    # Set the Number of walls
    global wallN
    try:
        a = mapList[1]
        wallN = a[0]
    except:
        print Fore.LIGHTCYAN_EX + '\nBad Map file. Check it please!'
        print Fore.LIGHTCYAN_EX + 'Hint: Maybe Number of walls is incorrect.'
        return False

    # Set the Number of enemies
    global enemyN
    length = len(mapList)
    try:
        a = mapList[length-1]
        enemyN = a[0]
    except:
        print Fore.LIGHTCYAN_EX + '\nBad Map file. Check it please!'
        print Fore.LIGHTCYAN_EX + 'Hint: Maybe Number of enemies is incorrect.'
        return False

    del mapList[0], mapList[len(mapList)-1]
    del mapList[0]

    global fullMap
    for j in range(0, consoleHeight):
        temp = []
        for i in range(0, consoleWidth):
            temp += ['d']
        fullMap += [temp]

    for i in range(0, consoleWidth):
        fullMap[0][i] = 'm'
    for j in range(0, consoleHeight):
        fullMap[j][0] = 'm'

    for i in mapList:
        fullMap[i[1]][i[0]] = 'w'

    global enemies
    t = 0
    while t < enemyN:
        ran_h = random.randint(0, consoleHeight - 1)
        ran_w = random.randint(0, consoleWidth - 1)
        inside = fullMap[ran_h][ran_w]
        if inside != 'w' and inside != 'm':
            fullMap[ran_h][ran_w] = 'e'
            enemies += [[ran_h, ran_w]]
            t += 1

    global eaten
    for i in range(0, enemyN):
        eaten += ['d']

    global pac_pos
    pac_placed = False
    while not pac_placed:
        ran_h = random.randint(0, consoleHeight - 1)
        ran_w = random.randint(0, consoleWidth - 1)
        inside = fullMap[ran_h][ran_w]
        if inside != 'w' and inside != 'e' and inside != 'm':
            fullMap[ran_h][ran_w] = 'p'
            pac_pos = [ran_w, ran_h]
            pac_placed = True

    global fullScore
    n = consoleHeight * consoleWidth
    n -= wallN
    n -= consoleHeight + consoleWidth
    fullScore = n * pointValue

    return True


def menu():
    text = 'mode con: cols=' + '50' + ' lines=' + '19'
    os.system(text)
    while True:
        os.system("title " + "Pac-Man Game")
        print_menu()
        try:
            choice = input()
        except NameError:
            print Fore.LIGHTYELLOW_EX + '\nHey! Enter Correctly!\n'
            os.system('pause')
        except SyntaxError:
            print Fore.LIGHTYELLOW_EX + "\nYou didn't enter anything!\n"
            os.system('pause')
        else:
            if choice == 1:
                while True:
                    if new_game():
                        game_loop()
                        reset_some_global_vars()
                        text = 'mode con: cols=' + '50' + ' lines=' + '19'
                        os.system(text)
                        break
                    else:
                        text = 'mode con: cols=' + '50' + ' lines=' + '19'
                        os.system(text)
                        break
            elif choice == 2:
                while True:
                    if load_game():
                        game_loop()
                        reset_some_global_vars()
                        text = 'mode con: cols=' + '50' + ' lines=' + '19'
                        os.system(text)
                        break
                    else:
                        text = 'mode con: cols=' + '50' + ' lines=' + '19'
                        os.system(text)
                        break
            elif choice == 3:
                auto_save_menu()
            elif choice == 4:
                high_score_menu()
            elif choice == 5:
                game_speed_menu()
            elif choice == 6:
                help_menu()
            elif choice == 7:
                about_page()
            elif choice == 8:
                print '\nBye-Bye!'
                exit()
            elif choice == 9:
                reset_high_save()
            else:
                print '\nYou must enter a number between 1 and 9.\n'
                os.system('pause')


def new_game():
    print_back()
    print Fore.LIGHTWHITE_EX + '\n- - - - - - - - - - New Game - - - - - - - - - - -\n'
    map_name = raw_input('Enter the map file name Without .txt:\n\n') + '.txt'
    if map_reader(map_name):
        if set_things_up():
            return True
        else:
            os.system('pause')
            return False
    else:
        os.system('pause')
        return False


def save_game():
    f = open('save.pck', 'w')
    pickle.dump(consoleHeight, f)
    pickle.dump(consoleWidth, f)

    pickle.dump(score, f)
    pickle.dump(pointValue, f)
    pickle.dump(fullScore, f)

    pickle.dump(enemyN, f)
    pickle.dump(wallN, f)

    pickle.dump(mapList, f)
    pickle.dump(fullMap, f)

    pickle.dump(pac_pos, f)
    pickle.dump(enemies, f)
    pickle.dump(eaten, f)

    pickle.dump(game_speed, f)
    pickle.dump(auto_save, f)

    f.close()

    print Fore.LIGHTYELLOW_EX + 'Game Saved.\n' + Fore.LIGHTWHITE_EX


def load_game():
    save_exists = os.path.isfile('save.pck')
    if save_exists:
        global consoleHeight, consoleWidth, score, pointValue, fullScore, enemyN, wallN
        global mapList, fullMap, pac_pos, enemies, eaten, game_speed, auto_save
        f = open('save.pck', 'r')
        consoleHeight = pickle.load(f)
        consoleWidth = pickle.load(f)

        score = pickle.load(f)
        pointValue = pickle.load(f)
        fullScore = pickle.load(f)

        enemyN = pickle.load(f)
        wallN = pickle.load(f)

        mapList = pickle.load(f)
        fullMap = pickle.load(f)

        pac_pos = pickle.load(f)
        enemies = pickle.load(f)
        eaten = pickle.load(f)

        game_speed = pickle.load(f)
        auto_save = pickle.load(f)

        f.close()

        text = 'mode con: cols=' + str(consoleWidth) + ' lines=' + str(consoleHeight)
        os.system(text)

        return True
    else:
        os.system('cls')
        print Fore.LIGHTGREEN_EX + '\nHey! There is no save file!\n' + Fore.LIGHTWHITE_EX
        os.system('pause')
        return False


def auto_save_menu():
    os.system('cls')
    os.system("title " + "Auto Save Settings")
    global auto_save
    if auto_save:
        print Style.DIM + Fore.LIGHTWHITE_EX + '\nAuto Save is ' + Fore.LIGHTGREEN_EX + 'ON.\n'
    elif not auto_save:
        print Style.DIM + Fore.LIGHTWHITE_EX + '\nAuto Save is ' + Fore.LIGHTRED_EX + 'OFF.\n'
    print Style.DIM + Fore.LIGHTGREEN_EX + '1. ON'
    print Style.DIM + Fore.LIGHTRED_EX + '2. OFF'
    print Style.DIM + Fore.LIGHTWHITE_EX + '3. Go Back\n'
    try:
        ch = input('Enter your choice: ')
    except NameError:
        print Fore.LIGHTYELLOW_EX + '\nHey! Enter Correctly!\n'
        os.system('pause')
    except SyntaxError:
        print Fore.LIGHTYELLOW_EX + "\nYou didn't enter anything!\n"
        os.system('pause')
    else:
        if ch == 1:
            auto_save = True
        elif ch == 2:
            auto_save = False
        elif ch == 3:
            pass
        else:
            print '\nYou must enter a number between 1 and 3.\n'
            os.system('pause')


def high_score_menu():
    os.system('cls')
    os.system("title " + "High Scores")
    print 'Top 10 High Scores\n' + Fore.LIGHTCYAN_EX + '------------------' + Fore.LIGHTWHITE_EX
    f = open('high.txt', 'a+')
    score_array = f.readlines()
    f.close()
    if not score_array:
        print '\n No Scores yet!\n'
    else:
        for i in range(0, len(score_array)):
            if i > 9:
                break
            print score_array[i],
        f.close()
    if len(score_array) == 1:
        print Fore.LIGHTCYAN_EX + '\n------------------' + Fore.LIGHTWHITE_EX
    else:
        print Fore.LIGHTCYAN_EX + '------------------' + Fore.LIGHTWHITE_EX
    os.system('pause')


def save_high_score():
    global score
    high_exists = os.path.isfile('high.txt')
    if not high_exists:
        f = open('high.txt', 'w')
        f.write(str(score))
        f.close()
    else:
        f = open('high.txt', 'r+')
        whole = f.read()
        str_scores = whole.split()
        all_scores = []
        for i in str_scores:
            all_scores += [int(i)]
        all_scores += [score]
        all_scores.sort(reverse=True)
        f.close()
        f = open('high.txt', 'w')
        for i in range(0, len(all_scores)):
            f.write(str(all_scores[i]) + '\n')
        f.close()


def about_page():
    os.system('cls')
    os.system("title " + "About Developer")
    print Style.DIM + Fore.LIGHTYELLOW_EX + 'Created with love by Mohammad Kaafi.'
    print Style.DIM + Fore.LIGHTGREEN_EX + '\n29 December 2016'
    print Style.DIM + Fore.LIGHTCYAN_EX + '\nVersion: 1.0\n'
    print Style.DIM + Fore.LIGHTWHITE_EX + 'Press any key to go back...',
    msvcrt.getch()


def print_menu():
    print '\033[32;45m'
    os.system('cls')
    print pos(20, 4) + Fore.LIGHTBLACK_EX + """
                            111111111111
                          1111111111111111
                        1111111111111111
                       11111111111111
                      111111111111      00    00
                      111111111111      00    00
                       11111111111111
                        1111111111111111
                          1111111111111111
                            111111111111
                                                    """ + pos(1, 1)
    print Style.DIM + Fore.LIGHTWHITE_EX + '- - - - - - - - - PAC-MAN Game! - - - - - - - - -\n'
    print Style.DIM + Fore.LIGHTRED_EX + '1. New Game'
    print Style.DIM + Fore.LIGHTGREEN_EX + '2. Load Game'
    print Style.DIM + Fore.LIGHTWHITE_EX + '3. Auto Save Options'
    print Style.DIM + Fore.LIGHTYELLOW_EX + '4. High Scores'
    print Style.DIM + Fore.LIGHTCYAN_EX + '5. Game Speed'
    print Style.DIM + Fore.LIGHTRED_EX + '6. Help'
    print Style.DIM + Fore.LIGHTYELLOW_EX + '7. About'
    print Style.DIM + Fore.LIGHTGREEN_EX + '8. Exit'
    print Style.DIM + Fore.LIGHTCYAN_EX + '9. RESET'
    print Style.DIM + Fore.LIGHTWHITE_EX + '\n\nEnter your choice:',


def help_menu():
    os.system('cls')
    text = 'mode con: cols=' + '63' + ' lines=' + '18'
    os.system(text)
    os.system("title " + "Help")
    print 'Keys:\n'
    print Fore.LIGHTRED_EX + 'esc: ' + Fore.RESET + 'Ends the game and saves it if auto-save is ON.'
    print Fore.LIGHTMAGENTA_EX + '  p: ' + Fore.RESET + 'Pauses the game. Hit the key again to continue the game.'
    print Fore.LIGHTCYAN_EX + '  d: ' + Fore.RESET + 'Move Right.'
    print Fore.LIGHTCYAN_EX + '  s: ' + Fore.RESET + 'Move Down.'
    print Fore.LIGHTCYAN_EX + '  a: ' + Fore.RESET + 'Move Left.'
    print Fore.LIGHTCYAN_EX + '  w: ' + Fore.RESET + 'Move Up.\n'
    print 'You can see your score in title bar.\n'
    os.system('pause')
    text = 'mode con: cols=' + '50' + ' lines=' + '19'
    os.system(text)


def reset_high_save():
    os.system('cls')
    os.system("title " + "Reset High score and save file")
    print Style.DIM + Fore.LIGHTYELLOW_EX + 'Are you sure? (y/n) '
    answer = raw_input()
    if answer == 'y' or answer == 'Y':
        save_exists = os.path.isfile('save.pck')
        if save_exists:
            os.remove('save.pck')
            print Fore.LIGHTRED_EX + '\nSave file Removed!' + Fore.LIGHTWHITE_EX
        else:
            print Fore.LIGHTGREEN_EX + '\nThere is no save file to remove!' + Fore.LIGHTWHITE_EX
        high_exists = os.path.isfile('high.txt')
        if high_exists:
            os.remove('high.txt')
            print Fore.LIGHTRED_EX + '\nHigh Scores cleaned!\n' + Fore.LIGHTWHITE_EX
        else:
            print Fore.LIGHTGREEN_EX + '\nNo high scores to delete!\n' + Fore.LIGHTWHITE_EX
    elif answer == 'n'or answer == 'N':
        pass
    else:
        print '\nYou must enter y or n!\n'
    os.system('pause')


def game_speed_menu():
    os.system('cls')
    os.system("title " + "Game Speed")
    global game_speed
    if game_speed == 0.15:
        print Fore.LIGHTWHITE_EX + '\nCurrent game speed is ' + Fore.LIGHTYELLOW_EX + 'Normal.\n'
    elif game_speed == 0.25:
        print Fore.LIGHTWHITE_EX + 'Current game speed is ' + Fore.LIGHTGREEN_EX + 'Slow.\n'
    elif game_speed == 0.10:
        print Fore.LIGHTWHITE_EX + 'Current game speed is ' + Fore.LIGHTRED_EX + 'Fast.\n'
    print Fore.LIGHTGREEN_EX + '1. Slow'
    print Fore.LIGHTYELLOW_EX + '2. Normal'
    print Fore.LIGHTRED_EX + '3. Fast' + Fore.LIGHTWHITE_EX
    print '4. Go Back\n'
    try:
        choice = input('Enter your choice: ')
    except NameError:
        print Fore.LIGHTYELLOW_EX + '\nHey! Enter Correctly!\n'
        os.system('pause')
    except SyntaxError:
        print Fore.LIGHTYELLOW_EX + "\nYou didn't enter anything!\n"
        os.system('pause')
    else:
        if choice == 1:
            game_speed = 0.25
        elif choice == 2:
            game_speed = 0.15
        elif choice == 3:
            game_speed = 0.10
        elif choice == 4:
            pass
        else:
            print '\nYou must enter a number between 1 and 4!\n'
            os.system('pause')


def map_reader(map_name):
    global mapList
    if os.path.isfile(map_name):
        f = open(map_name, 'r')
        mapList = f.readlines()
        f.close()
        for lines in range(0, len(mapList)):
            a = mapList[lines].split()
            temp = []
            for i in range(0, len(a)):
                temp += [int(a[i])]
            mapList[lines] = temp
        return True
    else:
        print Fore.LIGHTYELLOW_EX + "\nMap doesn't exist.\n" + Fore.LIGHTWHITE_EX
        return False


init()
menu()
