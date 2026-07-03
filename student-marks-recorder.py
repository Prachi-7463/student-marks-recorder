
while True:
    #Menu
    print("1. Add Students")
    print("2. View All Students")
    print("3. Exit")
    
    choice = int(input("Enter Your Choice: "))
    
    if choice == 1:
        name = input("Enter The Student's Name: ")
        marks = input("Enter The Student's Marks: ")
        
        file = open("student(s-m-r).txt", "a")
        file.write(f"{name} - {marks}""\n")
        file.close()
        print("You Successfully Stored the Student Record!")
        print("x----x---x----x")
        
    elif choice == 2:
        f = open("student(s-m-r).txt","r")
        data = f.read()
        f.close() 
        
        if data == " ":
            print("You do not add have any student record. Kindly store it first.")
            
        else:
            print("Student Records:" "\n")
            print(data)
                
    elif choice == 3:
        print("Program Closed!")
        break
    
    else:
        print("Invalid Choice. Please Enter Among 1,2 or 3!")
        