from player_list import PlayerList
from player import Player

zoe = Player(1,'Zoe')
luna = Player(2,'Luna')
alice = Player(3,'Alice')
prunsel = Player(4,'Prunsel')
wayne = Player(5,'Wayne')


my_list = PlayerList()

my_list.insert_at_head(zoe)
my_list.insert_at_head(luna)
my_list.insert_at_head(alice)
my_list.insert_at_tail(prunsel)
my_list.insert_at_tail(wayne)

my_list.iterate_over_list(True)
print("and backward")
my_list.iterate_over_list(False)
print("and lets delete")
my_list.pop_using_id(2)
my_list.iterate_over_list(True)
print("and backwards")
my_list.iterate_over_list(False)
print("and lets delete")
my_list.pop_at_tail()
my_list.iterate_over_list(True)
print("and again")
my_list.pop_at_head()
my_list.iterate_over_list(True)