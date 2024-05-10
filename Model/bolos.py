class Bolos:
    def __init__(self):
        self.rolls = []
        self.frames = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0
        for frame in range(10):
            if roll_index < len(self.rolls):
                frame = Frame(self.rolls[roll_index:])
                self.frames.append(frame)
                total_score += frame.score()
                roll_index += frame.rolls_count()

        return total_score


class Frame:
    def __init__(self, rolls):
        self.rolls = rolls

    def is_strike(self):
        return self.rolls[0] == 10

    def is_spare(self):
        return sum(self.rolls[:2]) == 10

    def score(self):
        if self.is_strike():
            return Strike(self.rolls).score()
        elif self.is_spare():
            return Spare(self.rolls).score()
        else:
            return NormalFrame(self.rolls).score()

    def rolls_count(self):
        return 1 if self.is_strike() else 2


class NormalFrame:
    def __init__(self, rolls):
        self.rolls = rolls

    def score(self):
        return sum(self.rolls[:2])


class Spare:
    def __init__(self, rolls):
        self.rolls = rolls

    def score(self):
        return 10 + self.bonus()

    def bonus(self):
        return self.rolls[2]


class Strike:
    def __init__(self, rolls):
        self.rolls = rolls

    def score(self):
        return 10 + self.bonus()

    def bonus(self):
        return sum(self.rolls[1:3])
