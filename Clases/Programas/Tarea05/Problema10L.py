# -*- coding: utf-8 -*-
def diasasueto(x):
    L=['1 de enero', '4 de febrero', '18 de marzo', '18 de abril', '19 de abril', '1 mayo',
       'No hay días de asueto oficiales en este mes', '16 de septiembre', '18 de noviembre', '25 de diciembre']
    ene, feb, mar, abr1, abr2, may, no, sep, nov, dic = L  
    if x=='enero':
        return ene
    else:
        if x == 'febrero':
            return feb
        else:
            if x == 'marzo':
                return mar
            else:
                if x == 'abril':
                    return abr1 + ' y ' + abr2
                else:
                    if x == 'mayo':
                        return may
                    else:
                        if x == 'junio':
                            return no
                        else:
                            if x == 'julio':
                                return no
                            else:
                                if x == 'agosto':
                                    return no
                                else:
                                    if x == 'septiembre':
                                        return sep
                                    else:
                                        if x == 'octubre':
                                            return no
                                        else:
                                            if x == 'noviembre':
                                                return nov
                                            else:
                                                return dic
                                                
            
