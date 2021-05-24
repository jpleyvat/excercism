class Luhn:
    def __init__(self, card_num):
        card_num = card_num.replace(" ", "")
        self.num = card_num

    def valid(self):
        if len(self.num) <= 1 or not self.num.isnumeric():
            return False
        checksum = []
        for i in range(len(self.num) - 1, -1, -1):
            if (len(self.num) - i) % 2 == 0:
                doubled = int(self.num[i]) * 2
                if doubled > 9:
                    doubled -= 9
                checksum.append(doubled)
                continue
            checksum.append(int(self.num[i]))

        return sum(checksum) % 10 == 0
