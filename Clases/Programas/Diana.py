'''def diana (x,y):
    if x<5 and y<10 or x<5 and 30<y:
        return (3)
    else:
            return (5)
        
    if 5 <= x and x <= 25 and y < 10 or 5 <= x and x <= 25 and 30 < y:
            return (7)
    else:
            return (10)

    if 25<x and y<10 or 25<x and 30<y:
            return (3)
    else:
            return (5)

            Hubo que anidar los ciclos if/else'''
    
def diana (x, y):
    if x<5:
        if y<10 or 30<y:
            return (3)
        else:
            return (5)
    else:
        if 5 <= x and x <= 25:
            if y<10 or 30<y:
                return (7)
            else:
                return (10)
        else:
            if 25<x and y<10 or 25<x and 30<y:
                return (3)
            else:
                return (5)

        
