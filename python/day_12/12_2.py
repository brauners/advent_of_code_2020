
import math
#           N
#           y
#           |
#           |
#           |
# W ------------------- x E
#           |
#           |
#           |
#           S

def cart_to_pol(x, y):
    rho = math.sqrt(x**2 + y**2)
    phi = math.atan2(y, x)
    return(rho, math.degrees(phi))

def pol_to_cart(rho, phi):
    x = rho * math.cos(phi)
    y = rho * math.sin(phi)
    return(x, y)

def move_in_world(a, v, pos_ship, pos_waypoint):
    x, y = pos_ship
    wx, wy = pos_waypoint

    if a == "N":
        wx, wy = wx, wy + v
    
    elif a == "E":
        wx, wy = wx + v, wy
    
    elif a == "S":
        wx, wy = wx, wy - v
    
    elif a == "W":
        wx, wy = wx - v, wy
    
    elif a == "F":
        dx = wx - x
        dy = wy - y
        x = x + dx * v
        y = y + dy * v
        wx = x + dx
        wy = y + dy
    
    elif a == "R":
        # rotate the waypoint around the ship right
        rho, phi = cart_to_pol(wx - x, wy - y)
        phi = phi - v
        dx, dy = pol_to_cart(rho, math.radians(phi))
        wx = x + dx
        wy = y + dy

    elif a == "L":
        # rotate the waypoint around the ship left
        rho, phi = cart_to_pol(wx - x, wy - y)
        phi = phi + v
        dx, dy = pol_to_cart(rho, math.radians(phi))
        wx = x + dx
        wy = y + dy

    return (x, y), (wx, wy)

def manhattan(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return dx + dy


if __name__ == "__main__":
    with open("12.in") as f:
        input = [x.strip() for x in f.readlines()]

    start_pos_ship = (0, 0)
    pos_ship = start_pos_ship

    pos_waypoint = (10, 1)

    for i in input:
        d, v = i[0], int(i[1:])
        pos_ship, pos_waypoint = move_in_world(d, v, pos_ship, pos_waypoint)
 
    print(manhattan(start_pos_ship[0], start_pos_ship[1], pos_ship[0], pos_ship[1]))
