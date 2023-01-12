import random

def generate_numbers():
    new_list = []
    size_number = 0
    while size_number < 3:
        new_number = random.randint(0, 9)
        if new_number not in new_list:
            new_list.append(new_number)
            size_number += 1

    return new_list


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    user_guess = []
    while len(user_guess) < 3:
        take_input = int(input("{}번째 숫자를 입력하세요: ".format(len(user_guess) + 1)))

        if take_input in user_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        elif take_input < 0 or take_input > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif take_input not in user_guess:
            user_guess.append(take_input)

    return user_guess




def get_score(guesses, solution):
    strike_counts = 0
    ball_counts = 0

    for i in range(len(guesses)):
        if guesses[i] == solution[i]:
            strike_counts += 1
        elif guesses[i] != solution[i] and guesses[i] in solution:
            ball_counts += 1

    return strike_counts, ball_counts



# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

print("축하합니다. {}번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다.".format(tries))






