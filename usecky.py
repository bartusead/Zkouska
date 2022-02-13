from math import inf
def segments_intersection(p1,p2,p3,p4):
    if p1 == p2 or p3 == p4:
        print("Segment can't have the same endpoints")  
        return None 
    x1,y1 = p1[0],p1[1]
    x2,y2 = p2[0],p2[1]
    x3,y3 = p3[0],p3[1]
    x4,y4 = p4[0],p4[1]

    first_x,first_y = [x1,x2],[y1,y2]
    second_x,second_y = [x3,x4],[y3,y4]

    vect1x,vect1y = x2-x1,y2-y1
    vect2x,vect2y = x4-x3,y4-y3

    A1 = y2-y1
    B1 = x1-x2
    C1 = A1*x1+B1*y1

    A2 = y4-y3
    B2 = x3-x4
    C2 = A2*x3+B2*y3

    det = A1*B2 - A2*B1

    #PARALLEL
    if det == 0:
        #NON-VERTICAL
        if x1 != x2:
            z = (x3-x1)/(x2-x1)
            #Collinear
            if round(y1 + z*(y2-y1),9) == round(y3,9):
                #NO INTERSECTION
                #1. left
                if max(first_x) < min(second_x):
                    print("Segments are collinear but don't intersect each other")
                    return None
                #2. left
                if max (second_x) < min(first_x):
                    print("Segments are collinear but don't intersect each other")
                    return None
            
                #ONE INTERSECTION
                #1. left
                if max(second_x) > max(first_x) and min(second_x) == max(first_x):
                    if p2 == p3:
                        print("Segments are collinear and intersect each other in one point p2;p3")
                        return p2
                    if p2 == p4:
                        print("Segments are collinear and intersect each other in one point p2;p4")
                        return p2
                    if p1 == p3:
                        print("Segments are collinear and intersect each other in one point p1;p3")
                        return p1
                    if p1 == p4:
                        print("Segments are collinear and intersect each other in one point p1;p4")
                        return p1

                #2. left
                if max(first_x) > max(second_x) and min(first_x) == max(second_x):
                    if p1 == p3:
                        print("Segments are collinear and intersect each other in one point p1;p3")
                        return p1
                    if p1 == p4:
                        print("Segments are collinear and intersect each other in one point p1;p4")
                        return p1
                    if p2 == p3:
                        print("Segments are collinear and intersect each other in one point p2;p3")
                        return p2
                    if p2 == p4:
                        print("Segments are collinear and intersect each other in one point p2;p4")
                        return p2
                #INFINITE INTERSECTIONS
                else:
                    print("Segments are collinear and their intersection is also a segment")
                    return inf

            #Non-collinear (but still parallel)
            else:
                print("Segments are parallel but non-collinear and thus they have no intersection")
                return None


        #VERTICAL
        if x1 == x2:
            #Collinear
            if x1 == x2 == x3 == x4:
                #NO INTERSECTION
                #1. down
                if max(first_y) < min(second_y):
                    print("Segments are collinear and vertical but they have no intersection")
                    return None
                #2. down
                if max(second_y) < min (first_y):
                    print("Segments are collinear and vertical but they have no intersection")
                    return None
        
                #ONE INTERSECTION
                #1. down
                if max(second_y) > max(first_y) and min(second_y) == max(first_y):
                    if p2 == p3:
                        print("Segments are collinear and vertical and intersect each other in one point p2;p3")
                        return p2
                    if p2 == p4:
                        print("Segments are collinear and vertical and intersect each other in one point p2;p4")
                        return p2
                    if p1 == p3:
                        print("Segments are collinear and vertical and intersect each other in one point p1;p3")
                        return p1
                    if p1 == p4:
                        print("Segments are collinear and vertical and intersect each other in one point p1;p4")
                        return p1

                #2. down
                if max(first_y) > max(second_y) and min(first_y) == max(second_y):
                    if p1 == p3:
                        print("Segments are collinear and vertical and intersect each other in one point p1;p3")
                        return p1
                    if p1 == p4:
                        print("Segments are collinear and vertical and intersect each other in one point p1;p4")
                        return p1
                    if p2 == p3:
                        print("Segments are collinear and vertical and intersect each other in one point p2;p3")
                        return p2
                    if p2 == p4:
                        print("Segments are collinear and vertical and intersect each other in one point p2;p4")
                        return p2

                #INFINITE INTERSECTIONS
                else:
                    print("Segments are collinear and vertical and their intersection is also a segment")
                    return inf

            #Non-collinear (but still parallel)
            else:
                print("Segments are parallel and verical but non-collinear and thus they have no intersection")
                return None

    #DIVERGENT    
    else:
        rx = (B2*C1 - B1*C2)/det
        ry = (A1*C2 - A2*C1)/det

        px = round(rx,9)
        py = round(ry,9)

        #NON-VERTICAL
        if x1 != x2 and x3 != x4:
            #ONE INTERSECTION
            if min(first_x) <= px <= max(first_x) and min(second_x) <= px <= max(second_x):
                print(f"Segments are divergent and they intersect each other in one point {px,py} ")
                return (px,py)
            #NO INTERSECTION
            else:
                print("Segments are divergent but they have no intersection")
                return None
        
        #FIRST VERICAL
        if x1 == x2:
            #ONE INTERSECTION
            if min(first_y) <= py <= max(first_y) and min(second_x) <= px <= max(second_x):
                print(f"Segments are divergent, 1. is vertical and they intersect each other in one point {px,py}")
                return (px,py)
            #NO INTERSECTION
            else:
                print("Segments are divergent, 1. is vertical, but they have no intersection")
                return None

        #SECOND VERTICAL
        if x3 == x4:
            #ONE INTERSECTION
            if min(first_x) <= px <= max(first_x) and min(second_y) <= py <= max(second_y):
                print(f"Segments are divergent, 2. is vertical and they intersect each other in one point {px,py}")
                return (px,py)
            #NO INTERSECTION
            else:
                print("Segments are divergent, 2. is vertical, but they have no intersection")
                return None




print(segments_intersection((0,0),(10,0),(0,0),(5,0)))


 





