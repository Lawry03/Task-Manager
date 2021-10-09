#
#                                                               TASK 25 ----- TASK MANAGER
#
######################################################################################################################################################################

# Import datetime to get current date, compare dates later, and for the stanard of writting dates in this application

from datetime import datetime

# Declare variable for cuurent date

Today = datetime.now()

# Define function for Logging in

def login():

    # While loop keeps requsting user for correct credentials.

    while True:

        # Print welcom message with current date and time.

        print("\n\n\t\t\t\t\t****** WELCOME TO THE TASK MANAGER® APPLICATION ******\n\n\t\t\t\t\t\t\tDATE : ",Today.strftime("%A, %d, %B, %Y"),"\n\t\t\t\t\t\t\tTIME : ",Today.strftime("%H"),":",Today.strftime("%M"))

        # Open User.txt file
        
        with open("user.txt","r") as f:

            # Request for user input.

            user_name = (input("\n\n\t\t\t\t\t\tPlease enter a valid 'username' : ")).lower()
            
            password = input("\t\t\t\t\t\tPlease enter a valid 'password' : ")

            for line in f:

                # Unpack data from user.txt file and assign respective variables.

                valid_username, valid_password = line.split(', ')

                # Strip password of any unwanted spaces.

                stripped_password = valid_password.strip()

                # Compare user input with valid caredentials

                if user_name == valid_username and password == stripped_password:

                    # If user input is valid then access is granted.

                    valid_login = True

                    # Return variables

                    return user_name,valid_login

            # Print output for incorrect credentials
                
            print("\t___________________________________________________________________________________________________________________________________________________")
            print("\n\t\t\t\t---> It seems like you have entered an incorrect 'Username' or 'Password'. <---\n\n\t\t\t\t\t\t\t---> Please try again.<---")
            print("\t___________________________________________________________________________________________________________________________________________________")



# Define a function for the menu for both admin and other users.

def menu(user_name):
    
    # Print Output
    
    print("\n\n\t\t\t\t\t\t\t*** Logged in as {} ***\n".format(user_name.upper()))

    # Declare variable for admin menu.
    
    message_1 = """
\t\t\tTask Manager®\n\n
\t\t\t _______________________________________________________________________________________________
\t\t\t*\t\t\t\t\t\t\t\t\t\t\t\t*
\t\t\t*\t\t\t\tPlease select one of the following options\t\t\t*
\t\t\t*\t\t\t\t\t\t\t\t\t\t\t\t*
\t\t\t*\tr    - \tRegister User\t\t\t\t\t\t\t\t\t*
\t\t\t*\ta    - \tAdd task\t\t\t\t\t\t\t\t\t*
\t\t\t*\tva   - \tView all tasks\t\t\t\t\t\t\t\t\t*
\t\t\t*\tvm   - \tView my tasks\t\t\t\t\t\t\t\t\t*
\t\t\t*\tgr   - \tGenerate reports\t\t\t\t\t\t\t\t*
\t\t\t*\tds   - \tDisplay statistics\t\t\t\t\t\t\t\t*
\t\t\t*\te    - \tExit\t\t\t\t\t\t\t\t\t\t*
\t\t\t*_______________________________________________________________________________________________*

"""
    
    # Declare variable for non admin users menu.
    
    message_2 = """
\t\t\tTask Manager®\n\n
\t\t\t _______________________________________________________________________________________________
\t\t\t*\t\t\t\t\t\t\t\t\t\t\t\t*
\t\t\t*\t\t\t\tPlease select one of the following options\t\t\t*
\t\t\t*\t\t\t\t\t\t\t\t\t\t\t\t*
\t\t\t*\ta    - \tAdd task\t\t\t\t\t\t\t\t\t*
\t\t\t*\tva   - \tView all tasks\t\t\t\t\t\t\t\t\t*
\t\t\t*\tvm   - \tView my tasks\t\t\t\t\t\t\t\t\t*
\t\t\t*\te    - \tExit\t\t\t\t\t\t\t\t\t\t*
\t\t\t*_______________________________________________________________________________________________*


"""

    # If username belongs to 'admin'

    if user_name == "admin":

        # While loop to ensure that a provided option is selected.

        while True:

            # Print Output menu for admin.

            print(message_1)

            # Request for user option.
            
            option = (input("\n\t\t\t\t\t\t\tEnter Here ---> : ")).lower()


            if option == "r" or option == "a" or option == "va" or option == "vm" or option == "e" or option == "gr" or option == "ds":

                # If option is valid return option

                return option

            # Print Output if option is not valid.

            else:
                print("\n\t\t\t\t\t---> That was an invalid option, please try again <---\n")


    else:

        # While loop to ensure that a provided option is selected.

        while True:

            # While loop to ensure that a provided option is selected.
            
            print(message_2)

            # Request for user option.

            option = (input("\n\t\t\t\t\t\t\tEnter Here ---> : ")).lower()

            if option == "a" or option == "va" or option == "vm" or option == "e":

                # If option is valid return option
                
                return option

            # Print Output if option is not valid.
            
            else:
                print("\n\t\t\t\t\t---> That was an invalid option, please try again <---\n")


