# Write a program that prompts the user to input number of calls and calculate the monthly telephone bills as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.

calls = int(input("Enter the number of calls you made: "))

if calls <= 100 and calls > 0:
    print("Your bill is 200 INR")
elif calls < 0:
    print("Your bill is 0 INR")
elif calls > 100 and calls <= 150:
    print("Your bill is", 200 + (0.6 * (calls - 100)), "INR")
elif calls > 150 and calls <= 200:
    print("Your bill is", 200 + (0.6 * 50) + (0.5 * (calls - 150)), "INR")
else:
    print("Your bill is", 200 + (0.6 * 50) + (0.5 * 50) +(0.4 * (calls - 150)), "INR")
