import FuncionDistanciaEntrePtos
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
                if FuncionDistanciaEntrePtos.distancia(x, y) < 10:
                    return (10)
                else:
                    return (100)
        else:
            if 25<x and y<10 or 25<x and 30<y:
                return (3)
            else:
                return (5)