# Define function for user registration.

def reg_user():

    # While loop to ensure that user input is a valid name and password of more than 3 characters and to check if user already exsists.

    while True:

        register = True

        # Print Output
        
        print("\n\n\t\t-------------------------------------------------  USER REGISTRATION  -----------------------------------------------------")

        # Request for user inputs.

        new_userename = (input("\n\n\n\t\t\t\t\t\t\tPlease enter a new User-Name : ")).lower()
      
        new_password = input("\t\t\t\t\t\t\tPlease enter user password : ")

        confirm_password = input("\t\t\t\t\t\t\tRe-Enter password : ")

        # Check if inputs are more than 3 characters.

        if len(new_userename) < 2 or len(confirm_password )<  2:
            print("\n\t\t\t\t\t\t     **** Username or Password is too short ****")
            register = False

        # Open user.txt file.

        with open("user.txt","r")as f:

            for line in f:

                # Unpack data from user.txt file and assign respective variables.

                valid_username, valid_password = line.split(", ")


                if valid_username == new_userename:

                    # If the userinput is the same as any valid username the usser exsists.

                    register = False

                    # Print output.

                    print("\n\t\t\t\t\t\t\t  **** That USER already exsists ****")
          
        # Compare the confirmed password with the new password and check ensure username is within parameters.
        
        if new_password == confirm_password and register is True:

            # Open the user.txt file in append mode to add new user.

            User_File = open("user.txt","a+")

            # Write username and password.

            User_File.write('\n'+new_userename + ', '+new_password)

            # Close file.

            User_File.close()

            # Print output

            print(f"\n\t\t\t\t\t\t**** New user has been succesfully registered ****\n\n\t\t\t\t\t\t\t\tUsername :\t{new_userename}\n\t\t\t\t\t\t\t\tPassword :\t{new_password}")
            print("\n\n\t\t----------------------------------------------------------------------------------------------------------------------------")
            break

        else:

            # Print output if registration is not allowed.

            print("\n\t\t\t\t\t\t\t    **** Please Try Again ****\n")

    # Used input function as a pause before returning to main menu
    
    input("\n\n\t\t\t\t\t\t----> PRESS ENTER TO RETURN TO MAIN MENU <-----\n")



# Define function for adding tasks.

def add_task():

    # Declare variable for an empty user list.

    user_list = []

    # Print a list of all registered users.

    print("\n\n\t\t-------------------------------------------------  ADD TASK  -----------------------------------------------------\n")
    print("\n\t\t\tLIST OF VALID USERS \n\n")

    # Open user.txt file to access all valid users.
    
    User_File = open("user.txt","r")
    
    lines = User_File.readlines()
    
    for line in lines:

        # Unpack and assign respective variables.
        
        name,password = line.split(', ')

        # Append the user list.

        user_list.append(name)

        # Print usernames
        
        print(f"\t\t\t\t\t--> : {name}\n")

    # Close User.txt flie.
    
    User_File.close()



    # While loop to ensure that selected user is a valid user.

    while True:

        # Request for user input.

        user = (input("\n\t\tTo which user would you like to assign a task : ")).lower()

        # Check if user is within the list of valid users.

        if user.lower() in user_list:
            break

        # Print output if user is not valid.
        
        print(f"\n\t\t\t\t\t\t---------- '{user}' is Not a valid 'user' ----------")

    # Request for user input.
    
    task_title = input("\n\t\tTitle of the task being assigned : ")
    
    task_description = input("\n\t\tPlease give a brief description of the task : ")

    # Assign current date to variable start date.
    
    start_date = Today.strftime("%d %b %Y")

    print("\n\n\t\t\t\t\t\t---------- Kindly enter only NUMERICAL VALUES ----------")


    # While loop to ensure that input is numerical
    
    while True:

        # Request for user input.
        
        day_num = input("\n\t\tOn which DAY is the task due : ")

        if day_num.isdigit() and int(day_num) < 32:

            break

        # Print output if input is invalid.

        else:
            print("\n\n\t\t\t\t\t\t--------- That is not a vaild DAY please try again ---------")

    # While loop to ensure that input is numerical
    
    while True:

        # Request for user input.

        month_num = input("\n\t\tIn what MONTH is the task due (1-12) : ")

        if month_num.isdigit() and int(month_num) < 13:

            break

        else:
            
            # Print output if input is invalid.
            
            print("\n\n\t\t\t\t\t\t--------- That is not a vaild MONTH please try again ---------")

    # While loop to ensure that input is numerical
    
    while True:

        # Request for user input.
        
        year_num = input("\n\t\tIn what YEAR is the task due : ")

        if year_num.isdigit() and int(year_num) < 10000:

            break

        else:

            # Print output if input is invalid.
            
            print("\n\n\t\t\t\t\t\t--------- That is not a vaild YEAR please try again ---------")

    # Convert user input to month name.

    month_object = datetime.strptime(month_num,"%m")

    # Convert month name to shorter name

    month_name = month_object.strftime("%b")

    # Declare variable for the end date.

    end_date = day_num+" "+month_name+" "+year_num

    # Initiate complete variable with 'NO'

    completed = "NO"

    # Open task.txt file in append mode.

    Task_File = open("tasks.txt","a+")

    # Write to task.txt file.

    Task_File.write('\n'+user + ', ' + task_title + ', ' + task_description + ', ' + start_date + ', ' + end_date + ', ' + completed)

    # Close task.txt flie.

    Task_File.close()

    # Print output.

    print("\n\n\t\t\t\t\t\t---------- New Task Has Been Successfully Loaded ----------\n\n")
    print("\n\t\t--------------------------------------------------------------------------------------------------------------\n")

    # Used input function as a pause before returning to main menu
    
    input("\n\n\t\t\t\t\t\t ----> PRESS ENTER TO RETURN TO MAIN MENU <-----\n")


