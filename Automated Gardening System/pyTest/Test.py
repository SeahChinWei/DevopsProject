import ultrasonic
import ldr

def test_distance_below():
    result = ""
    test = 20
    distance = 4
    result = ultrasonic.distance_check(distance)

    assert( result == test)

def test_distance_above():
    result = ""
    test = 0
    distance = 15
    result = ultrasonic.distance_check(distance)

    assert (result == test)

def test_dim_light():
    result = ""
    test = 1
    light = 500
    result = ldr.light_checker(light)
    assert (result == test)

def test_bright_light():
    result = ""
    test = 0
    light = 1000
    result = ldr.light_checker(light)
    assert (result == test)