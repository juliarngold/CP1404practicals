class Guitar:
    def __init__(self, name="", year=0,cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.cost < other.cost

    def get_age(self):
        """get age"""
        return 2024 - self.year

    def is_vintage(self):
        """is vintage if its 50 or older"""
        if self.get_age() >= 50:
            return True
        else:
            return False