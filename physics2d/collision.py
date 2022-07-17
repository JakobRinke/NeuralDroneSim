

def colldide(o1, o2):
    if o1.type == "rect" and o2.type == "rect":
        return rects_collide(o1, o2)
    elif o1.type == "circle" and o2.type == "circle":
        return spheres_collide(o1, o2)
    elif o1.type == "rect" and o2.type == "circle":
        return sphere_collide_rect(o2, o1)
    elif o2.type == "rect" and o1.type == "circle":
        return sphere_collide_rect(o1, o2)

def rects_collide(r1, r2):
    l1 = r1.pos - r1.param2/2
    l2 = r2.pos - r2.param2/2
    return (l1.x <= l2.x + r2.param2.x and
            l1.x + r1.param2.x >= l2.x and
            l1.y <= l2.y + r2.param2.y and
            r1.param2.y + l1.y >= l2.y)

def spheres_collide(s1, s2):
    return (s1.pos-s2.pos).length() <= s1.param2 + s2.param2

def sphere_collide_rect(s, r):
    v = s.pos-r.pos
    v2 = v.normalize() * min(v.length, s.param2)
    return r.in_bounds(v2)