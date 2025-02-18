# get sentence from user

original = input("enter your sentence here please ! ").strip().lower()

# split the sentence to a single word
words = original.split()
#print(words)


#loop  through words and convert to pig latin
new_words = []
for word in words:
   # print (word)
    voyell = ["a","e","u","i","o","y"]
    if word[0] in voyell:
        new_word = word + "yay"
        new_words.append(new_word)

    else :
        vowel_pos = 0
        for letter in word:
            if letter not in voyell:
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)
    

# if it starts with vowel, jsut add "yay"

# otherwise, move the first consonant cluster to end , and add "ay"



#stick words back together

output = " ".join(new_words)
#output the final string
print(output)
