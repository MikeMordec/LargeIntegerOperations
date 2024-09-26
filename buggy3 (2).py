'''
CSC 157
Discussion 2:
Program 3
'''

def main():
    largeInteger = int(34389340934938)
    resultString = ""
    result = 0
    print("The value of largeInteger is: ", largeInteger)
    print("Please choose from one of the following options and enter your choice (1, 2, or 3).")
    print("1: divide largeInteger by 2.")
    print("2: divide largeInteger by 3.")
    print("3: mod the largeInteger by 9.")
    choiceOp = int(input("Enter choice: "))
    match choiceOp:
        case 1:
            result = largeInteger/2
            resultString = "Your result after dividing by 2: "
        case 2:
            result = largeInteger/3
            resultString = "Your result after dividing by 3: "
        case 3:
            result = largeInteger%9
            resultString = "Your result after moding by 9: "
    print(resultString, result) 
main()
