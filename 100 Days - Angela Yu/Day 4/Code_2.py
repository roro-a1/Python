# Lists

states_of_india = ["Maharashtra", "Gujarat", "UP", "MP", "Bihar"]
"""
print(states_of_india[0]) # Index start with 0 - Maharashtra
print(states_of_india[2]) # UP
print(states_of_india[-2]) # MP by negative indexing.

states_of_india[0] = "MH"
print(states_of_india)

states_of_india.append("Roroland")
print(states_of_india)

states_of_india.extend(["Angelaland", "Nihari"])
print(states_of_india)
"""

#IndexError: list index out of range
"""
print(len(states_of_india))
print(states_of_india[6]) 
"""

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

combined_list = [states_of_india, friends]
print(combined_list)