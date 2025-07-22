# Dictionary in Python - Dictionaries are used to store data values in key:value pairs.
# They are unordered, mutable(changeable) & don't allow duplicate keys.
"""
info = {
    "Name" : "Job",
    "Roro" : "DE",
    "Naks" : "SE",
    "ApeX" : "SDE"
}
print(info)
print("Naks is", info["Naks"])

info["Naks"] = "GDE"
print(info)
info["Shraddha"] = "teacher"
print(info)
"""
# Note - We can assign a key its own dictionary. i.e. - {"Sub" : {"phy : 90, "chem" : 88, "math" : 99}}. To print this - print(dic["Sub"]["chem"]) -- 88

# Dictionary Methods
"""
info = {
    "Name" : "Job",
    "Roro" : "DE",
    "Naks" : "SE",
    "ApeX" : "SDE"
}
print(info.items()) # Returns all pairs from dictionaries.
print(info.keys()) # Return all key from dictionary.
print(info.values()) # Return all values from dictionary.
print(list(info.keys())) # Type cast is possible.
print(list(info.values()))
print(list(info.items()))
print(info.get("Naks")) # Returns the value according to key entered
print(info.get("Shraddha")) # It doesn't throw error even if key does not exist - Returns "None"
# print(info["Shraddha"]) - Throws error as key doesn't exist in dictionary
info.update({"Shraddha" : "Teacher"}) # Insert the specified item to the dictionary.
print(info)
"""

# Set in Python - Set is the collection of the unordered items
# Each element in the set must be unique & immutable, but set itself is mutable
"""
roro = {24, 24, 6.5, "Naks", "Data Engineer", "O & M"}
print(roro)
print(type(roro))
naks = set() # Empty set
"""

# Set Methods
"""
roro = {24, 24, 6.5, "Naks", "Data Engineer", "O & M"}
print(roro)
roro.add("ApeX") # Inserts the value given in set.
print(roro)
roro.remove("ApeX")  # Removes given value from set
print(roro)
roro.pop() # Removes any random element from set
print(roro)
roro.clear() # Empty out the set.
print(roro)

naks = {23, "Roro", "Microsoft", 5, "Software engineer", 24}
print(roro.union(naks)) # Combines both set values and returns new
print(roro.intersection(naks)) # Combines common values and returns new
"""

# Practice
# Store the following word meanings in a python dictionary - table : "a piece of furniture", "list of facts & figures" cat: "a small animal"
"""
dictionary = {"cat" : "a small animal", "table" : ["a piece of furniture", "list of facts & figures"]}
print(dictionary)
"""

# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
"""
subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(subjects))
"""

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as values.
"""
marks = {}
x = int(input("Enter phy marks: "))
y = int(input("Enter chem marks: "))
z = int(input("Enter math marks: "))
marks.update({"Phy" : x})
marks.update({"Chem" : y})
marks.update({"Math" : z})
print(marks)
"""

# Figure out a way to store 9 & 9.0 as separate values in the set.
"""
nines = {9, "9.0"}
print(nines)
nine = {("float", 9.0), ("int", 9)}
print(nine)
"""

