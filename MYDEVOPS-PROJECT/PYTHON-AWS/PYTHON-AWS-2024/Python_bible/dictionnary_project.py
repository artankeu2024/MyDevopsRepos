# cinema Simulator

films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan":[15,5],
    "TheGhost":[12,5]
}
while True:
    choice = input("which film do you want to watch ?").strip().title()
    if choice in films:
        age = int(input("how old are you?").strip())
        if age >= films[choice][0] :
            ticket = int(input("how many ticket do you want please"))
            if ticket <= films[choice][1]:
                print("enjoy the film") 
                ticketR = films[choice][1] - ticket
                print(ticketR)
            else :
                print("we do not have enought ticket")
        else:
            print("you are too young ")
         
    else:
        print("we dont have that film")


# while True:
#     choice = input("which film do you want to watch ?").strip().title()
#     if choice in films:
#         pass 
#     else :
#         print("we dont have that film")














# 57209170 - 50500000
# = 6709000fcfa - 3681206 = 3027794- 2697794
