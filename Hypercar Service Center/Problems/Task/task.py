class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    def __add__(self, other):
        descr = self.description + "\n" + other.description
        team = self.team + ", " + other.team
        return Task(descr, team)