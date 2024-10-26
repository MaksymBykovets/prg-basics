def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return n*0.3937

def feet_to_cm(f, i):
    cm_foot = f*30.48
    cm_inch = i*0.3937
    return cm_foot+cm_inch


if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f"100cm = {cm_to_inch(100)}inch")
    print(f"3 ft 9 inch = {feet_to_cm(3, 9)}")

