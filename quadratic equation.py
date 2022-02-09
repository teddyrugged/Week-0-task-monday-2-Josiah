""" solvinging with quadratic formular considering a zero division """

def quadraticSolver(a,b,c):
    #using the quadractic equation {(b+or-(b**2 - 4as))/2*a}
    if a == 0:
        return (f"it cannot be divided by {a}")
    d = ((b**2) - (4*a*c))**0.5
    return f"{(-b + (d))/(2*a)} andy {(-b - (d))/(2*a)}"

    #return invalid
        
print(quadraticSolver(1,-3,-10))