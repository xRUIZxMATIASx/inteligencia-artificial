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

def random_dirt(floor):
    num = random.randint(0, 1)
    if num:
        floor[random.randint(0, len(floor)-1)] = states[random.randint(0, 3)]
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
    position = 0
    false_floor = create_false_floor(len(floor), position)
    direction = directions[1]
    total_moviments = 0
    movement_changes = 0

    history_of_positions = list()
    for i in range(len(floor)):
        history_of_positions.append(0)

    position_on_the_ground = 0

    max_clean = 20

    while True:
        #time.sleep(2)
        floor = random_dirt(floor)
        print("Floor:   ", floor)
        print("Position:", false_floor)
        print("History: ", history_of_positions)
        print("Total moviments:", total_moviments)
        print("Movement changes:", movement_changes)
        state = check_floor_state(floor, position)
        print("State:", floor[position])
        if state[0] > 0 and history_of_positions[position_on_the_ground] < max_clean:
            print("Action: Cleaning")
            floor = clean(floor, position)
            history_of_positions[position_on_the_ground] += 1
            state = check_floor_state(floor, position)
            if state[0] > 0:
                continue
        else:
            print("Action: Already clean")

        if check_movement(len(floor), position + direction):
            print("Action: Moving")
            position = position + direction
            false_floor = create_false_floor(len(floor), position)
            total_moviments += 1
            if direction == 1:
                position_on_the_ground += 1
            else:
                position_on_the_ground -= 1
        else:
            print("Can not go in that direction, changing route...")
            direction = change_direction(direction)
            movement_changes += 1
            total_moviments += 1

        keep_cleaning = False
        for cleaning_counter in history_of_positions:
            if cleaning_counter < max_clean:
                keep_cleaning = True

        if keep_cleaning:
            continue
        else:
            print("Floor:   ", floor)
            print("Position:", false_floor)
            #print("History: ", history_of_positions)
            print("Total moviments:", total_moviments)
            print("Movement changes:", movement_changes)
            state = check_floor_state(floor, position)
            print("State:", floor[position])
            print("Close program")
            break