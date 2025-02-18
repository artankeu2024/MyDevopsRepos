# this function allow you to choose randomly from the list of question in the baby simulator projet
# we are using the choice function from the random librairy


#  the while  loop it helps to repeat a task over and over while some condition is true 
syntax
# while bolean_condition: 
#     code(do something) ...
it can be combine with de else statement
else:
    do something diffrent


# while True :
#     print("hello") 

# this print any whole number less than 3number 
# number = 1
# while number <= 10:
#     if number % 2 == 0:
#         print(number)
#     number = number + 1
   

# answer = input("why is the sky blue ? ").strip().lower()
# while answer != "justbecause":
#     answer = input("why? : ").strip().lower()


# baby simulator he is going to ask you question until you said justbecause
questions = ["why is the sky blue", "why is there a face on the moon ?" , "where are all the dinosaurs ?" ]
question = choice(questions) # wew are leveraging the choice function here
answer = input(question).strip().lower()
while answer != "justbecause":
    answer = input("why? : ").strip().lower()

    