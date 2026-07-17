import question
import os
def print_question():
    a=question.Que
    score=0
    que=0
    for q_no, data in a.items():
        print(f"\nQuestion {q_no}: {data['question']}")
        for option, value in data["options"].items():
            print(f"{option}. {value}")
        user_ipnut=input("Enter your option : ").upper()
        option=True
        while option:
            if user_ipnut in "ABCD":
                if user_ipnut==data["answer"]:
                    score+=1
                    que+=1
                    os.system('cls')
                    print(f"Your score is {score}/{que}")
                    option=False
                else:
                    que+=1
                    os.system('cls')
                    print(f"Your score is {score}/{que}")
                    option=False
            else:
                print("Please enter the given option from A to D")
                user_ipnut=input("Enter your option : ").upper()
    print(f"Your final score is {score}/{que} and you scored {(score/que)*100}%")        
    
        
print("*"*50)
print("       Welcome to the Quiz Game")
print("*"*50)
print()
print("*****This is the quiz of Python*****")
print_question()
