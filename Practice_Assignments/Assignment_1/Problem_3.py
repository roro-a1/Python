# Write a program to accept a 4 digit number and
# Display face value of each decimal digit
# Display place value of each decimal digit
# Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 output should be
# a. 9 3 6 1
# b. 9361 = 9 000 + 300 + 60 + 9
# c. 1639

a = int(input("Enter a 4 digit number: "))
f1 = a % 10
a = a // 10
f2 = a % 10
a = a // 10
f3 = a % 10
a = a // 10
f4 = a % 10
print(f4, f3, f2, f1)

a = f1 + f2*10 + f3*100 + f4*1000
print(a, "=", f4*1000, "+", f3*100, "+", f2*10, "+", f1)

print(f4 + f3*10 + f2*100 + f1*1000)