# Define function to view all tasks.

def view_all():

    # Print heading with date and time.

    print("\n\n\t\t------------------------------------------------------ VIEW ALL TASKS  -------------------------------------------------------------------\n\n")
    
    print("\n\t\tTask Manager®\n\t\t\t\t\t\t\tDATE : ",Today.strftime("%A, %d, %B, %Y"),"\n\t\t\t\t\t\t\tTIME : ",Today.strftime("%H"),":",Today.strftime("%M"),"\n\t\t\t\t\t\t\t__________________________________\n\n\n")

    # Open task.txt file.
    
    with open("tasks.txt","r+") as f:

        for line in f:

            # Unpack each element and assign variabels respectivly.

            user, task_title, task_description, start_date, end_date, completed = line.split(', ')

            # Print all available task in a neatly arrange format.

            print(f"""
\t\t*\tAssigned to\t\t: {user}
\t\t*\tTask Title\t\t: {task_title}
\t\t*\tTask Description\t: {task_description}
\t\t*\tStart Date\t\t: {start_date}
\t\t*\tDue Date\t\t: {end_date}
\t\t*\tCompletion Status\t: {completed}
""")
        print("\n\n\t\t-----------------------------------------------------------------------------------------------------------------------------------------\n\n")

        # Used input function as a pause before returning to main menu
        
        input("\n\n\t\t\t\t\t\t\t   ----> PRESS ENTER TO RETURN TO MAIN MENU <-----\n")



# Define function to view user tasks only.

