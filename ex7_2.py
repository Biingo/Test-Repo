#!/usr/bin/env python3

"""
Viết 1 một trò chơi đánh đối kháng giữa 2 nhân vật. Mỗi nhân vật có tên (str),
máu (int), vũ khí.
Vũ khí chọn random khi tạo nhân vật, có damage (int) bằng lượng máu trừ đi
khi đánh trúng.

Cho 2 nhân vật lần lượt đánh nhau, print kết quả mỗi lượt đánh, print người
thắng.

"""


class Fighter():
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def __str__(self):
        return "{}: {}".format(self.name, self.HP)


class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


def solve(player1, player2):
    """Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)"""
    result = ("", 0)
    F1 = player1
    F2 = player2
    W1 = Weapon('bao', 30)
    W2 = Weapon('bua', 50)
    W3 = Weapon('keo', 40)
    import random
    W123 = [W1, W2, W3]
    VK = random.choice(W123)
    while F1.HP > 0 and F2.HP > 0:
        print(F1, F2)
        VK = random.choice(W123)
        print("{} tan cong {} bang vu khi {}". format(F1.name,
              F2.name, VK.name))
        F2.HP = F2.HP - VK.damage
        if F2.HP < 0:
            break

        print(F2, F1)
        VK = random.choice(W123)
        print("{} tan cong {} bang vu khi {}". format(F2.name,
              F1.name, VK.name))
        F1.HP = F1.HP - VK.damage
        if F1.HP <= 0:
            print("{} cui bap {} thang". format(F1.name, F2.name))
            result = (F2.name, F2.HP)
        else:
            print("{} cui bap {} thang". format(F2.name, F1.name))
            result = (F1.name, F1.HP)
    return result


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter('Pi', 200)
    player2 = Fighter('Miu', 150)
    print(solve(player1, player2))


if __name__ == "__main__":
    main()
