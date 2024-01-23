from field import Field

class Pawn:
    def __init__(self, belongsTo):
        self.belongsTo = belongsTo
        self.isOn = None
        self.goal = False

    def move(self, spaces, players):
        print(self.isOn)
        self.isOn.remove_pawn(self)
        print(self.isOn)
        k = 0
        for i in range(spaces):
            print("Les move")
            if self.isOn is None:
                self.belongsTo.goaled += 1
                break
            self.isOn = self.isOn.next
            print("What")
            if self.isOn == self.belongsTo.entry:
                print("WHO")
                k = spaces - i
                break

        if k > 0:
            self.goal = True
            self.isOn = self.belongsTo.goal
            k += 1
            for i in range(k):
                if self.isOn.next is None:
                    self.goal = True
                else:
                    self.isOn = self.isOn.next
        if self.isOn is not None:
            self.isOn.add_pawn(self)
            if len(self.isOn.pawns) > 1:
                for pawn in self.isOn.pawns:
                    if pawn.belongsTo != self.belongsTo:
                        start = False
                        for player in players:
                            if self.isOn == player.entry and pawn.belongsTo == player:
                                start = True
                        if start is False:
                            pawn.isOn = None
                            self.isOn.remove_pawn(pawn)
                        else:
                            self.isOn.remove_pawn(self)
                            self.isOn = None
                            return

    def move_out(self):
        self.isOn = self.belongsTo.entry
        self.isOn.add_pawn(self)
        if len(self.isOn.pawns) > 1:
            for pawn in self.isOn.pawns:
                if pawn.belongsTo != self.belongsTo:
                    pawn.isOn = None
                    self.isOn.remove_pawn(pawn)