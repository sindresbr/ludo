from die import Die
from pawn import Pawn
from field import Field
from player import Player

class Board:
    def __init__(self):
        self.die = Die()
        self.pawns = []
        self.players = []
        self.fields = []
        self.goals = []

        #Put the fields on the board
        field = Field(0)
        self.fields.append(field)
        for i in range(51):
            field = Field(i+1)
            self.fields.append(field)
            self.fields[i].next = field

        self.fields[len(self.fields)-1].next = self.fields[0]

        #Initialize the players
        for i in range(4):
            entry = self.fields[i*13]
            field = Field(52+i+i*5)
            self.goals.append(field)
            entry.goal = field
            goal = entry.goal
            player = Player(goal, entry, i) #Add goal and entry
            self.players.append(player)

            #Make goal area
            for j in range(4):
                next = Field(53+j +5*i)
                self.goals.append(next)
                goal.next = next
                goal = next

        #Initialize the pawns
        gibb = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
        for i in range(16):
            pawn = Pawn(self.players[gibb[i]])
            self.pawns.append(pawn)
            self.players[gibb[i]].add_pawn(pawn)

    def play(self):
        winner = False

        turns = 0
        while not winner:
            turns += 1
            for player in self.players:
                self.play_once(player)
                if player.goaled == len(player.pawns):
                    winner = True
                pawns = ""
                for pawn in player.pawns:
                    pawns += str(pawn.isOn)
                print(pawns)
            for player in b.players:
                print(f"Pieces in goals for {player.id}: {player.goaled}")

        print(f"Turns: {turns}")

    def play_once(self,player):
            num = self.die.roll()
            print(f"Player: {player.id}, roll: {num}")
            if num == self.die.eyes:
                print("Wheeee, move out")
                self.move_out(player, num)
                self.play_once(player)
            else:
                active = []
                for j in range(len(player.pawns)):
                    if player.pawns[j].isOn is not None:
                        print(player.pawns[j].isOn)
                        active.append(player.pawns[j])

                if len(active) > 0:
                    self.move(active, num)

    def move_out(self, player, die):
        moved_out = False
        for j in range(len(player.pawns)):
            if player.pawns[j].isOn is None and player.pawns[j].goal == False:
                player.pawns[j].move_out()
                moved_out = True
                print("Wohoo")
                break
        if not moved_out:
            self.move(player.pawns, die)

        self.print_board()
        input()

    def move(self, pawns, die):
        print("Gibbigabb")
        for i in range(len(pawns)):
            if pawns[i].isOn is not None:
                pawns[i].move(die, self.players)
                break

        self.print_board()
        input()

    def print_board(self):
        """
        text = ""
        for g in range(4):
            text += "\n"
            for i in range(13):
                text += "["
                if len(self.fields[i+g*13].pawns) > 0:
                    for pawn in self.fields[i+g*13].pawns:
                        text += str(pawn.belongsTo.id)   
                else:
                    text += " "       
                text += "]"
        print(text+"\n")
        """
        i = 49
        j = 48
        k = 0
        text = "                  "
        for g in range(3):
            text += "["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i += 1
            text += "]"  

        i = 0
        text += "\n"
        for g in range(5):
            text += "                  ["
            if len(self.fields[j].pawns) > 0:
                    for pawn in self.fields[j].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            j -= 1
            text += "]["
            if len(self.goals[k].pawns) > 0:
                    for pawn in self.goals[k].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            k += 1
            text += "]["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i += 1
            text += "]\n" 

        j -= 5
        for g in range(6):
            text += "["
            if len(self.fields[j].pawns) > 0:
                    for pawn in self.fields[j].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            j += 1
            text += "]"

        text += "         "
        for g in range(6):
            text += "["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i += 1
            text += "]"

        j -= 7
        text += "\n["
        if len(self.fields[j].pawns) > 0:
            for pawn in self.fields[j].pawns:
                text += str(pawn.belongsTo.id)
        else:
                text += " "
        text += "]"
        k = 15
        for g in range(5):
            text += "["
            if len(self.goals[k].pawns) > 0:
                    for pawn in self.goals[k].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            k += 1
            text += "]"
        text += "         "
        k = 9
        for g in range(5):
            text += "["
            if len(self.goals[k].pawns) > 0:
                    for pawn in self.goals[k].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            k -= 1
            text += "]"
        text += "["
        if len(self.fields[i].pawns) > 0:
            for pawn in self.fields[i].pawns:
                text += str(pawn.belongsTo.id)
        else:
                text += " "
        text += "]\n"

        j -= 1
        i += 1

        for g in range(6):
            text += "["
            if len(self.fields[j].pawns) > 0:
                    for pawn in self.fields[j].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            j -= 1
            text += "]"

        text += "         "
        i += 5
        for g in range(6):
            text += "["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i -= 1
            text += "]"

        i += 7
        k = 14

        print(len(self.goals))
        text += "\n"
        for g in range(5):
            text += "                  ["
            if len(self.fields[j].pawns) > 0:
                    for pawn in self.fields[j].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            j -= 1
            text += "]["
            if len(self.goals[k].pawns) > 0:
                    for pawn in self.goals[k].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            k -= 1
            text += "]["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i += 1
            text += "]\n" 

        i = j
        text += "                  "
        for g in range(3):
            text += "["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i -= 1
            text += "]" 

        print(text)

if __name__ == "__main__":
    b = Board()

    b.play()

    #for player in b.players:
     #   print(f"Pieces in goals for {player.id}: {player.goaled}")
