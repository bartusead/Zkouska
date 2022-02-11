from math import inf
def segments_intersection(p1,p2,p3,p4):
    
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    x4 = p4[0]
    y4 = p4[1]
            
    prvni_x = [x1,x2]
    druhy_x = [x3,x4]
    prvni_y = [y1,y2]
    druhy_y = [y3,y4]

    vect1x = x2-x1
    vect1y = y2-y1
    vect2x = x4-x3
    vect2y = y4-y3

    A1 = y2-y1
    B1 = x1-x2
    C1 = A1*x1+B1*y1

    A2 = y4-y3
    B2 = x3-x4
    C2 = A2*x3+B2*y3

    det = A1*B2 - A2*B1

    #ROVNOBĚŽNÉ!!!
    if det == 0:
        #NESVISLÉ
        if x1 != x2:
            z = (x3-x1)/(x2-x1)
            #Když jsou v jedné linii (ne svislé)
            if round(y1 + z*(y2-y1),9) == round(y3,9) and vect1y/vect1x == vect2y/vect2x:
                #ŽÁDNÝ PRŮSEČÍK
                #1. níž
                if max(prvni_x) < min(druhy_x):
                    print("Úsečky jsou ve stejné linii, ale neprotínají se")
                    return None
                #2. níž
                if max (druhy_x) < min(prvni_x):
                    print("Úsečky jsou ve stejné linii, ale neprotínají se")
                    return None
            
                #JEDEN PRŮSEČÍK
                #1. níž
                if max(druhy_x) > max(prvni_x) and min(druhy_x) == max(prvni_x):
                    if p2 == p3:
                        print("Úsečky jsou ve stejné linii a mají 1 průsečík BC")
                        return p2
                    if p2 == p4:
                        print("Úsečky jsou ve stejné linii a mají 1 průsečík BD")
                        return p2
                    if p1 == p3:
                        print("Úsečky jsou ve stejné linii a mají 1 průsečík AC")
                        return p1
                    if p1 == p4:
                        print("Úsečky jsou ve stejné linii a mají 1 průsečík AD")
                        return p1

                #2. níž
                if max(prvni_x) > max(druhy_x) and min(prvni_x) == max(druhy_x):
                    if p1 == p3:
                        print("Úsečky jsou ve stejné linii a mají 1 průsečík AC")
                        return p1
                    if p1 == p4:
                        print("Úsečky jsou ve stejné linii a mají 1 průsečík AD")
                        return p1
                    if p2 == p3:
                        print("Úsečky jsou ve stejné linii a mají 1 průsečík BC")
                        return p2
                    if p2 == p4:
                        print("Úsečky jsou ve stejné linii a mají 1 průsečík BD")
                        return p2
                #NEKONEČNĚ MNOHO PRŮSEČÍKŮ
                else:
                    print("Úsečky jsou ve stejné linii a průsečíkem je úsečka")
                    return inf

            #Když nejsou v jedné linii (ne svislé)
            else:
                print("Úsečky jsou rovnoběžné ostatní, ale neprotínají se")
                return None


        #SVISLÉ
        if x1 == x2:
            #Když jsou v jedné linii (svislé)
            if x1 == x2 == x3 == x4:
                #ŽÁDNÝ PRŮSEČÍK
                #1. níž
                if max(prvni_y) < min(druhy_y):
                    print("Úsečky jsou ve stejné linii, jsou svislé, ale neprotínají se")
                    return None
                #2. níž
                if max(druhy_y) < min (prvni_y):
                    print("Úsečky jsou ve stejné linii, jsou svislé, ale neprotínají se")
                    return None
        
                #JEDEN PRŮSEČÍK
                #1. níž
                if max(druhy_y) > max(prvni_y) and min(druhy_y) == max(prvni_y):
                    if p2 == p3:
                        print("Úsečky jsou rovnoběžné svislé a mají 1 průsečík BC")
                        return p2
                    if p2 == p4:
                        print("Úsečky jsou rovnoběžné svislé a mají 1 průsečík BD")
                        return p2
                    if p1 == p3:
                        print("Úsečky jsou rovnoběžné svislé a mají 1 průsečík AC")
                        return p1
                    if p1 == p4:
                        print("Úsečky jsou rovnoběžné svislé a mají 1 průsečík AD")
                        return p1

                #2. níž
                if max(prvni_y) > max(druhy_y) and min(prvni_y) == max(druhy_y):
                    if p1 == p3:
                        print("Úsečky jsou rovnoběžné svislé a mají 1 průsečík AC")
                        return p1
                    if p1 == p4:
                        print("Úsečky jsou rovnoběžné svislé a mají 1 průsečík AD")
                        return p1
                    if p2 == p3:
                        print("Úsečky jsou rovnoběžné svislé a mají 1 průsečík BC")
                        return p2
                    if p2 == p4:
                        print("Úsečky jsou rovnoběžné svislé a mají 1 průsečík BD")
                        return p2

                #NEKONEČNĚ MNOHO PRŮSEČÍKŮ
                else:
                    print("Úsečky jsou svislé a průsečíkem je úsečka")
                    return inf

            #Když nejsou v jedné linii (svislé)
            else:
                print("Úsečky jsou rovnoběžné, svislé, ale neprotínají se")
                return None



    #NEJSOU ROVNOBĚŽNÉ!!!     
    else:
        rx = (B2*C1 - B1*C2)/det
        ry = (A1*C2 - A2*C1)/det

        px = round(rx,9)
        py = round(ry,9)
        #print(px, py)

        #NESVISLÉ
        if x1 != x2 and x3 != x4:
            #JEDEN PRŮSEČÍK
            if min(prvni_x) <= px <= max(prvni_x) and min(druhy_x) <= px <= max(druhy_x):
                print(f"Úsečky jsou různoběžné a mají průsečík {px,py} ")
                return (px,py)
            #ŽÁDNÝ PRŮSEČÍK
            else:
                print("Úsečky jsou různoběžné, ale nemají žádný průsečík")
                return None
        
        #PRVNÍ SVISLÁ
        if x1 == x2:
            #JEDEN PRŮSEČÍK
            if min(prvni_y) <= py <= max(prvni_y) and min(druhy_x) <= px <= max(druhy_x):
                print(f"Úsečky jsou různoběžné, 1. je svislá a mají průsečík {px,py}")
                return (px,py)
            #ŽÁDNÝ PRŮSEČÍK
            else:
                print("Úsečky jsou různoběžné, 1. je svislá, ale nemají žádný průsečík")
                return None

        #DRUHÁ SVISLÁ
        if x3 == x4:
            #JEDEN PRŮSEČÍK
            if min(prvni_x) <= px <= max(prvni_x) and min(druhy_y) <= py <= max(druhy_y):
                print(f"Úsečky jsou různoběžné, 2. je svislá a mají průsečík {px,py}")
                return (px,py)
            #ŽÁDNÝ PRŮSEČÍK
            else:
                print("Úsečky jsou různoběžné, 2. je svislá, ale nemají žádný průsečík")
                return None




print(segments_intersection((0,0),(5,5),(4,4),(12,12)))


 





