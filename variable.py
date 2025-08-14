
usernames= ["ellie","john","fils","fiston","manuel","gift","pixie","peter"]
userinput= input("enter your name to log in")
password =
valid = ""
for i in usernames:
    if userinput in usernames:
        valid += f"welcome{userinput}"
        break
    else:    
         valid+= (f"{userinput} Not recognised")
    break
print(valid)  




