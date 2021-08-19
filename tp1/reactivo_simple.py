import random
import time


def create_false_floor(floor_length, position):
    floor = list()
    for i in range(floor_length):
        if i == position:
            floor.append("A")
        else:
            floor.append(" ")
    return floor

def create_floor():
    floor = list()
    length = random.randint(10, 15)
    for i in range(length):
        floor.append(states[random.randint(0, 3)])
    return floor

def check_movement(floor_length, new_position):
    if new_position < 0 or new_position > floor_length-1:
        return False
    else:
        return True

def check_floor_state(floor, position):
    state = [k for k, v in states.items() if v == floor[position]]
    return state

def change_direction(direction):
    if direction == -1:
        direction = 1
    elif direction == 1:
        direction = -1
    return direction

def clean(floor, position):
    key = [k for k, v in states.items() if v == floor[position]]
    key = key[0]
    if key != 0 and key != 3:
        key = key - 1
    floor[position] = states[key]
    return floor

if __name__ == "__main__":
    states = {
        0: " ",
        1: "+",
        2: "*",
        3: "#"
    }
    directions = {
        0: -1,
        1: 1
    }
    floor = create_floor()
    position = random.randint(0, len(floor))
    false_floor = create_false_floor(len(floor), position)
    direction = directions[random.randint(0, 1)]
    total_moviments = 0
    movement_changes = 0
    while True:
        time.sleep(2)
        print("Floor:   ", floor)
        print("Position:", false_floor)
        print("Total moviments:", total_moviments)
        print("Movement changes:", movement_changes)
        state = check_floor_state(floor, position)
        print("State:", floor[position])
        print("Action: Cleaning")
        floor = clean(floor, position)
        if check_movement(len(floor), position + direction):
            print("Action: Moving")
            position = position + direction
            false_floor = create_false_floor(len(floor), position)
            total_moviments += 1
        else:
            print("You can not go in that direction, changing route...")
            direction = change_direction(direction)
            movement_changes += 1
            total_moviments += 1
