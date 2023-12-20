import math
from scipy.optimize import fsolve
import pandas as pd
import xlrd


def Capacity_of_Bolt():
    print('''                      ****Capacity of Bolt****
    
            1> Shear
    
            ''')
    d = input("what is the diameter of the bolt\t")
    na = input("Enter the number of shear planes with threads intercepting the shear plane\t")
    ns = input("Enter the number of shear planes without threads intercepting the shear plane\t")
    Asb = (3.14 * d * d) / 4
    Anb = 0.78 * Asb
    Vdsb = 400 * ((na * Anb) + (ns * Asb)) / (1.732 * 1.25)
    print "Shear Capacity of bolt: ", format(Vdsb,".3f")

    print('''
                    2> Bearing Capacity
        ''')
    t = input("Enter summation of the thickness of the connected plates experiencing...\t \t")
    Vdpb = (2.5 * 1 * d * t * 400) / 1.25
    print("Bearing Capacity of bolt=",Vdpb)
    Capacity = min(Vdpb, Vdsb)
    print "The Capacity of the bolt is:  ", format(Capacity,".3f")
    Number = Tu / Capacity
    if Number < 1:
        Number = 2
        print "The number of Bolt Required is: ", format(Number,".3f")
    else:
        
        print("The number of Bolt Required is: ", format(Number,".3f"))
     
    


def Tension():

    import pandas as pd
    import time
   



    print('''
                 Approximate Gross Area of the Tension Member from the gross yielding criteria
            ''')
    Areq = (Tu * 1.1) / 250
    Area = 1.3 * Areq
    print "the required area of the section in (cm^2 ):      ", format(Area/100,".3f")

    print("Choose the section from the table (from IS 808:1989) \n")
    df = pd.read_excel('C:\Users\umesh\Desktop\MC.xlsx', sheet_name='Sheet6')
    
    print(df)
    t = input("Choose the corresponding row number for suitable angle section:   ")
    print("Assuming longer leg is connected")
    L1 = df.iloc[t, 0]
    print "length of the connected leg = ", format(L1,".3f")
    L2 = df.iloc[t, 2]
    print "length of outstanding leg = ", format(L2,".3f")
    t = df.iloc[t, 4]
    print "width of the section =", format(t,".3f")
    Capacity_of_Bolt()

    print('''
                             CHECK     
              ''')

    d = input("Enter the Diameter of bolt \t")
    Ag = (L1 - t / 2) * t + (L2 - t / 2) * t
    print "The gross area of the section is:", format(Ag,".3f")
    Tdg = (Ag * 250) / 1.10
    print "The design strength of members under axial tension: ", format(Tdg,".3f")

    print('''
                       ****Design Strength Due to Rupture of Critical Section (For Single Angles)****
            ''')
    print("BOlt Arrangement in the angle \n")
    R = input("In how many rows are bolts placed \t")
    C = input("In how many Columbs are the bolts placed \t")
    P = input("Enter the pitch (>40)\t")
    CL = input("Enter the end distance (>30)\t")
    L3 = L2 + CL + (R - 1) * P
    bs =  L3 - t
    Lc = CL+ (C - 1) * P
    B = 1.4 - 0.076 * (L2 / t) * (250.0/ 410.0) * (bs / Lc)
    print "Beta = ", format(B,".3f")
    if B <= (410.0 * 1.10) / (250.0 * 1.25) and B >= 0.7:
        print("The value of BETA lies within range\t")
        ago = (L2 - t / 2) * t
        anc = (L1 - t / 2 - (d + 2))*t
        Tn = ((0.9 * anc * 410) / 1.25) + ((B * ago * 250) / 1.1)
        print "Design strength governed by rupture at net Section is : ", format(Tn,".3f")
    else:
        print("The value of BETA lies out of Range\n")

    print('''
                            ****Design Strength Due to Block Shear****
           ''')
    avg = (CL + (C - 1) * P) * t
    avn = (CL + (C - 1) * P - (C - 1) * (d + 2) - (d + 2) / 2) * t
    atg = ((R - 1) * P + CL) * t
    atn = (((R - 1) * P + CL) - (d + 2) / 2) * t
    Tdb1 = ((avg * 250) / (1.732 * 1.1)) + ((0.9 * atn * 410) / (1.25))
    Tdb2 = ((0.9 * avn * 410) / (1.732 * 1.25)) + ((atg * 250) / (1.10))
    Tdb = min(Tdb1, Tdb2)
    print "Strength goverened by block shear: ", format(Tdb,".3f")
    Ds = min(Tdg, Tn, Tdb)
    print "The Design strength is:  ", format(Ds,".3f")
    if Ds > Tu:
        print("the section is safe \t")
    else:
        print("the section is not safe\t\n")
        
    time.sleep(60)




