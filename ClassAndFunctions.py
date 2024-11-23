class multipleFunctions():
    def subfields():
        SubfieldsInAI=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for fields in SubfieldsInAI:
            print(fields)
        

    def OddEven():
        num=int(input("Enter the number"))
        print("Number entered:",num)
        if((num%2)==0):
            print(num ,"is Even number")
            message="is Even number"
        else:
            print(num ,"is Odd number")
            message="is Odd number"
        return message

    def Elegible():
        gender=input("Enter your Gender:")
        print("Your Gender:",gender)
        age=int(input("Enter your Age:"))
        print("Your Age:",age)
        if(gender=="Male"):
            if(age>=21):
                print("Eligible")
                message="Eligible"
            else:
                print("Not Eligible")
                message="Not Eligible"
        elif(gender=="Female"):
            if(age>=18):
                print("Eligible")
                message="Eligible"
            else:
                print("Not Eligible")
                message="Not Eligible"
        return message

    def triangle():
        height=int(input("Enter height value:"))
        print("Height:",height)
        breadth=int(input("Enter breadth value:"))
        print("Breadth:",breadth)
        area_triangle=(height*breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",area_triangle)
        height1=int(input("Enter height value:"))
        print("Height1:",height1)
        height2=int(input("Enter height value:"))
        print("Height2:",height2)
        breadth1=int(input("Enter breadth value:"))
        print("Breadth",breadth1)
        perimeter_triangle=height1+height2+breadth1
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeter_triangle)
        

    def percentage():
        sub1=int(input("Enter Mark for the subject1:"))
        print("Subject1=",sub1)
        sub2=int(input("Enter Mark for the subject2:"))
        print("Subject2=",sub2)
        sub3=int(input("Enter Mark for the subject3:"))
        print("Subject3=",sub3)
        sub4=int(input("Enter Mark for the subject4:"))
        print("Subject4=",sub4)
        sub5=int(input("Enter Mark for the subject5:"))
        print("Subject5=",sub5)
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total:",Total)
        Percentage=(Total/500)*100
        print("Percentage:",Percentage)
        
        