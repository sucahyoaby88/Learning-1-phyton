arithmetics = ["9 + 99", "3801 - 2", "45 + 43"]

def main () :
    for arithmetic in arithmetics :
        item = arithmetic.split()
        num1 = int(item[0])
        num2 = int(item[2])
        op = item[1]
        if(op == '+') :
            x = num1 + num2
            x = str(x)
        elif(op == '-') :
            x = num1 - num2
            x = str(x)
        else : 
            print("Operator must + or -")
        
        num1 = str(num1)
        num2 = str(num2)
        fillchar = ' '
        line  = '-'

        if(len(num1) > len(num2)) :
            width = len(num1)
            space = width-1

            print(num1.rjust(width, fillchar))
            print(op+num2.rjust(space, fillchar))
            print(line.rjust(width, line))
            print(x.rjust(width, fillchar))        
            print('\n')

        elif(len(num1) < len(num2)) :
            width = len(num2)
            space = width+2

            print(num1.rjust(space, fillchar))
            print(op, num2.rjust(width, fillchar))
            print(line.rjust(space, line))
            print(x.rjust(space, fillchar))        
            print('\n')
        else :
            width = len(num2)
            space = width+2

            print(num1.rjust(space, fillchar))
            print(op, num2.rjust(width, fillchar))
            print(line.rjust(space, line))
            print(x.rjust(space, fillchar))        
            print('\n')
    
main()