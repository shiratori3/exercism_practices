class Luhn:
    valid_chars = set(" 0123456789")

    def __init__(self, card_num: str):
        self.nums = card_num.strip()[::-1]

    def valid(self):
        if len(self.nums) <= 1:
            return False
        if len(set(self.nums) - Luhn.valid_chars) > 0:
            return False

        total = []
        for index, num in enumerate(self.nums.replace(" ", "")):
            if index % 2 == 1:
                doubled = int(num) * 2
                total.append(doubled - 9 if doubled > 9 else doubled)
            else:
                total.append(int(num))
        return sum(total) % 10 == 0
