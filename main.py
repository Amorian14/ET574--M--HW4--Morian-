import random

class Reel:
    def __init__(self, max_value=9):
        self.max_value = max_value

    def spin(self):
        return random.randint(0, self.max_value)


class SlotMachine:
    def __init__(self):
        self.reel1 = Reel()
        self.reel2 = Reel()
        self.reel3 = Reel()

    def evaluate_spin(self, r1, r2, r3):
        if r1 == r2 == r3:
            return "WIN"
        if r1 == 0 or r2 == 0 or r3 == 0:
            return "LOSE"
        return "SPIN AGAIN"

    def play_round(self):
        r1 = self.reel1.spin()
        r2 = self.reel2.spin()
        r3 = self.reel3.spin()
        total = r1 + r2 + r3
        result = self.evaluate_spin(r1, r2, r3)
        return {
            "reels": (r1, r2, r3),
            "total": total,
            "result": result
        }
