"The ATM Dispenser Chain"
from dispenser import Dispenser, Dispenser1


class ATMDispenserChain:  # pylint: disable=too-few-public-methods
    "The Chain Client"

    def __init__(self):
        # initializing the successors chain
        self.chain1 = Dispenser(domination=1000)
        self.chain2 = Dispenser(domination=500)
        self.chain3 = Dispenser(domination=100)
        self.chain4 = Dispenser(domination=50)
        self.chain5 = Dispenser(domination=10)
        self.chain6 = Dispenser(domination=5)
        self.chain7 = Dispenser1()

        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)
        self.chain3.next_successor(self.chain4)
        self.chain4.next_successor(self.chain5)
        self.chain5.next_successor(self.chain6)
        self.chain6.next_successor(self.chain7)
