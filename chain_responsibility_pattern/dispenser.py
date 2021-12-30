
from interface_dispenser import IDispenser


class Dispenser1(IDispenser):

    def __init__(self, domination: int = None):
        super().__init__(domination)
        self._successor = None

    def next_successor(self, successor):
        "Set the next successor"
        self._successor = successor

    def handle(self, amount):
        "Handle the dispensing of notes"
        if amount >= 1:
            print(f"Dispensing {amount} 1 note")
        else:
            self._successor.handle(amount)

class Dispenser(IDispenser):

    def __init__(self, domination: int):
        super().__init__(domination)
        self._successor = None

    def next_successor(self, successor):
        "Set the next successor"
        self._successor = successor

    def handle(self, amount):
        "Handle the dispensing of notes"
        if amount >= self.domination:
            num = amount // self.domination
            remainder = amount % self.domination
            print(f"Dispensing {num} {self.domination} note")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)



# class Dispenser10(IDispenser):
#
#     def __init__(self):
#         self._successor = None
#
#     def next_successor(self, successor):
#         "Set the next successor"
#         self._successor = successor
#
#     def handle(self, amount):
#         "Handle the dispensing of notes"
#         if amount >= 10:
#             num = amount // 10
#             remainder = amount % 10
#             print(f"Dispensing {num} 10 note")
#             if remainder != 0:
#                 self._successor.handle(remainder)
#         else:
#             self._successor.handle(amount)

# class Dispenser20(IDispenser):
#
#     def __init__(self):
#         self._successor = None
#
#     def next_successor(self, successor):
#         "Set the next successor"
#         self._successor = successor
#
#     def handle(self, amount):
#         "Handle the dispensing of notes"
#         if amount >= 20:
#             num = amount // 20
#             remainder = amount % 20
#             print(f"Dispensing {num} 20 note(s)")
#             if remainder != 0:
#                 self._successor.handle(remainder)
#         else:
#             self._successor.handle(amount)
#
# class Dispenser50(IDispenser):
#
#     def __init__(self):
#         self._successor = None
#
#     def next_successor(self, successor):
#         "Set the next successor"
#         self._successor = successor
#
#     def handle(self, amount):
#         "Handle the dispensing of notes"
#         if amount >= 50:
#             num = amount // 50
#             remainder = amount % 50
#             print(f"Dispensing {num} 50 note(s)")
#             if remainder != 0:
#                 self._successor.handle(remainder)
#         else:
#             self._successor.handle(amount)
#
# class Dispenser100(IDispenser):
#
#     def __init__(self):
#         self._successor = None
#
#     def next_successor(self, successor):
#         "Set the next successor"
#         self._successor = successor
#
#     def handle(self, amount):
#         "Handle the dispensing of notes"
#         if amount >= 100:
#             num = amount // 100
#             remainder = amount % 100
#             print(f"Dispensing {num} 100 note(s)")
#             if remainder != 0:
#                 self._successor.handle(remainder)
#         else:
#             self._successor.handle(amount)