def Compression_Member():
    import pandas as pd
    import time
    
    

    print('''
                                 ***Compression Member Design***
                      
        ''')

    fcd = input("Assume a suitable value for fcd varying between 125 N/mm^2 to 175 N/mm^2 \t")
    print "The value of design compressive strength is assumed as: ", fcd
    Area = (Tu / fcd)/2
    print "Area of the section is:", format(Area,".3f")
    print("In cm^2 Area = ", Area/100)
    print("Choose the suitable section from the table below:\n \n")

    df = pd.read_excel('C:\Users\umesh\Desktop\MC.xlsx', sheet_name = 'Sheet1')
    print (df)
    print("   ")

    CC = input("enter the corrsponding row number for your selection")
    S = df.iloc[CC, 0]
    print "The selected section is:", S
    A = (df.iloc[CC, 2]) * 100
    print 'Area of the section (A) = ', A
    D = df.iloc[CC, 3]
    print 'Depth of the section (D) = ', D
    B = df.iloc[CC, 4]
    print 'Width of the section(B) = ', B
    t = df.iloc[CC, 5]
    print 'Thickness (t) =  ', t
    Cy = df.iloc[CC, 6] * 10
    print "Centroidal distance is (Cy) = ", Cy
    Ix = (df.iloc[CC, 7]) * 10000
    print "Moment of Inertia along x-x axis (Ix) = ", Ix
    Iy = (df.iloc[CC, 8]) * 10000
    print 'The moment of Inertia is along y-y axis, (Iy) =  ', Iy
    rx = (df.iloc[CC, 9]) * 10
    print 'Radius of Gyration along x-axis (rx)= ', rx
    ry = (df.iloc[CC, 10]) * 10
    print 'Radius of Gyration along y-axis (ry)=  ', ry

    def f(d):
        return 2 * (Iy + A * ((B + d / 2 - Cy) ** 2)) - 2 * Ix

    d0 = 1
    d = fsolve(f, d0)
    print ("d = ", d)
    d = int(d) + 5
    print("Increasing d by 5: d =", d)
    Iyy = 2 * (Iy + A * ((B + d / 2 - Cy) ** 2))
    Ixx = 2 * Ix
    print "Iy = ", format(Iyy, ".3f")
    print "Ix = ", format(Ixx, ".3f")
    Imin = min(Ixx, Iyy)
    rmin = pow((Imin / (2 * A)), 0.5)
    print ' Rmin = ', format(rmin,".3f")

    l = input("enter the length of built up section")
    print("Effective Length Calculation")
    leffective = pd.read_excel('C:\Users\umesh\Desktop\MC.xlsx', sheet_name='Sheet4')
    print(leffective)
    l1 = input("Choose ( 2 to 7)  from above table :")
    if l1 == 2 or 3:
        leff = 2.0 * l
    if l1 == 4:
        leff = 1.0*l
    if l1 == 5:
        leff = 1.2*l
    if l1 == 6:
        leff = 0.8*l
    if l1 == 7:
        leff = 0.65*l
    else:
        print("Invalid Selection")
    lam = 1.05 * (leff / rmin)
    print "the slenderness ratio is: ", lam

    dd = pd.read_excel('C:\Users\umesh\Desktop\MC.xlsx', sheet_name='Table9c')
    dd_cols = ['slender_Ratio', '250']
    dd.columns = dd_cols
    print(dd)
    #for i in dd.iloc[:, 0]:
        #if i == lam:
            #print i

    print("Taking fy = 250")
    l1 = input("enter the row number for the lower value of the slenderness ratio ")
    l2 = l1 + 1
    fcd2 = dd.iloc[l1, 1] - ((dd.iloc[l1, 1] - dd.iloc[l2, 1]) / 10) * (lam - dd.iloc[l1, 0])
    print "fcd = ", fcd2
    pd = (fcd2 * 2 * A)
    print "the design strength is: ", pd
    if pd > Tu:
        print("the section is safe")
    else:
        print("not safe\n")


    print("LACING DESIGN")
    print("  ")
    angle = input("Select the angle of Lacing from 40 to 70 degree: ")
    p = (B - Cy + d / 2) * 2
    print "Distance between the centroidal axis of two channels is: ", format(p,".3f")
    b = p * math.tan(math.radians(angle))
    a1 = 2 * b
    Spacing = a1 / min(rx, ry)
    if Spacing >= 50 and Spacing >= 0.7 * lam:
        print("Spacing does not lies within the limit")
    else:
        print "Spacing = ", Spacing
    length = p / math.sin(math.radians(angle))
    print "The length of the lacing=", length
    db = input("Assume the diameter of the bolt (12,14,16,18) ")
    print "Width of the lacing is", 3 * db
    print('''Choose an option:
              1> single lacing
              2> Double lacing    
          ''')
    answer = input("Choose an option")
    if answer == 1:
        t = length / 40 + 4
        print "thickness of lacing = ", t
        f = (2.5 * Tu) / (100 * 2 * math.sin(math.radians(angle)))
        print "the value of f is: ", format(f,".3f")
    else:
        t = (length / 60) + 4
        print "thickness of lacing = ",format(t,".3f")
        f = (2.5 * Tu) / (100 * 4 * math.sin(math.radians(angle)))
        print "the value of f is: ", format(f,".3f")

    rmin_lacing = t / math.sqrt(12)
    print "Rmin for lacing = ", format(rmin_lacing,".3f")
    lam_lac = length / rmin_lacing
    print "Slenderness ratio for the lacing is: ", lam_lac
    print(dd)
    print("from above table, choose the corresponding row number:")
    ll1 = input("Enter the row number corresponding to lower value of slenderness ratio")
    ll2 = ll1 + 1

    fcd_lacing = dd.iloc[ll1, 1] - (dd.iloc[ll1, 1] - dd.iloc[ll2, 1]) / 10 * (
           lam_lac - dd.iloc[ll1, 0])
    print "the fcd for lacing = ", format(fcd_lacing,".3f")
    f_lacing = fcd_lacing * t * 3 * db
    print "the force: ", format(f_lacing, ".3f")
    if f_lacing > f:
        print("the section is safe")
    else:
        print("not safe\n")

    print("  ")


    print('''                      ****Capacity of Bolt****

               1> Shear

               ''')
    d = input("what is the diameter of the bolt\t")
    na = input("Enter the number of shear planes with threads intercepting the shear plane\t")
    ns = input("Enter the number of shear planes without threads intercepting the shear plane\t")
    Asb = (3.14 * d * d) / 4
    Anb = 0.78 * Asb
    Vdsb = 400 * ((na * Anb) + (ns * Asb)) / (1.732 * 1.25)
    print "Shear Capacity of bolt: ", format(Vdsb, ".3f")

    print('''
                       2> Bearing Capacity
           ''')
    t = input("Enter summation of the thickness of the connected plates experiencing...\t \t")
    Vdpb = (2.5 * 1 * d * t * 400) / 1.25
    print("Bearing Capacity of bolt=", Vdpb)
    Capacity = min(Vdpb, Vdsb)
    print "The Capacity of the bolt is:  ", format(Capacity, ".3f")
    Number = f / Capacity
    if Number < 1:
        Number = 2
        print "The number of Bolt Required is: ", format(Number,".3f")
    else:
        
        print("The number of Bolt Required is: ", format(Number,".3f"))
    time.sleep(60)

