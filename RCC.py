def singly_reinforced():

    print('Design of a Singly Reinforced Concrete Beam using Limit state Design')

    def moment_calculation():
        M_mix = input(" Enter the strength of Concrete to be used (N/mm^2)")
        S_str = input("Enter the strength of Steel(N/mm^2) ")
        b = input("enter the breadth of the beam (mm) ")
        d = input("enter the depth of the beam (mm) ")
        l = input("Enter the span of the beam (mm):")

        if S_str == 415:
            x_max = 0.48 * int(S_str)
            print(" the maximum depth of neutral axis is:", x_max, "mm")
        else:
            if S_str == 250:
                x_max = 0.53 * int(S_str)
                print(" the maximum depth of neutral axis is:", x_max, "mm")
            else:
                x_max = 0.46 * int(S_str)
                print(" the maximum depth of neutral axis is:", x_max, "mm")

        print("the moment of resistance of the beam  is calculated as:")
        M = 0.36 * int(M_mix) * int(b) * int(x_max) * (int(d) - int(0.42 * x_max))
        print (M, "N/mm^2")

    def area_calculation():
        M_mix = input(" Enter the strength of Concrete to be used (N/mm^2)")
        S_str = input("Enter the strength of Steel(N/mm^2) ")
        b = input("enter the breadth of the beam (mm) ")
        d = input("enter the depth of the beam (mm) ")
        l = input("Enter the span of the beam (mm):")
        D_Load = input("Enter Dead load (N/mm^2):")
        L_Load = input("Enter live load (N/mm^2):")
        S_w = d * 25
        print("self weight of the beam:", S_w, "N/mm^2")

        M = ((int(D_Load) + int(L_Load)) * int(l) * int(l) + int(S_w)) / 8
        print("moment is", M, "N/mm^2")
        print("Factored moment = 1.5*moment = ", M * 1.5, "N/mm^2")

        if S_str == 415:
            x_max = 0.48 * int(S_str)
            print(" the maximum depth of neutral axis is:", x_max, "mm")
        else:
            if S_str == 250:
                x_max = 0.53 * int(S_str)
                print(" the maximum depth of neutral axis is:", x_max, "mm")
            else:
                x_max = 0.46 * int(S_str)
                print(" the maximum depth of neutral axis is:", x_max, "mm")

        print("the area of the steel required is calculated as:")

        print (M, "N/mm^2")

    def neutral_axis():
        d = input("diameter of the bars")
        n1 = input("number of diameter bars")
        Area = (3.14*d**2*n1)/4
        print("area of reinforcement steel: ",Area)
        f = input("Are there additional bars(Y/N)")
        if f == 5:
            d2 = input("enter the diameter of bar")
            n2 = input("number of bars")
            A= d2*n2
        else:
            print("")
    print(''' 
           1 > Moment of Resistance Calculation
           2 > Area of Reinforcement steel Calculation
           3 > Calculation of depth of neutral axis
    ''')
    answer = input(" Choose an option")

    if answer ==1:
        print("Moment Resistance Calculation")
        moment_calculation()
    elif answer == 2:
        print(" Area of Steel Computation:")
        area_calculation()
    elif answer == 3:
        print("Calculation of Neutral axis")
        neutral_axis()
    else:
        print("Invalid! Watch your fingers:")


print("RCC DESIGN CALCULATOR")

print('''

1. Singly Reinforced Beam
2.Doubly Reinforced Beam

''')

a = input("Choose an option:")
if a ==1:
    print('Welcome to Singly Reinforced beam design window')
    singly_reinforced()

elif a ==2:
    print('Welcome to Doubly Reinforced beam design window')
else:
    print("Invalid input,control your fingers")
