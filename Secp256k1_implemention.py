import random

def point_gen():
    for i in range(500):
        x = random.randint(0,263)
        z = (x**3 + 7) % 263
        y1 = pow(z, 66) % 263
        y2 = 263 - y1
        s1 = pow(y1, 2) % 263
        s2 = pow(y2, 2) % 263 
        if s1 == z:
            return x,y1
        elif s2 == z:
            return x,y2
        else:
            i = i + 1
    return 0, 0

def point_add(x_i, y_i, x_f, y_f):
    if x_i == 0 & y_i == 0:
        return x_f, y_f
    elif x_f == 0 & y_f == 0:
        return x_i, y_i
    else:
        m = ((y_f - y_i) % 263) * pow((x_f-x_i), 261, 263)
        ret_x = (m**2 - x_i - x_f) % 263
        ret_y = (m*(x_i - ret_x) - y_i) % 263
        return ret_x, ret_y

def point_double(x_i, y_i):
    m = ((3*(x_i ** 2)) % 263) * pow(2*y_i, 261, 263) 
    ret_x = (m ** 2 - x_i - x_i) % 263
    ret_y = (m*(x_i - ret_x) - y_i) % 263
    return ret_x, ret_y

def point_find():
    x,y = point_gen()
    if x == 0:
        return(print("Failure"))
    print("Point generated on our curve:", x, y)
    n = input("Enter the number we want to dot the point with itself(between 2 and 263):")
    n = int(n)
    n = list(bin(n)[2:])
    n.reverse()
    x_f = 0
    y_f = 0
    for i in n:
        if i == '1':
            x_f, y_f = point_add(x, y, x_f, y_f)
        x, y = point_double(x, y)
    z = (x_f**3 + 7) % 263
    s = pow(y_f, 2) % 263
    if s == z:
        return(print("Point found:", x_f, y_f))
    else:
        return(print("Does not exist on the curve"))

if __name__ == '__main__':
    point_find()
