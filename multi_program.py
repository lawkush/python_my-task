while True:
    print("Menu choice program")
    print("1.Area of circle")
    print("2.Area of Rectangle")
    print("3.Area of Traingle")
    print("4. Sum of Digit")
    print("5.Exit")
    choice=int(input("Enter your choice"))
    if(choice==1):
        r=int(input("Enter radius"))
        print(f"Area of circle is:{3.14*r}")
    elif choice==2:
        l=int(input("Enter length"))
        b=int(input("Enter breadth"))
        print(f"Area of Rectangle:{l*b}")
    elif choice==3:
        a=float(input("first side"))
        b=float(input("2nd side"))
        c=float(input("3rd side"))
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print(f"Area of Traingle:{area}")
    elif choice==4:
        sum=0
        n=int(input("Enter numbers"))
        while(n!=0):
           
            r=n%10
            sum=sum+r
            n=int(n/10)
        print("Sum of digit:",sum)
    elif choice==5:
        break
    else:
        print("Wrong choice")
    
        
        
