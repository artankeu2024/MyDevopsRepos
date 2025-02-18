
# slicing syntax
# variable [start:end:step]

email = input("what is your email address? : ").strip()
user= email[:email.index("@gmail")]
print(user)
domain = email[email.index("gmail"):]
# or domaine = email[email[.index("@")+1:]
print(domain)

output = "your username is {} and your domaine name is {}".format(user,domain)
print(output)


#