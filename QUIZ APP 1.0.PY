
def ques_list():
    # Quiz questions as a list of dictionaries
    global quiz_questions
    quiz_questions = [
        {
            "question": "What does ACID stand for in the context of database transactions?",
            "options": ["A) Atomicity, Consistency, Isolation, Durability",
                        "B) Accuracy, Consistency, Integration, Dependency",
                        "C) Availability, Concurrency, Isolation, Durability",
                        "D) Atomicity, Concurrency, Isolation, Durability"],
            "answer": "A"
        },
        {
            "question": "Which SQL command is used to remove a table and all its data from a database?",
            "options": ["A) DROP", "B) DELETE", "C) REMOVE", "D) TRUNCATE"],
            "answer": "A"
        },
        {
            "question": "Which data structure uses LIFO (Last In First Out) principle?",
            "options": ["A) Queue", "B) Stack", "C) Linked List", "D) Tree"],
            "answer": "B"
        },
        {
            "question": "What is the time complexity of binary search?",
            "options": ["A) O(n)", "B) O(log n)", "C) O(n^2)", "D) O(n log n)"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a mutable data type in Python?",
            "options": ["A) Tuple", "B) String", "C) List", "D) Integer"],
            "answer": "C"
        },
        {
            "question": "What does the 'break' statement do in Python loops?",
            "options": ["A) Ends the current loop iteration", 
                        "B) Exits the loop", 
                        "C) Skips the current iteration", 
                        "D) Restarts the loop"],
            "answer": "B"
        },
        {
            "question": "Which of the following is the correct syntax for a function in Python?",
            "options": ["A) def functionName[]:", 
                        "B) function functionName():", 
                        "C) def functionName():", 
                        "D) def functionName{}:"],
            "answer": "C"
        },
        {
            "question": "In a relational database, what is a 'foreign key'?",
            "options": ["A) A key that uniquely identifies a record",
                        "B) A field in one table that links to a primary key in another table",
                        "C) A key that references another key in the same table",
                        "D) A field used for indexing records"],
            "answer": "B"
        },
        {
            "question": "What is the purpose of an index in a database?",
            "options": ["A) To ensure data integrity", 
                        "B) To improve query performance", 
                        "C) To enforce primary key constraints", 
                        "D) To store duplicate data"],
            "answer": "B"
        },
        {
            "question": "Which Python keyword is used to handle exceptions?",
            "options": ["A) catch", "B) error", "C) try", "D) except"],
            "answer": "C"
        }
    ]

def register():
    user=input("Enter Username :")
    pwd=input("Enter Password :")
    Users.append(user)
    Passwords[user]=pwd
    print("User successfully Registered")
    
def login():
    global Is_login
    global username
    user=input("Enter Username :")
    if user in Users:
        pwd=input("Enter Password :")
        if pwd == Passwords[user]:
            username=user
            print("login successfull")
            Is_login=True
        else:
            print("Invalid Password")
            print("Please Try Again With Correct Password")
            print()
            login()

    else:
        print("Invalid user ")
        print("Please Try Again")
        login()
    Is_login = True

def attempt():
    global Is_login
    global score 
    global Result
    global Is_attempt
    print(Is_login)
    if Is_login == True:
        print()
        ques_list()
        
        for ques in quiz_questions:
            
            print(ques["question"])
            for choice in ques["options"]:
                
                print(choice)
            print()
            ans=input("Enter your Choice : ").upper()
            if ans == ques["answer"]:
                
                score+=1
        Is_attempt=True
        
    else:
        print("You must be logined to attempt the question")

def result():
    if Is_login == True:
        if Is_attempt == True :
            print(f"Result of user {username.upper()} is {score}")
        else:
            print("you must first attempt the quiz")
            print()
            attempt()
    else:
        print("you must login first!!!")
        login()
Users=["abc"]
Passwords={"abc":"123"}
Result = {}
username =""
# global Is_login 
Is_login = False

#global Is_attempt 
Is_attempt = False
quiz_questions=[]
#global score
score=0
on = 1
while on == 1:
    print("---Select an option---")
    print("1.> Registration")
    print("2.> Login")
    print("3.> Attempt quiz")
    print("4.> Show Result ")
    print("5.> Exit")
    print()
    ch= int(input("Enter your Choice : "))
    if ch == 1:
            register()
            print()
            
    elif ch ==2:
            login()
            print()
    elif ch == 3:
            attempt()
            print()
    elif ch == 4:
        result()
        print()
    elif ch == 5 :
        on =0
        exit()
    else:
        print("invalid choice")     


