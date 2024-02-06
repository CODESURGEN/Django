def abbrevations(first_name , middle_name , last_name):
    return first_name[0] + "." + middle_name[0]+ "." + last_name

# first_name = input("Enter your first name: ")
# middle_name = input("Enter your middle name: ")
# last_name = input("Enter your last name: ")
# print(abbrevations(first_name , middle_name , last_name))

def remove_consonants(strings):
    consonats = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result = ""
    for char in strings:
        if char not in  consonats:
            result += char
    return result

# print(remove_consonants("Hello, have a good day"))

def find_all_occurencies(strings,  letter):
    result = []
    for i in range(len(strings)):
        if strings[i] == letter:
            result.append(i)
    return result
# print("The letter 'a' is found at index: ", find_all_occurencies("Hello, have a good day", "a"))

def replace_to_dollar(strings):
    x = strings[0]
    result = strings.replace(x, "$")
    result = x + result[1:]
    return result

# print(replace_to_dollar("MalyalaM"))

def append_middle(str1 , str2):
    middle = len(str1) // 2
    result = str1[:middle] + str2 + str1[middle:]
    return result

# print(append_middle("Door", "Knob"))    

print("{}".format(1))
print(type("{}".format(1)))
 