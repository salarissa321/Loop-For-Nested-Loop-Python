

#-------------------------------------------------
#-------- Loop => for --------
#--------Nested Loop----------
#---------------------------------------------------



# peoples = ["Salar" , "Gamel" , "Raman" , "Shergo"]

# skills = ["Html" , "Css" , "Js"]

# for person in peoples : # Outer Loop

#     # print(person) # Salar , Gamel , Raman , Shergo
#     print(f"{person} Skills is ") # Salar Skills is  # Raman Skills is # Gamel Skills is # Shergo Skills is 

#     for skill in skills : # inner Loop
#         print(skill) # Html , Css , Js


peoples = {
    "Salar" : {
        "Html" : "70%" , 
        "Css" : "80%" , 
        "Js" : "50%"
    },
    "Raman" : {
        "Html" : "80%" , 
        "CSs" : "50%" ,
        "Js" : "30%"
    },
    "Gamel" :{
        "Html" :"80%" ,
        "Css" : "70%" ,
        "Js" : "30%"
    }
}

# print(peoples["Salar"]) #  {'Html': '70%', 'Css': '80%', 'Js': '50%'}
# print(peoples ["Salar"] ["Css"]) # 80%
# print(peoples["Gamel"] ["Html"]) # 80%

for person in peoples:
    
    # print(person) # Salar , Raman , Gamel
    # print(f"SKills and Progress for {person} is : {peoples[person]}") # SKills and Progress for Salar is : {'Html': '80%', 'CSs': '50%', 'Js': '30%'} # SKills and Progress for Raman is : {'Html': '80%', 'CSs': '50%', 'Js': '30%'} # SKills and Progress for Gamel is : {'Html': '80%', 'Css': '70%', 'Js': '30%'}
    # print(f"{peoples[person]}") # {'Html': '70%', 'Css': '80%', 'Js': '50%'} , {'Html': '80%', 'CSs': '50%', 'Js': '30%'} , {'Html': '80%', 'Css': '70%', 'Js': '30%'}
    print(f"Skills and progress for {person} is : ") # 
    for skill in peoples[person] :
        # print(skill) # Html , CSs , JS
        print(f"{skill} => {peoples[person][skill]}") # 

# Skills and progress for Salar is :      
# Html => 70%
# Css => 80%
# Js => 50%
# Skills and progress for Raman is :
# Html => 80%
# CSs => 50%
# Js => 30%
# Skills and progress for Gamel is :
# Html => 80%
# Css => 70%
# Js => 30%



 