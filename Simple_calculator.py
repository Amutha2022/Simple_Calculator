
print("\t*****************************************")                #user interface print statements
print("\t    SIMPLE CALCULATOR APPLICATION ")

try:
    while True:                                                      #while loop 
        print("\t________________________________________\n")        #user interface print statements
        print("Select your choice from below options\n")
        user_choice =input(" 1.Calculation \n 2.Read and print file \n 3.To Exit \n\tYour choice : ")            #user input to enter choice

        if user_choice == "1":                                        #if statement if user enters calculation
            try:                                                       #try function to handle value error 
                while True: 
                    sign_in_out=input("Type yes to sign_in and Type no to sign_out from calculation:")
                    if sign_in_out=="no":
                        print("\nYou signed out from calculation")
                        break
                    elif sign_in_out=="yes":                                             
                        num1 = int(input("\nEnter 1st number :"))               #user input to enter first number
                        num2 = int(input("Enter 2nd number :"))               #user input to enter second number
                        operators = input("Enter the operator (+,-,*,/,) : ")  #user input to enter operator
                        
                        if operators =="+":                                   # if condition if user needs to add the numbers
                            answer=num1+num2
                            print("\nSum of two numbers: ", num1 , "+" , num2 , "=" , (answer),"\n")

                        elif operators == "-":                                 #elif condition if user needs to subtract the numbers
                            answer=num1-num2
                            print("\nDifference between the two numbers : ", num1 , "-" , num2 , "=" , (answer),"\n")

                        elif operators == "*":                                 #elif condition if user needs to multiply the numebrs
                            answer=num1*num2
                            print("\nMultiplication of two numbers : ", num1 , "*" , num2 , "=" ,(answer),"\n")

                        elif operators == "/":                                 #elif condition if user needs to divide the numbers
                            if num2!=0:                                        #if condition if second number is not equal to zero
                                answer=num1/num2
                                print("\nDivision of two numbers : ", num1 , "/" , num2 , "=" ,(answer),"\n")
                            else:                                              #else statement if user enters zero then result should be displayed as dividing by zero is undefined
                                answer= "Dividing by zero is undefined" 

                        elif operators != "+"and operators!="-" and operators!="*" and operators!="/" :  # using elif statement if user enters other then +,-,*,/ alert message will be displayed
                            answer="Invalid operator!!"
                            print(answer,"\n")                                                              
                    print("Result: ", answer,"\n")                              # print answer
                    user_filename=input("Enter filename with extensions of.txt:")
                    with open(user_filename, "a") as equ:                        #open a text file and append function to write the equation in the file when user enters the input
                        equ.write((f"{num1} {operators} {num2} = {answer}\n"))  #write the text file in the given format using function
                        equ.close()                                             #close function to close the text file

            except ValueError:                                              #except valueerror
                    print("Invalid input... Try again!!!!")   

        elif user_choice=="2":                                               #elif statement if user enter to read and print
            file_name = input("Enter the name of the text file: ")           #ask input from the user to read the text file  
            try:    
                with open(file_name,"r") as user_filename:                     #open text file as user_filename
                    print(user_filename.read())                                   #print text file in the terminal using read function
                    user_filename.close()                                         #close function to close the text file
            except FileNotFoundError:                                        #except filenotfounderror
                print("Invalid file name...Try again!!") 
                    
        elif user_choice=="3":                                               #elif statement if user enter to exit
            print("Bye user!!Have a nice day!!!\n") 
            break                                                            #break statement to terminate the program
        
except ValueError:
    print("Invalid input... Try again!!!!")                                  #except both value error 