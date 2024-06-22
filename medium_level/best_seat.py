# best solution with O(n) space and O(1) time

def bestSeat(seats):
    n = len(seats)
    if n == 1:
        return -1 # first and last always occupied
    best_seat = (-1, -1, -1)
    for seat_index in range(n):
        seat_space, left_spaces, right_spaces = computeSpaces(seats, seat_index, n)
        best_space = best_seat[1] + best_seat[2]
        print('seat_space',seat_space)
        print('best', best_space)
        if seat_space >= best_space:
            if seat_space > best_space:
                best_seat = (seat_index, left_spaces, right_spaces)
            else:
                # better distribution of space around the seat
                if abs(left_spaces - right_spaces) < abs(best_seat[1] - best_seat[2]):
                    best_seat = (seat_index, left_spaces, right_spaces)
    if best_seat[1] + best_seat[2] == -2: # no seat available in the row
        return -1
    return best_seat[0]

def computeSpaces(seats, seat_index, n):
    if seat_index == 0:
        return -1, -1, -1 # first always occupied
    elif seats[seat_index] == 1:
        return -1, -1, -1 # seat is not available
    else:
        left_spaces, right_spaces = 0, 0
        left_index, right_index = seat_index-1, seat_index+1
        # compute spaces to the left
        while left_index > -1 and seats[left_index] != 1:
            left_spaces += 1
            left_index -= 1
        # ditto for right spaces
        while right_index < n and seats[right_index] != 1:
            right_spaces += 1
            right_index += 1
        return left_spaces + right_spaces, left_spaces, right_spaces
