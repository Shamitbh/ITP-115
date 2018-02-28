# play the actual game

from Ranged import Ranged
from ZoomRanged import ZoomRanged

def main():
    p = Ranged("Peach Grenade", 100, 3)
    y = ZoomRanged("Yoshi Egg Shooter", 200, 10)
    m = Ranged("Mario Flower Fireballs", 50, 20)

    # make a list of Weapons
    armory = [p, y, m]

    for item in armory:
        print(item)

    for item in armory:
        item.use()





    # print("The name of this weapon is ", p.getName())
    # p.use()
    # p.use()
    # p.use()
    # p.use()



main()