def view_mine(user_name):

    # Declare count variable to assign a task identification number for each task.

    count = 0

    # Declare empty list variable to save all tasks assigned to the user.
    
    task_id = []

    print("\n\n\t\t------------------------------------------------------ VIEW MY TASKS  -------------------------------------------------------------------\n\n")


    print("\n\t\tTask Manager®\n\t\t\t\t\t\t\tDATE : ",Today.strftime("%A, %d, %B, %Y"),"\n\t\t\t\t\t\t\tTIME : ",Today.strftime("%H"),":",Today.strftime("%M"),"\n\t\t\t\t\t\t\t__________________________________\n\n\n")

    # Open task.txt file in read mode.
    
    with open("tasks.txt","r") as f:

        for line in f:

            # Unpack each element and assign variabels respectivly.
            
            user, task_title, task_description, start_date, end_date, completed = line.split(', ')

            # Create a dictionanry with values and keys.

            task_dictonary = { '1' : user, '2' : task_title, '3' : task_description, '4' : start_date, '5' : end_date, '6' : completed }

            # Increace count by 1.

            count = count + 1

            
            if user_name == user :

                # If the logged in username matches the user variable append task id list with the count number.

                task_id.append(count)

                # Print output in a neat format.

                print(f"""
\t\t\t\t\t\tTASK IDENTIFICATION NUMBER : {count}

\t\tAssigned to\t\t\t: {task_dictonary['1']}
\t\tTask Title\t\t\t: {task_dictonary['2']}
\t\tTask Description\t\t: {task_dictonary['3']}
\t\tStart Date\t\t\t: {task_dictonary['4']}
\t\tDue Date\t\t\t: {task_dictonary['5']}
\t\tCompletion Status\t\t: {task_dictonary['6']}
""")
                

    if len(task_id) == 0:

        # If the task id list is empty there are no available tasks therefore return to main menu.
        
        print("\n\n\t\t\t\t\t\t\t    **** NO AVAILABLE TASKS ****\n\n")
        print("\n\n\t\t--------------------------------------------------------------------------------------------------------------------------------------------\n\n")

        # Used input function as a pause before returning to main menu
        
        input("\n\n\t\t\t\t\t\t   ----> PRESS ENTER TO RETURN TO MAIN MENU <-----\n")
        return

    # Declare control variable for while loop to view spesific task.
    
    view_spesific = True

    while view_spesific:

        # Request for user to enter a task identification number which matches the number valid task number assigned to user.
            
        option = input("\n\n\t\t\t****** To select a valid task ENTER the TASK IDENTIFICATION NUMBER or to return to Main Menu press 'e' ******\n\n\t\t\t\t\t\t\t\tENTER HERE --- > : ")

        if option == 'e':

            # Exit back to menu
            
            break
                

        elif option.isdigit() and int(option) in task_id:

            # If the option entered is a digit and the input number is within the task id list the option is valid.
                
            # Reset count variable.
            
            count = 0

            # Open task.txt file in read mode.
            
            with open("tasks.txt","r") as f:
                for line in f:

                    # Unpack each element and assign variabels respectivly.

                    user, task_title, task_description, start_date, end_date, completed = line.split(', ')

                    # Increase count by 1.
                        
                    count = count + 1


                    if int(option) == count and user_name == user and (int(option) in task_id):

                        # If the count is the same as the entered option and username is the same as the user and the option is within the task id list.

                        task_dictonary = { '1' : user, '2' : task_title, '3' : task_description, '4' : start_date, '5' : end_date, '6' : completed }
                    
                        # Print task neatly.
                        
                        print(f"""
\n\n\n
\t\t\t\t\t\tTASK IDENTIFICATION NUMBER\t: {count}

\t\tAssigned to\t\t\t: {task_dictonary['1']}
\t\tTask Title\t\t\t: {task_dictonary['2']}
\t\tTask Description\t\t: {task_dictonary['3']}
\t\tStart Date\t\t\t: {task_dictonary['4']}
\t\tDue Date\t\t\t: {task_dictonary['5']}
\t\tCompletion Status\t\t: {task_dictonary['6']}
""")
                
                            
                            
            # Strip the complete variable stared in dictionary.
            
            complition_status = task_dictonary['6'].strip('\n')

                            
            if complition_status == 'YES':

                # If the completion status is valid. The task is complete.
                
                print("\t\tTHIS TASK HAS BEEN COMPLETED")
                print("\n\n\t\t--------------------------------------------------------------------------------------------------------------------------------------------\n\n")

                # Used input function as a pause before returning to main menu
                
                input("\n\n\t\t\t\t\t\t\t   ----> PRESS ENTER TO RETURN TO MAIN MENU <-----\n")
                return

            # While loop to insure tht a vaild input is entered. 

            while True:

                # Print menu
                
                print("\n\t\t\t\t-----------------------------------------------------------------------\n\n\t\t\t\t\t\tMARK TASK AS COMPLETE OR EDIT TASK\n")

                # Request for user input.

                user_input = input("\n\t\t\t\t\tTo 'mark the task as COMPLETE'\t\t-\tPRESS '1'\n\n\t\t\t\t\tTo 'EDIT the task'\t\t\t-\tPRESS '2'\n\n\t\t\t\t\tTo 'EXIT'\t\t\t\t-\tPRESS 'e'\n\n\t\t\t\t\tENTER HERE ---> : ")
                    
                if user_input == '1':

                    # User selects option 1, to mark the task as complete.

                    # Declar variable for empty task list

                    empty_task_list = []

                    # Reset count to zero.
                    
                    count = 0

                    # Open task.txt file in read+ mode.
                    
                    with open("tasks.txt","r+") as f:
                        for line in f.readlines():

                            # Unpack each element and assign variabels respectivly.

                            user, task_title, task_description, start_date, end_date, completed = line.split(', ')

                            # Increase count by one.
                            
                            count = count + 1
                                
                            if int(option) == count and user_name == user and (int(option) in task_id):

                                # If the count is the same as the entered option and username is the same as the user and the option is within the task id list.
                                
                                task_id_number = count

                                # Replace 'NO' WITH 'YES'.
                                
                                new_line = line.replace("NO","YES")

                                # Append the empty task list with the new line.
                                
                                empty_task_list.append(new_line)

                                # Declare line variable as empty string.

                                line = ''

                            # Append every other unchanged task to list.
                            
                            empty_task_list.append(line)

                    # Remove empty string from list.
                                
                    empty_task_list.remove('')

                    # Open task.txt file in write mode.
                    
                    with open("tasks.txt","w") as f:
                        for line in empty_task_list:

                            # Write each line in the task.txt file
                            
                            f.write(line)

                    # Print Output.
                    print(f"\n\n\t\t\t\t\tTASK IDNTIFICATION NUMBER {task_id_number} ------- HAS BEEN SUCCESSFULLY UPDATED")
                    print("\n\n\t\t--------------------------------------------------------------------------------------------------------------------------------------------\n\n")

                    # Used input function as a pause before returning to main menu
                    
                    input("\n\n\t\t\t\t\t\t----> PRESS ENTER TO RETURN TO MAIN MENU <-----\n")
                    return

                    
                elif user_input == '2':

                    # If user selects option 2 , to either change assigned username or change due date. 


                    # While loop to ensure that selection is valid.
                    
                    while True:

                        # Pritn heading and menu.
                        
                        print("\n\n\n\n\t\t\t\t-----------------------------------------------------------------------\n\n\t\t\t\t\t\t\t\tEDIT TASK\n")

                        # Request for user input.
                        
                        user_input = input("\n\t\t\t\t\tTo change assigned 'USERNAME'\t\t-\tPRESS '1'\n\n\t\t\t\t\tTo change 'DUE DATE'\t\t\t-\tPRESS '2'\n\n\t\t\t\t\tTo 'EXIT'\t\t\t\t-\tPRESS 'e'\n\n\t\t\t\t\tENTER HERE ---> : ")
                            
                        if user_input == '1':

                            # If user selection is to assigned change username.

                            # Declare variable for empty user list.
                            
                            username_list = []
                            
                            print("\n\n\t\t\t\t\t\t\tLIST OF VALID USERS :\n\n")

                            # Open user.txt file in read mode.
                            
                            User_File = open("user.txt","r")
                            lines = User_File.readlines()

                            # Declare variable for i used to number the valid users.
                            i = 0
                                
                            for line in lines:
                                i = i + 1
                                name,password = line.split(', ')

                                # Print valid user and what nuber they are registered as.
                                
                                print(f"\t\t\t\t\t\t({i})\t\t-->\t\t: {name}\n")

                                # Append the list for usernames.
                                
                                username_list.append(name)

                            # Close user.txt file.
                            
                            User_File.close()

                            # While loop to ensure that input entered is a valid user.

                            while True:

                                # Request for user input.
                                
                                user_request = input("\n\n\t\t\t\t\tTo which user would you like to assign the task to : ")

                                # Ensure user input is within the list of valid users.

                                if user_request.lower() in username_list:

                                    # Declare variable for empty list for tasks.
                                    
                                    empty_task_list = []

                                    # Reset count.
                                    
                                    count = 0

                                    # Open task.txt file in read+ mode.
                                    
                                    with open("tasks.txt","r+") as f:
                                        for line in f.readlines():

                                            # Unpack each element and assign variabels respectivly.

                                            user, task_title, task_description, start_date, end_date, completed = line.split(', ')

                                            # Increase count by one.
                                            
                                            count = count + 1

                                            if int(option) == count and user_name == user and (int(option) in task_id):
                                                task_id_number = count

                                                # Replace the selected task with the new username requested.
                                                
                                                new_line = line.replace(user, user_request.lower())

                                                # Append task to list.
                                                
                                                empty_task_list.append(new_line)

                                                # Declare line variable as empty string.
                                                
                                                line = ''

                                            # Append each line to empty list of tasks.
                                            
                                            empty_task_list.append(line)

                                    # Remove empty string from task list.

                                    empty_task_list.remove('')

                                    # Open task.txt file in write mode.
                                    
                                    with open("tasks.txt","w") as f:
                                        for line in empty_task_list:

                                            # Rewrite task file with new data in empty task list.
                                            
                                            f.write(line)

                                    # Print output.
                                    
                                    print(f"\n\n\t\t\t\t\tTASK IDNTIFICATION NUMBER {task_id_number} ------- HAS BEEN SUCCESSFULLY UPDATED")
                                    print("\n\n\t\t--------------------------------------------------------------------------------------------------------------------------------------------\n")

                                    # Used input function as a pause before returning to main menu
                                    
                                    input("\n\t\t\t\t\t\t----> PRESS ENTER TO RETURN TO MAIN MENU <-----\n")
                                    return

                                
                                else:

                                    # Print output if user enters an invalid user.
                                    
                                    print("\n\n\t\t\t\t\t\t---- INVALID USER PLEASE TRY AGAIN ----")                                        


                        # If user selection is to change due date a of spesific task.
                        
                        elif user_input == '2':
                            
                            print("\n\n\n\t\t\t\t\t\t\t**Kindly enter only NUMERICAL VALUES !!!**\n")

                            # While loop to ensure that a valid entry is entered.
                            
                            while True:

                                # Request for user input and ensure it is within parameters.
                                
                                day_num = input("\n\t\t\t\t\tOn which DAY is the task due : ")
                                if day_num.isdigit() and int(day_num) < 32:
                                    break
                                
                                else:
                                    
                                    print("\n\n\t\t\t\t\t\t---- That is not a vaild DAY please try again -----\n")

                            while True:

                                # Request for user input and ensure it is within parameters.
                                
                                month_num = input("\n\t\t\t\t\tIn what MONTH is the task due (1-12) : ")
                                if month_num.isdigit() and int(month_num) < 13:
                                    break
                                
                                else:
                                    
                                    print("\n\n\t\t\t\t\t\t----- That is not a vaild MONTH please try again -----\n")

                            while True:

                                # Request for user input and ensure it is within parameters.

                                year_num = input("\n\t\t\t\t\tIn what YEAR is the task due : ")
                                if year_num.isdigit() and int(year_num) < 10000:
                                    break
                                
                                else:
                                    
                                    print("\n\n\t\t\t\t\t\t----- That is not a vaild YEAR please try again\n")

                            # Convert user input to month name.

                            month_object = datetime.strptime(month_num,"%m")

                            # Convert month name to short abriviation.
                            
                            month_name = month_object.strftime("%b")

                            # Declare variable for new end date.
                            
                            new_end_date = day_num+" "+month_name+" "+year_num

                            # Create an empty list for tasks

                            empty_task_list = []

                            # Reset count to zero.
                            
                            count = 0

                            # Open tasks.txt in readmode.
                            
                            with open("tasks.txt","r+") as f:
                                for line in f.readlines():

                                    # Unpack each element and assign variabels respectivly.
                                    
                                    user, task_title, task_description, start_date, end_date, completed = line.split(', ')

                                    # Increase the count by 1.
                                    
                                    count = count + 1
                                    
                                    if int(option) == count and user_name == user and (int(option) in task_id):
                                        task_id_number = count

                                        # Replace end date with the new end date.
                                        
                                        new_line = line.replace(end_date, new_end_date)

                                        # Append new line to list.
                                        
                                        empty_task_list.append(new_line)

                                        # Declare line as empty string.
                                        
                                        line = ''

                                    # Append each line to list.
                                    
                                    empty_task_list.append(line)

                            # Remove empty string from list.

                            empty_task_list.remove('')

                            # Open tasks.txt file in write mode.

                            with open("tasks.txt","w") as f:
                                for line in empty_task_list:

                                    # Rewrite each line from empty list to tasks.txt file.
                                    
                                    f.write(line)

                            # Print output.
                            
                            print(f"\n\n\t\t\t\t\tTASK IDNTIFICATION NUMBER {task_id_number} ------- HAS BEEN SUCCESSFULLY UPDATED")

                            # Used input function as a pause before returning to main menu
                            
                            input("\n\n\t\t\t\t\t\t\t   ----> PRESS ENTER TO RETURN TO MAIN MENU <-----\n")
                            return
                        
                        elif user_input == 'e':

                            # Return to main menu.
                            
                            return
                        
                        else:

                            # Print Output.
                            
                            print("\n\t\t\t\t\t  ----- That is not a vaild entry please try again -----")
                            
                elif user_input == 'e':

                    # Return to main menu.
                    
                    break
                
                else:
                    # Print Output.
                    
                    print("\n\t\t\t\t\t  ----- That is not a vaild entry please try again -----")
                                    
                        
        else:
            # Print Output.
            
            print("\n\n\n\t\t\t\t\t\t\t\t\tVALID NUMBER\S")

            # Print out a list of that valid task identification number assigned to a user.
            
            for i in task_id:
                print(f"\n\t\t\t\t\t\t\t\tTASK IDENTIFICATION NUMBER : {i}")
                

