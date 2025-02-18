from random import choice
# this function allow you to choose randomly from the list of question in the baby simulator projet
# we are using the choice function from the random librairy

questions = ["why is the sky blue","why is there a face on the moon ?","where are all the dinosaurs ?" ]
question = choice(questions) # wew are leveraging the choice function here
answer = input(question).strip().lower()
while answer != "justbecause" :
    answer = input("why? : ").strip().lower()
    