def Tension_Analytical():
    print('''
                             ****Design Strength Due to Yielding of Gross Section****

                ''')
    import pandas as pd
    import xlrd
    import time
    print('''
                              ****Design of a Tension Member of Steel Structure using Limit state Design****
                  ''')
    print('''
                     Approximate Gross Area of the Tension Member from the gross yielding criteria
                ''')

    print("Choose the section from the table (from IS 808:1989) \n")
    df = pd.read_excel('C:\Users\umesh\Desktop\MC.xlsx', sheet_name='Sheet6')

    print(df)
    t1 = input("Choose the corresponding row number for suitable angle section:   ")

    var = input("Which leg is connected (1> Longer / 2> Shorter)")
    if var == 1:
        L1 = df.iloc[t1, 0]
        print "length of the connected leg = ", format(L1,".3f")
        L2 = df.iloc[t1, 2]
        print "length of outstanding leg = ", format(L2,".3f")
    elif var == 2:
        L2 = df.iloc[t1, 0]
        print "length of the connected leg = ", format(L2,".3f")
        L1 = df.iloc[t1, 2]
        print "length of outstanding leg = ", format(L1,".3f")
    else:
        print("Invalid Selection")

    t = df.iloc[t1, 4]
    print "width of the section =", format(t,".3f")

    print('''
                                 CHECK     
                  ''')

    d = input("Enter the Diameter of bolt \t")
    Ag = (L1 - t / 2) * t + (L2 - t / 2) * t
    print "The gross area of the section is:", format(Ag,".3f")
    Tdg = (Ag * 250) / 1.10
    print "The design strength of members under axial tension: ", format(Tdg,".3f")

    print('''
                           ****Design Strength Due to Rupture of Critical Section (For Single Angles)****
                ''')
    print("BOlt Arrangement in the angle \n")
    R = input("In how many rows are bolts placed \t")
    C = input("In how many Columbs are the bolts placed \t")
    P = input("Enter the pitch (>40)\t")
    CL = input("Enter the end distance (>30)\t")
    L3 = L2 + CL + (R - 1) * P
    bs = L3 - t
    Lc = CL+(C - 1) * P
    B = 1.4 - (0.076 * (L2 / t) * (250.0 / 410.0) * (bs/ Lc))
    print 'Beta = ',format(B,".3f")
    if B <= (410 * 1.10) / (250 * 1.25) and B >= 0.7:
        print("The value of BETA lies within range\t")
        ago = (L2 - t / 2) * t
        anc = (L1 - t / 2 - (d + 2))*t
        Tdn = ((0.9 * anc * 410) / 1.25) + ((float(B) * ago * 250) / 1.1)
        print "Design strength governed by rupture at net Section is : ", format(Tdn,".3f")
    else:
        print("The value of BETA lies of Range\n")

    print('''
                                ****Design Strength Due to Block Shear****
               ''')
    avg = (CL + (C - 1) * P) * t
    avn = (CL + (C - 1) * P - (C - 1) * (d + 2) - (d + 2) / 2) * t
    atg = ((R - 1) * P + CL) * t
    atn = (((R - 1) * P + CL) - (d + 2) / 2) * t
    Tdb1 = ((avg * 250) / (1.732 * 1.1)) + ((0.9 * atn * 410) / (1.25))
    Tdb2 = ((0.9 * avn * 410) / (1.732 * 1.25)) + ((atg * 250) / (1.10))
    Tdb = min(Tdb1, Tdb2)
    print "Strength goverened by block shear: ", format(Tdb,".3f")
    Ds = min(Tdb, Tdn, Tdg)
    print "The Design strength is:  ", format(Ds,".3f")
    if Ds > Tu:
        print("the section is safe \t")
    else:
        print("the section is not safe\t")
    Capacity_of_Bolt()
    time.sleep(60)
    
    
print('''                                        
                                      ***WELCOME***
                                 STEEL DESIGN CALCULATOR
      
      ''')



print('''
          NOTE: ALL DIMENSIONS ARE IN MM AND FORCE IN NEWTON
          DESIGN PER IS CODE (IS 800:2007 and IS 808:1989)
          
          ''')
print("Developed by Umesh Raj Joshi")
Tu = input("Enter the design load  ")

print('''

1. Design of Tension Member
2. Analytical problem in tension
3. Design of Compression Member

''')


a = input("Choose an option:\t")
if a == 1:
    print("****Welcome to Tension member design window****\n \n ")
    Tension()

elif a == 2:
    print(' ***Welcome to analytical problem solution window***\n \n ')
    Tension_Analytical()
elif a == 3:
    print("***Welcome to  Compression member design window***\n\n")
    Compression_Member()
else:
    print("Invalid input, control your fingers")
