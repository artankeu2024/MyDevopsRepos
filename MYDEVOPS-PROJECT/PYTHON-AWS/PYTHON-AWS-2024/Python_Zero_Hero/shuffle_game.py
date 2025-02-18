from random import shuffle

example = [1,2,3,4,5]

shuffle(example)
print(example)

mylist = ["","O",""]

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist 

result = shuffle_list(example)
print(result)

#Guessing where is the ball

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input("Pick a number : 0,1 or 2:  ")
    return int(guess)

# player_guess()
# Pick a number: 0, 1, or 2:  1
# 1
# Now we will check the user's guess. Notice we only print here, since we have no need to save a user's guess or the shuffled list.

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
        print('Wrong! Better luck next time')
        print(mylist)
#Now we create a little setup logic to run all the functions. Notice how they interact with each other!

# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixedup_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()
# Check User's Guess
#------------------------
# Notice how this function takes in the input 
# based on the output of other functions!
check_guess(mixedup_list,guess)