# Define function to generate user overview.

def user_overview():

    # Open and close file in write mode to clear file.

    user_overview_file = open("user_overview.txt","w")
    user_overview_file.close

    # Open User.txt file in read mode.
    
    userfile = open("user.txt","r")

    # Read user file data.
    
    users = userfile.readlines()

    # Close user file.
    
    userfile.close()

    # The number of users is equal to the number of elements withing the user file.

    no_of_users = len(users)

    # Open user.txt file in read mode.
    
    with open("user.txt","r") as f:
        for line in f.readlines():

            # Reset all counts to zero.
            
            total_task = 0
            completed_tasks = 0
            incomplete_tasks = 0
            tasks_per_user = 0
            incomplete_overdue = 0

            # Unpack each element and assign variabels respectivly.
            
            username, password = line.split(', ')

            # for every username in the user file, open task.txt file in read mode.

            with open("tasks.txt","r") as f:
                for line in f.readlines():
                    
                    # Increace total task cout by 1.
                    
                    total_task = total_task + 1

                    # Unpack each element and assign variabels respectivly.

                    user, task_title, task_description, start_date, end_date, completed = line.split(', ')

                    # Create a new date object for comparision in order to check if task is overdue.

                    date_object = datetime.strptime(end_date, "%d %b %Y")

                    if user == username:

                        # Add 1 to total tasks assigned to the user.
                        
                        tasks_per_user = tasks_per_user + 1

                    if user == username and completed.strip('\n') == "YES":

                        # Add 1 to completed tasks count assigned to the user.
                        
                        completed_tasks = completed_tasks + 1
                        
                    if user == username and completed.strip('\n') == "NO":

                        # Add 1 to oncomplete tasks count assigned to the user.
                        
                        incomplete_tasks = incomplete_tasks + 1
                        
                    if user == username and completed.strip('\n') == "NO" and Today > date_object:

                        # Add 1 to incomplete and overdue tasks coutn assigned to the user.
                        
                        incomplete_overdue = incomplete_overdue + 1

                if tasks_per_user == 0:

                    # If the user has no tasks assigned to them.

                    # Open user overview.txt file in append mode.

                    user_overview_file = open("user_overview.txt","a+")

                    # write given values to user overview file.

                    user_overview_file.write( str(no_of_users) + ', ' + username + ', ' + str(total_task) + ', ' + str(0) + ', ' + str(0) + ', ' + str(0) + ', ' + str(0) + ', ' + str(0) + ', ' + str(0) + ', ' + str(0) + ', ' + str(0) + '\n')

                    # Close user overview file.
                    
                    user_overview_file.close()
                    

                elif tasks_per_user > 0 :

                    # If the user has atleast 1 task.
                    

                    # Calculate percentage of the total number of tasks have been assigned to that user.
                    
                    user_task_percantage = round(( tasks_per_user / total_task ) * 100,2)

                    # Calculate percentage of the total number of copleted tasks have been assigned to that user.

                    user_complete_percantage = round(( completed_tasks / tasks_per_user ) * 100,2)

                    # Calculate percentage of the total number of incomplete tasks have been assigned to that user.

                    user_incomplete_percangate = round(( incomplete_tasks / tasks_per_user ) * 100,2)

                    # Calculate percentage of the total number of incomplete and overdue tasks have been assigned to that user.

                    user_incompl_overdue_percentge = round(( incomplete_overdue / incomplete_tasks ) * 100,2)

                    # Open user overview.txt file in append mode.

                    user_overview_file = open("user_overview.txt","a+")

                    # Write data to file in a stamdard format.

                    user_overview_file.write(str(no_of_users) + ', ' + username + ', ' + str(total_task) + ', ' + str(tasks_per_user) + ', ' + str(completed_tasks) + ', ' + str(incomplete_tasks) + ', ' + str(incomplete_overdue) + ', ' + str(user_task_percantage) + ', ' + str(user_complete_percantage) + ', ' + str(user_incomplete_percangate) + ', ' + str(user_incompl_overdue_percentge) + '\n')

                    # Close file.
                    
                    user_overview_file.close
             

