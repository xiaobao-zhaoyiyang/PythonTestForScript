import random
import string

count = 0
while count < 3:
    car_num = [] # 存储用户选择的号
    for i in range(20):
        n1 = random.choice(string.ascii_uppercase) #生成第一个
        n2 = random.sample(string.ascii_uppercase+string.digits, 5)
        n2 = "".join(n2)
        c_num = f"京{n1}-{n2}"
        print(c_num)
        car_num.append(c_num)
    choice = input("输入您喜欢的：").strip()
    if choice in car_num:
        print(f"恭喜您选择了您的车牌号：{choice}")
        exit("Good luck")
    else:
        print("不合法的选择")

    count += 1