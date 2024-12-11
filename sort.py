import math

def sort(width, height, length, mass) -> str:
    for x in [width, height, length, mass]:
        if not is_positive_number(x):
            return "REJECTED"
    
    try:
        w = float(width)
        h = float(height)
        l = float(length)
        m = float(mass)

        if any(math.isinf(x) for x in [w, h, l, m]):
            return "REJECTED"
    except:
        return "REJECTED"
    
    try:
        volume = w * h * l
        if volume != volume:
            return "REJECTED"
    except:
        return "REJECTED"
    
    volume_too_big = w * h * l >= 1000000
    size_too_big = w >= 150 or h >= 150 or l >= 150
    bulky = volume_too_big or size_too_big
    heavy = m >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    elif not bulky and not heavy:
        return "STANDARD"
    else:
        # this is probably not needed
        return "REJECTED"


def is_positive_number(x):
    try:
        return float(x) > 0
    except:
        return False