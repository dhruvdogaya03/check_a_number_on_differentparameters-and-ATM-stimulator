#find your input number on different analysis

while True:
    print(".....Check your Number on Different Parameters.....")
    print("1.Armstrong Number")
    print("2.prime or not prime")
    print("3.Reverse of number")
    print("4.palindrome or not palindrome number")
    print('5.Multiplication of digits')
    print("6.Neon Number or Not Neon Number")
    print("7.Strong number")
    print("8.Harshad Number")
    print("9.Automorphic Number")
    print("10.Duck Number")
    print("11.next prime no")
    print("12.Buzz Number")
    print("13.Adam No")

    choice=int(input("Enter the Choice = "))
    n=int(input("Enter the Number = "))
    temp=n
    
    match choice:
        

        case 1:
            temp=n
            sum=0
            power=len(str(temp))
            if power>=5:
                print("A Armstrong Number can't be 5 digit Number")
            else:
                i=0
                while power>i:
                    digit=temp%10
                    digit=digit**power
                    sum+=digit
                    temp//=10
                    i+=1
                if sum==n:
                    print()
                    print(".........Armstrong Number ........")
                    print()
                else:
                    print()
                    print(" .........Not Armstrong Number........")
                    print()
        case 2:
            flag=True
            if n<=0:
                flag=False
            else:
                power=len(str(temp))
                for i in range(2,n//2+1):
                    if n%i==0:
                        flag=True
                        break
                if flag:
                    print()
                    print("...........Prime Number.........")
                    print()
                else:
                    print()
                    print("..........Not Prime Number..........")
                    print()
        case 3:
            rev=0
            power=len(str(temp))
            for i in range(power):
                digit=temp%10
                rev=rev*10+digit
                temp=temp//10
            print()
            print("..........Reversed Number is ",rev)
            print()

        case 4:
            rev=0
            power=len(str(temp))
            for i in range(power):
                digit=temp%10
                rev=rev*10+digit
                temp=temp//10
            if n==rev:
                print()
                print("..............Pelindrome............")
                print()
            else:
                print("...........Not Pelindrome Number........")
                print()
         
        case 5:
            rev=0
            mul=1
            power=len(str(temp))
            for i in range(power):
                digit=temp%10
                mul*=digit
                temp//=10
            print()
            print("...........Multiplication of Digits =",mul)
            print()
        case 6 :
            sum=0
            sq=n*n
            l=len(str(sq))
            for i in range(l):
                digit=sq%10
                sum+=digit
                sq//=10
            if sum==n:
                  print()
                  print("..........Neon Number..........")
                  print()
        
            else:
                 print()
                 print(".........Not Neon Number.............")
                 print()
        case 7:
            sum=0
            fact=1
            l=len(str(n)) 
            for i in range(l):
                digit=n%10
                fact=1
                for digit in range(1,digit+1):
                    fact*=digit
                sum+=fact
                n//=10
            
            if sum==temp:
                print()
                print("............Strong Number.........")
                print()
            else:
                print()
                print(".........Not a strong Number.........")
                print()
        case 8:
            sum=0
            l=len(str(n))
            for i in range(l):
                digit=n%10
                sum+=digit
            if n%sum==0:
                print("")
                print("...........Harshad Number............")
                print()
            else:
                print()
                print(".............NOt Harshad Number..........")
                print()
        case 9:
            l1=len(str(n))
            sq=n*n
            l2=len(str(sq))
            for i in range(1):
                digit=sq%10**l1
            if digit==n:
                print()
                print(".........Automorphic Number.............")
                print()
            else:
                print()
                print("........Not Automorphic number.........")
                print()

        case 10:
            l=len(str(n))
            rev=0
            for i in range(l):
                digit=temp%10
                rev=rev*10+digit
                temp=temp//10
            rem=rev%10
            rev//=10
            rem2=rev%10
            if rem2==0:
                print()
                print("...........Duck Number......... ")
                print()
            else:
                print()
                print("........Not Duck number............")
                print()
        case 11:
            
            while True:
                temp=temp+1
                if temp<=1:
                    continue
                else:
                    x=0
                    i=2
                    while i<temp//2:
                        if temp%i==0:
                           x=1
                           break
                        i+=1    
                    if x==0:
                        break
            print()
            print("..........Next prime = ",temp)
            print()
        case 12:
            digit=temp%10
            if digit==7:
                print(".........Buzz Number...... ")
            elif temp%7==0:
                    print()
                    print(".......Buzz No......... ")
                    print()
            else:
                print()
                print("..........Not a buzz Number ...........")
                print()
           
               
        case 13:
            sq1=temp*temp
            l=len(str(temp))
            rev=0
            for i in range(l):
                digit=temp%10
                rev=rev*10+digit
                temp//=10
            sq2=rev*rev
            rev2=0
            l2=len(str(sq2))
            for x in range(l2):
                rem=sq2%10
                rev2=rev2*10+rem
                sq2//=10
            if sq1==rev2:
                    print()
                    print("...........Adum Number...........")
                    print()
            else:
                print()
                print("............Not Adum Numberr...........")
                print()