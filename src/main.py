from player_list import PlayerList
from player import Player

zoe = Player("1", 'Zoe')
luna = Player("2", 'Luna')
alice = Player("3", 'Alice')
prunsel = Player("4", 'Prunsel')
wayne = Player("5", 'Wayne')

my_list = PlayerList()

my_list.insert_at_head(zoe)
my_list.insert_at_head(luna)
my_list.insert_at_head(alice)
my_list.insert_at_tail(prunsel)
my_list.insert_at_tail(wayne)

my_list.display(True)
print("and backward")
my_list.display(False)
print("and lets delete")
my_list.pop_using_id(2)
my_list.display(True)
print("and backwards")
my_list.display(False)
print("and lets delete")
my_list.pop_at_tail()
my_list.display(True)
print("and again")
my_list.pop_at_head()
my_list.display(True)

zoe.score = 1
luna.score = 2
alice.score = 3
prunsel.score = 4
wayne.score = 5

standardList = [zoe, luna, alice, prunsel, wayne]

print(standardList[0].__str__())
print(standardList[4].__str__())

Player.bubble_sort(standardList)

print(standardList[0].__str__())
print(standardList[4].__str__())
