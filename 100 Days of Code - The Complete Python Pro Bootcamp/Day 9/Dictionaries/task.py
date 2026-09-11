programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}


my_dictionary = {"name": "John", "age": 36, "city": "New York"
                 ,"country": "USA"
                 ,"languages": ["English", "Spanish", "French"]
                 ,"hobbies": ["Reading", "Writing", "Coding"]
                 ,"is_married": False
                 ,"children": ["Older brother", "Younger sister"]
                 ,"pets": ["cat", "dog", "bird"]
                 ,"address": {"street": "123 Main St", "city": "New York", "state": "NY", "zip_code": "10001"}
                 ,"contact_info": {"email": "", "phone": "123-456-7890"}
                }
#
# for key in my_dictionary:
#     print(key, my_dictionary[key])
#
# print("-"*30)
#
# for val in my_dictionary.values():
#     print(val)
#
# print("-"*30)
#
# for key, val in my_dictionary.items():
#     print(key, val)
# print("-"*30)

my_dictionary["is_married"] = True
print(my_dictionary["is_married"])