# Define task to genarate task overview.

def task_overview():

    # Reset all counts.

    total_task = 0
    incomplete_overdue_count = 0
    complete_count = 0
    incomplete_count = 0

    # Open tasks.txt file in read mode.
    
    with open("tasks.txt","r") as f:
        for line in f.readlines():

            # Increase total task count by 1 with eat iteration.

            total_task = total_task + 1

            # Unpack each element and assign variabels respectivly.
            
            user, task_title, task_description, start_date, end_date, completed = line.split(', ')

            # Create a new date object for comparision in order to check if task is overdue.

            date_object = datetime.strptime(end_date, "%d %b %Y")
            

            if completed.strip('\n') == "YES":

                # If task is complete add 1 to count.
                
                complete_count = complete_count + 1
                
            if completed.strip('\n') == "NO":

                # If task is complete add 1 to count.
                
                incomplete_count = incomplete_count + 1
                
            if completed.strip('\n') == "NO" and Today > date_object :

                # If task is complete add 1 to count.
                
                incomplete_overdue_count = incomplete_overdue_count + 1

    # Calculate percentage of the total number of incomplete tasks.

    incomplete_percent = round((incomplete_count / total_task) * 100,2) if incomplete_count or total_task != 0 else 0        # To avoid mathamatical error if denominator is zero.

    # Calculate percentage of the total number of incomplete and overdue tasks.

    incomplete_overdue_percent = round((incomplete_overdue_count / incomplete_count)* 100,2)  if incomplete_overdue_count or incomplete_count != 0 else 0   # To avoid mathamatical error if denominator is zero.

    # Open task overview.txt file in write mode.
    
    task_overview_file = open("task_overview.txt","w")

    # Write data to file in standard format.
    
    task_overview_file.write(str(total_task) + ', ' + str(complete_count) + ', ' + str(incomplete_count) + ', ' + str(incomplete_overdue_count) + ', ' + str(incomplete_percent) + ', ' + str(incomplete_overdue_percent) )

    # Close file.
    
    task_overview_file.close


