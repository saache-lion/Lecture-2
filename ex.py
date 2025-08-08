#1
'''
fav_no = int(input("Enter your favorite number: "))
print("Your favorite number is: ", fav_no)
new_fav_no = fav_no * 2
print("Your new favorite number is: ", new_fav_no)
'''

#2
hobbies = input("Enter your hobbies separated by commas: ")
hobbies_list = hobbies.split(',')
for i, hobby in enumerate(hobbies_list, start=1):
    print(f"{i} I love {hobby}")


