# камень – 1, ножницы - 2, бумага - 3.

import random


def comp_choice():
    value = random.randint(1, 3)
    return value


def user_choice(user_value):
    while user_value not in ["1", "2", "3"]:
        user_value = input("Камень – 1, Ножницы - 2, Бумага - 3 (Введите 1-3):\n")

    return int(user_value)


def gamestart():
    user_answer = input("Выберите режим игры: (Турнир | Обычная)\n").lower()

    while user_answer.isdigit() or user_answer not in ["турнир", "обычная"]:
        user_answer = input(
            "Выберите режим игры: (Турнир | Обычная)\n!НУЖНО ВВОДИТЬ ТОЛЬКО ЗНАЧЕНИЯ ИЗ СКОБОК!\n").lower()

    if user_answer == "турнир":
        tournament_game()
    elif user_answer == "обычная":
        simple_game()


def simple_game():
    play_again = input("Введите ДА если хотите продолжить, либо НЕТ, чтобы сменить режим игры\n").lower()
    while play_again not in ["да", "нет"]:
        play_again = input("Нужно --> ДА | НЕТ").lower()

    if play_again == "нет":
        gamestart()

    while play_again == "да":
        user_value = input("Камень – 1, Ножницы - 2, Бумага - 3:\n")
        correct_user_value = user_choice(user_value)  # То что ввел игрок
        comp_value = comp_choice()  # То что ввел компуктер

        if correct_user_value == 1:
            print("Вы выбрали КАМЕНЬ")
        elif correct_user_value == 2:
            print("Вы выбрали НОЖНИЦЫ")
        else:
            print("Вы выбрали БУМАГУ")

        if comp_value == 1:
            print("Компуктер выбрал КАМЕНЬ")
        elif comp_value == 2:
            print("Компуктер выбрал НОЖНИЦЫ")
        else:
            print("Компуктер выбрал БУМАГУ")

        if correct_user_value == 1:
            if comp_value == 1:
                wins = 0
            elif comp_value == 2:
                wins = 1
            else:
                wins = 2
        elif correct_user_value == 2:

            if comp_value == 1:
                wins = 2
            elif comp_value == 2:
                wins = 0
            else:
                wins = 1
        else:
            if comp_value == 1:
                wins = 1
            elif comp_value == 2:
                wins = 2
            else:
                wins = 0
        if wins == 0:
            print("Ничья")
        elif wins == 1:
            print("Вы победили")
        else:
            print("Компуктер победил")

        play_again = input("Хотите сыграть еще? ").lower()
        while play_again not in ["да", "нет"]:
            play_again = input("Хотите сыграть еще? ").lower()

    if play_again == "нет":
        userAnswer = input("Может вы хотите сменить режим игры?\nЕсли ДА то ENTER, если НЕТ то напишите ВАЛЮ").lower()

        while userAnswer.isdigit() or userAnswer not in ["", "валю"]:
            userAnswer = input("Нажмите ENTER либо введите ВАЛЮ").lower()

        if userAnswer == "":
            gamestart()
        else:
            print("Вы прервали игру ")


def valid_check(amount_rounds):
    while not amount_rounds.isdigit():
        amount_rounds = input("Введите кол-во раундов: (ТОЛЬКО ЧИСЛОВОЙ ВВОД)\n")

    return int(amount_rounds)


def draw(comp_wins, user_wins, rounds):
    if comp_wins == user_wins:
        print("\nДобавлен +1 раунд из-за ничьи\n")
        rounds += 1

    return rounds


def tournament_game():
    rounds = input("Введите кол-во раундов: ")
    rounds = valid_check(rounds)

    count_rounds = 0
    comp_wins = 0
    user_wins = 0

    while count_rounds != rounds:
        user_value = input("Камень – 1, Ножницы - 2, Бумага - 3:\n")
        correct_user_value = user_choice(user_value)  # То что ввел игрок
        comp_value = comp_choice()  # То что ввел компуктер

        if correct_user_value == 1:
            print("Вы выбрали КАМЕНЬ")
        elif correct_user_value == 2:
            print("Вы выбрали НОЖНИЦЫ")
        else:
            print("Вы выбрали БУМАГУ")

        if comp_value == 1:
            print("Компуктер выбрал КАМЕНЬ")
        elif comp_value == 2:
            print("Компуктер выбрал НОЖНИЦЫ")
        else:
            print("Компуктер выбрал БУМАГУ")

        if correct_user_value == 1:
            if comp_value == 1:
                comp_wins += 1
                user_wins += 1
            elif comp_value == 2:
                user_wins += 1
            else:
                comp_wins += 1
        elif correct_user_value == 2:

            if comp_value == 1:
                comp_wins += 1
            elif comp_value == 2:
                comp_wins += 1
                user_wins += 1
            else:
                user_wins += 1
        else:
            if comp_value == 1:
                user_wins += 1
            elif comp_value == 2:
                comp_wins += 1
            else:
                comp_wins += 1
                user_wins += 1

        count_rounds += 1
        if rounds == count_rounds:
            rounds = draw(comp_wins, user_wins, rounds)

    if comp_wins > user_wins:
        print(f"\nКомпуктер выйграл со счетом {comp_wins} : {user_wins}")
    elif comp_wins < user_wins:
        print(f"\nПользователь выйграл со счетом {user_wins} : {comp_wins}")

    user_answer = input("Хотите ли вы выбрать новый режим игры? Если НЕТ то нажмите ENTER\n").lower()
    while user_answer.isdigit() or user_answer not in ["да", "нет", "не хочу", "хочу", ""]:
        user_answer = input("Хотите ли вы выбрать новый режим игры? (да, нет, не хочу, хочу)\n").lower()

    if user_answer in ["да", "нет"]:
        gamestart()
    else:
        print("Вы закончили игру ")


start_game = input("Хотите начать игру? ").lower()
while start_game.isdigit() or start_game not in ["да", "нет"]:
    user_rep = input("Ответ ДА либо НЕТ").lower()

if start_game == "да":
    gamestart()
else:
    print("Вы прервали игру ")