# Define function to genarate reports.

def generate_report():

    print("\nDATE : ",Today.strftime("%A, %d, %B, %Y"),"\nTIME : ",Today.strftime("%H"),":",Today.strftime("%M"),"\n")

    # Call task overview function to update the data.

    task_overview()

    # Call user overview function to update the data.

    user_overview()

    # Print output.
    
    print("\n\n\t___________________________________________________________________________________________________________________________________________________________")
    print("\t***********************************************************************************************************************************************************\n")
    print("\t\t--------------------------------------------------  REPORTS SUCCESSFULLY UPDATED  ---------------------------------------------------------")

    # Used input function as a pause before returning to main menu.
    
    input("\n\n\t\t\t\t\t\t\t   ----> PRESS ENTER TO RETURN TO MAIN MENU <-----\n")


# Define functione to display statistics.

def display_statistics():

    # Declare variable for current date.

    current_date = Today.strftime("%A, %d, %B, %Y")

    # Open task overview in read mode.

    with open("task_overview.txt","r") as f:
        for line in f.readlines():

            # Unpack each element and assign variabels respectivly.

            total_task, complete_count, incomplete_count, incomplete_overdue_count, incomplete_percent, incomplete_overdue_percent = line.split(', ')


    # Print Task overview.

    print(f"""

\t___________________________________________________________________________________________________________________________________________________________
\t***********************************************************************************************************************************************************
\n\n
\t\t{current_date}
\n\n
\t\t\t------------------------------------------------  Task Overview  -----------------------------------------------------
\n\n
\t\tTASK OVERVIEW AND REPORT TOTALS
\n
\t\tTotal number of tasks genarated and track by Task Manager®\t:\t{total_task}
\n\n
\t\t\t _______________________________________________________________________________________________________________________________
\t\t\t|\tTotal No of Tasks Completed\t|\tTotal No of Tasks Incomplete\t|\tTotal No of Tasks Incomplete & Overdue\t|
\t\t\t|\t                           \t|\t                            \t|\t                                      \t|
\t\t\t|\t\t{complete_count}     \t\t\t|\t\t{incomplete_count}    \t\t\t|\t\t\t{incomplete_overdue_count}    \t\t\t|
\t\t\t|_______________________________________________________________________________________________________________________________|
\n\n
\t\tTASK OVERVIEW REPORT PERCENTAGES
\n\n
\t\t\t\t\t _______________________________________________________________________________________________________
\t\t\t\t\t|\tTotal Percentage of Tasks Inomplete\t|\tTotal Percentage of Tasks Incomplete & Overdue\t|
\t\t\t\t\t|\t                                   \t|\t                                              \t|
\t\t\t\t\t|\t\t\t{incomplete_percent}%      \t\t|\t\t\t{incomplete_overdue_percent}%         \t\t\t|
\t\t\t\t\t|_______________________________________________________________________________________________________|
\n\n
\t\t\t------------------------------------------------  END OF REPORT -----------------------------------------------------
\n\n\n\n\n\n\n

""")
            

    # Open user overview in read mode.
    
    with open("user_overview.txt","r") as f:
        for line in f.readlines():

            # Unpack each element and assign variabels respectivly.
            
            no_of_users, username, total_task, tasks_per_user, completed_tasks, incomplete_tasks, incomplete_overdue, user_task_percantage, user_complete_percantage, user_incomplete_percangate, user_incompl_overdue_percentge = line.split(', ')

            # Strip value of newline character.
            
            incomplete_overdue_percantage_user = user_incompl_overdue_percentge.strip('\n')

            # Print output for each user in table format.

            print(f"""
\t___________________________________________________________________________________________________________________________________________________________
\t***********************************************************************************************************************************************************
\n\n
\t\t{current_date}
\t\t\t------------------------------------------------  User Overview  -----------------------------------------------------
\n\n
\t\tUSER OVERVIEW REPORT
\n
\n
\t\tUsername\t\t\t\t:\t{username}
\n\n\t\tTotal number of registered users\t:\t{no_of_users}\n\n
\t\tNumber of tasks assinged to '{username}'\t:\t{tasks_per_user}
\n\n
\t\t\t _______________________________________________________________________________________________________________
\t\t\t|\tNo of Completed Tasks\t|\tNo of Incomplete Tasks\t|\tNo of Incomplete & Overdue Tasks\t|
\t\t\t|\t                     \t|\t                      \t|\t                                \t|
\t\t\t|\t\t{completed_tasks}  \t\t|\t\t{incomplete_tasks}\t\t|\t\t\t{incomplete_overdue}\t\t\t|
\t\t\t|_______________________________________________________________________________________________________________|
\n\n\n
\t\tUSER OVERVIEW PERCENTAGES
\n
\t\tPercentage of the total number of tasks assigned to '{username}'\t:\t{user_task_percantage}%
\n\n
\t\t _______________________________________________________________________________________________________________________________________
\t\t|\tPercentage of Completed Tasks\t|\tPercentage of Incomplete Tasks\t|\tPercentage of Incomplete & Overdue Tasks\t|
\t\t|\t                             \t|\t                              \t|\t                                        \t|
\t\t|\t\t{user_complete_percantage}%\t\t\t|\t\t{user_incomplete_percangate}%\t\t\t|\t\t\t{incomplete_overdue_percantage_user}%\t\t\t\t|
\t\t|_______________________________________________________________________________________________________________________________________|
\n\n\n
\t\t\t------------------------------------------------  End of report -----------------------------------------------------
\t___________________________________________________________________________________________________________________________________________________________
\t***********************************************************************************************************************************************************

""")

    # Used input function as a pause before returning to main menu.
            
    input("\n\n\t\t\t\t\t\t\t   ----> PRESS ENTER TO RETURN TO MAIN MENU <-----\n")
    return

            

# Define functione for the selection of diffrent menus.    

def selections(Option):

    # Option to register a new user.

    if Option == "r":
        reg_user()

    # Option to add a new task.

    elif Option == "a":
        add_task()

    # Option to view all tasks.

    elif Option == "va":
        view_all()

    # Option to view logged in users task.

    elif Option == "vm":
        view_mine(Username)

    # Option to generate reports.

    elif Option == "gr":
        generate_report()

    # Option to display reports to admin.

    elif Option == "ds":
        display_statistics()

    # To exit task manager back to login screen.
        
    elif Option == "e":
        return Option

# Declare login variable as false.

login_valid = False

while login_valid == False:

    # call login function and return username and if login is valid
    
    Username,login_valid = login()

    if login_valid == True:

        # While loop to ensure that program runs in a loop and.

        while True:

            # Call menu function and return option from menue.
            
            Option = menu(Username)

            # Call selection function and return option.

            Option = selections(Option)

            if Option == "e":

                # If the option retuened from the selection is 'e', exit to login function and begin again.
                
                login_valid = False
                break

# END
                
    


        





    
