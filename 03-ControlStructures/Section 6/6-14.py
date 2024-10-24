
##
# Write a program that checks whether a given person is a good influencer,
#  that is, whether the person has at least two of the following accounts: Facebook, Twitter or Instagram.
##

count = 0
facebook = str(input("Does influencer have Facebook account? (yes/no) : "))
if facebook == "yes" : 
    facebook = True
    count += 1
elif facebook == "no" : 
    facebook = False
twitter = str(input("Does influencer have Twitter account? (yes/no) : "))
if twitter == "yes" : 
    twitter = True
    count += 1
elif twitter == "no" : 
    twitter = False
instagram = str(input("Does influencer have Instagram account? (yes/no) : "))
if instagram == "yes" : 
    instagram = True
    count += 1
elif instagram == "no" : 
    instagram = False
print(f"Facebook = {facebook}")
print(f"Twitter = {twitter}")
print(f"Instagram = {instagram}")
if count >= 2 :
    print("You are a good influencer!")
else :
    print("You are not a good influencer!")











facebook, twitter, instagram