import modules


class Player:

    def __init__(self):
        self.sheet = modules.create_sheet()

    def remove_number(self, barrel_number):
        decision = input("Зачеркнуть цифру?(да/нет)")
        if decision == "да" and barrel_number in self.sheet:
            self.sheet = self.sheet.remove(barrel_number)
        elif decision == "нет":
            pass


