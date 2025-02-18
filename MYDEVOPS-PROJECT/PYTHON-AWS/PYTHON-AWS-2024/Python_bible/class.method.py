import random
# creating a class method
# we need a constructor 

class Pound:
# class constructor 
    def __init__(self, rare=False): #self is a aparameter . a constructor can have many parameters.
        
        self.rare = rare
        if self.rare: # or if self.rare == True:
            self.value = 1.25
        else :
            self.value = 1.00
        self.value = 1.00
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5 
        self.thickness = 3.25
        self.heads = True
    # destructor
    def __del__(self):
        print("Coin Spent")
    def rust(self):
        self.color = "greenish"
    
    def clean(self):
        self.color = "gold"
    
    def flip(self):
        options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice

