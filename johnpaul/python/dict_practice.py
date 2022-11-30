#Display numbers from -10 to -1 using for loop

# for num in range(-10, 0, 1):
#     print(num)

# Convert to dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# x = dict(zip(keys, values))
# print(x)

# empty_dict = {}
# for i in range(len(keys)):
#     empty_dict.update({keys[i]: values[i]})
# print(empty_dict)
#-----------------------------------------------------------------#
#Merge 2 dictionaries
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 20, 'Fourty': 40, 'Fifty': 50}
# new_dict = {**dict1, **dict2}
# print(new_dict)

#-----------------------------------------------------------------#
#print the value of history
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict['class']['student']['marks']['history'])
#-----------------------------------------------------------------#
# Print the value of key ‘history’ from the below dict
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# x = {employees[0]: defaults, employees[1]: defaults}
# print(x)


#-----------------------------------------------------------------#
#Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract keys = ["name", "salary"]
# keys = {"name": sample_dict['name'], "salary": sample_dict['salary']}
# print(keys)
#-----------------------------------------------------------------#
#Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# Keys to remove keys = ["name", "salary"]
# del sample_dict['name'], sample_dict['salary']
# print(sample_dict)

#-----------------------------------------------------------------#

#Write a Python program to check if value 200 exists in the following dictionary.
# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# for key, item in sample_dict.items():
#     if item == 500:
#         print(True)
#     else:
#         print(False)
#-----------------------------------------------------------------#
#Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(sample_dict, key=sample_dict.get))

#-----------------------------------------------------------------#

