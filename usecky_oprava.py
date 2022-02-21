from math import inf

def vector_cross(u,v):
    u1,u2 = u[0],u[1]
    v1,v2 = v[0],v[1]    
    cross_product = u1*v2 - u2*v1
    return cross_product

def vector_dot(r,s):
    r1,r2 = r[0],r[1]
    s1,s2 = s[0],s[1]
    dot_product = r1*s1 + r2*s2
    return dot_product

def vector_from_points(p1,p2):
    u1 = p2[0]-p1[0]
    u2 = p2[1]-p1[1]
    return u1,u2

def intersection_point(p1,k,r):
    p1x,p1y = p1[0],p1[1]
    rx,ry = r[0],r[1]
    point = (p1x + k*rx,p1y + k*ry)
    return point

def segments_intersection(p1,p2,p3,p4):
    vector1, vector2 = vector_from_points(p1,p2), vector_from_points(p3,p4)
    cross_product = vector_cross(vector1,vector2)
    vector3 = vector_from_points(p1,p3)
    cross_product_points = vector_cross(vector3,vector1)
    
    if cross_product == 0:
        #Collinear
        if cross_product_points == 0:
            print("The segments are collinear")
            t0 = vector_dot(vector3,vector1)/vector_dot(vector1,vector1)
            t1 = t0 + (vector_dot(vector2,vector1)/vector_dot(vector1,vector1))
            #No intersection point
            if (t0 > 1 and t1 > 1) or (t0 < 0 and t1 < 0):
                return None
            #One intersection point
            elif (t0 == 1 and t1 > 1) or (t0 == 0 and t1 < 0) or (t1 == 1 and t0 > 1) or (t1 == 0 and t0 < 0):
                if p1 == p3 or p1 == p4:
                    return p1
                elif p2 == p3 or p2 == p4:
                    return p2
            #Infinite intersection points
            return inf
        #Parallel
        print("The segments are parallel")
        return None

    #Divergent
    #print("The segments are divergent")
    t = vector_cross(vector3,vector2)/vector_cross(vector1,vector2)
    u = vector_cross(vector3,vector1)/vector_cross(vector1,vector2)
    if 0 <= t <= 1 and 0 <= u <= 1:
        point = intersection_point(p1,t,vector1)  
        return point
    return None



#print(segments_intersection((-724863.38,-1058692.18),(-724788.88,-1058709.10),(-724823.03,-1058700.60),(-724822.45,-1058706.17)))