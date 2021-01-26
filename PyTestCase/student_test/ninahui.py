import random
import string

winner_third = []
winner_second = []
all_workers = []
for i in range(300):
    all_workers.append(i)


def third():
    while True:
        num = random.choice(all_workers)
        if num in winner_third:
            continue
        else:
            winner_third.append(num)
            print(f"恭喜 {num} 获得三等奖")
        if len(winner_third) >= 6:
            break


def second():
    while True:
        num = random.choice(all_workers)
        if num in winner_third and winner_second:
            continue
        else:
            winner_second.append(num)
            print(f"恭喜 {num} 获得二等奖")
        if len(winner_second) >= 3:
            break


def first():
    while True:
        num = random.choice(all_workers)
        if num in winner_third and winner_second:
            continue
        else:
            winner_second.append(num)
            print(f"恭喜 {num} 获得一等奖,大奖，撒花")
            break


if __name__ == '__main__':
    third()
    second()
    first()
