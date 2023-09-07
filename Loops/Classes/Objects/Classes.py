class  student:
    def __init__(self,f_name,l_name):
        self.first_name = f_name,
        self.last_name = l_name

class  game_player:
    def __init__(self,name,ranking,level):
        self.player_name = name,
        self.ranking = ranking,
        self.level = level

    def print_pretty(self):
        print(str(self.player_name).upper())



game_player1= game_player("shayan qureshi",10,"pro")
game_player2= game_player("rizwan qureshi",1,"god")
game_player2.print_pretty()

# print(game_player2.player_name)


student_1 = student("john","hopkin")
student_2 = student("bill", "gates")
student_3 = student("rizwan", "qureshi")

students = [student_1,student_2,student_3]

for i in range(len(students)):
    print(students[i].last_name)
