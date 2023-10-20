#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

while True:
    num= int(input("Enter an integer but it has to be specific or I will ask you again:"))
    if num%2 ==0:
        print ("You got it! The number had to be an even integer")
        break
    else: 
        print("Wrong try again.")