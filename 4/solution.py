class Card:
    def __init__(self, id, winning_numbers, my_numbers) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers

    def matches(self) -> int:
        n = 0
        for number in self.my_numbers:
            if number in self.winning_numbers:
                n += 1
        return n

    def score(self) -> int:
        n = self.matches()
        if n == 0:
            return 0
        else:
            return pow(2, n - 1)

    @classmethod
    def create_card(cls, line: str) -> "Card":
        card_id_str, numbers_str = line.split(":")
        card_id = int(card_id_str.split()[1])

        winning_numbers_str, my_numbers_str = numbers_str.split(" | ")
        winning_numbers = [int(number) for number in winning_numbers_str.split()]
        my_numbers = [int(number) for number in my_numbers_str.split()]

        return cls(card_id, winning_numbers, my_numbers)


def main():
    with open("4/input.txt", "r") as f:
        lines = f.read().split("\n")

    score1 = 0
    score2 = 0
    card_copies = {}

    for i in range(len(lines)):
        card = Card.create_card(lines[i])
        card_matches = card.matches()
        card_score = card.score()
        score1 += card_score
        score2 += card_copies.get(i, 0) + 1

        for j in range(i + 1, i + card_matches + 1):
            card_copies[j] = card_copies.get(j, 0) + card_copies.get(i, 0) + 1

    print("answer1:", score1)
    print("answer2:", score2)


if __name__ == "__main__":
    main()
