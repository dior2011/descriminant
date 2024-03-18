import math
def descriminant(a,b,c):
    d = (b**2) - (4*a*c)
    if d == abs(d):
        x1 = ((-b - math.sqrt(d)) / (2 * a))
        x2 = ((-b + math.sqrt(d)) / (2 * a))
        
        if int((a*(x1**2))+(x1*b)+c) == 0:    
            if int((a*(x2**2))+(x2*b)+c) == 0:
                return f"D = {d}\nx1 = {x1}\nx2 = {x2}"

        if int((a*(x1**2))+(x1*b)+c) != 0:
            if int((a*(x2**2))+(x2*b)+c) == 0:
                return f"D = {d}\nx2 = {x2}"
            

        if int((a*(x1**2))+(x1*b)+c) == 0:
            if int((a*(x2**2))+(x2*b)+c) != 0:  
                return f"D = {d}\nx2 = {x2}"
        
    else:
        return f"D = {d}\nTenglama yechimli emas!"
        
print(descriminant(4,9,2))