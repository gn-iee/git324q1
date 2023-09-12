def initial_state():
    return (0, 0, 0)

def is_goal(s):
    return True

def successors(s):
    x, y, z = s
    
    #Try to empty bottle
    if x>0:
        yield((0,y,z),x)
    if y>0:
        yield((x,0,z),y)
    if z>0:
        yield((x,y,0),z)
    
    #Try to fill up
    if x<8:
        yield((8,y,z),8-x)
    if y<5:
        yield((x,5,z),5-y)
    if z<3:
        yield((x,y,3),3-z)  
                
    #Try to pour 8L to 5L
    t = 5-y
    if x>0 and t>0:
        if x>t:
            yield((x-t,5,z),t)
        else:
            yield((0,y+x,z),x)
            
    #Try to pour 8L to 3L
    t = 3-z
    if x>0 and t>0:
        if x>t:
            yield((x-t,y,3),t)
        else:
            yield((0,y,z+x),x)
            
    #Try to pour 5L to 8L
    t = 8-x        
    if y>0 and t>0:
        if y>t:
            yield((x+t,y-t,z),t)
        else:
            yield((x+y,0,z),y)
    
    #Try to pour 5L to 3L
    t = 3-z
    if y>0 and t>0:
        if y>t:
            yield((x,y-t,3),t)
        else:
            yield((x,0,z+y),y)
    
    #Try to pour 3L to 8L
    t = 8-x
    if z>0 and t>0:
        if z>t:
            yield((8,y,z-t),t)
        else:
            yield((x+z,y,0),z)
            
    #Try to pour 3L to 5L
    t = 5-y
    if z>0 and t>0:
        if z>t:
            yield((x,5,z-t),t)
        else:
            yield((x,y+z,0),z)
