# JankenGame クラスを定義しよう
class JanKenGame:
    def play(self, left_hand: int, right_hand: int):
        result = self.judge(left_hand, right_hand)
        self.show_result(result)

    def judge(self, left_hand: int, right_hand: int) -> int:
        # 勝敗を判定して結果（1:勝ち, 2:引き分け, 3:負け）を返却しよう
        if left_hand == 0:  # Goo
            if right_hand == 0:  # Goo
                return 2
            elif right_hand == 1:  # Tyoki
                return 1
            else:  # Paa
                return 3
        elif left_hand == 1:  # Tyoki
            if right_hand == 0:  # Goo
                return 3
            elif right_hand == 1:  # Tyoki
                return 2
            else:  # Paa
                return 1
        else: # Paa
            if right_hand == 0:  # Goo
                return 1
            elif right_hand == 1:  # Tyoki
                return 3
            else:  # Paa
                return 2

    def show_result(self, result: int):
        # 結果をもとに勝敗を print を使って表示しよう
        if result == 1:
            print("勝ち")
        elif result == 2:
            print("引き分け")
        else:
            print("負け")


# JankenGame クラスを使ってジャンケンをしよう
def main():
    game = JanKenGame()
    game.play(1, 2)

if __name__ == '__main__':
    main()
