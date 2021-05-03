import random as rn



def result():
    doors = ["lambo", "goat", "sheep"]
    unmodified_doors = doors
    # radnomise doors

    rn.shuffle(doors)

    # randomly select a door

    choice = rn.choice(doors)

    doors.remove(choice)
    # open a door



    cont = True
    i = 0
    door_to_reveal = ""

    for z in doors:
        if doors.index(z) == choice:
            i += 1
            continue
        elif z == "lambo":
            i += 1
            continue
        else:
            door_to_reveal = z
    doors.remove(door_to_reveal)


    outcome = ""

    # decide to make our second choice
    decide_to_change = bool(rn.getrandbits(1))
    if decide_to_change:
        if doors[0] == "lambo":
            outcome = "win"
        else:
            outcome = "loss"
    else:
        if doors[0] == "lambo":
            outcome = "win"
        else:
            outcome = "loss"

    if outcome == "win":
        return True
    else:
        return False






    # while cont and i <=2:
    #     if i == choice:
    #         i += 1
    #         continue
    #     elif doors[i] == "lambo":
    #         i += 1
    #         continue
    #     else:
    #         door_to_reveal = i
    #         cont = False
    #         break


