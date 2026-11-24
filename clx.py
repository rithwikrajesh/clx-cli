#stopping elements
stp = ['%','^','*','**',"(",')','-','+','/']
no = ['1','2','3','4','5','6','7','8','9','0']

#global result
res = 0

def parser(exp):
    #Going to make new logic for parser

def error(exp):
    pass
    #print(exp)
    #print("There's something wrong with your expression!")

def checker(exp):
    #checks if the given expresssion is computable 
    inst = exp.index('%','^','*','**',"(",')','-','+','/')




def evaluater(exp):
    x = int(exp[0])
    y = int(exp[-1])
    op = exp[1]
    if op == '*':
        return x*y
    elif op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == '**' or op =="^":
        return x**y
    elif op == '%':
        return x%y
    else:
        return x/y




def main():
    print("==================================================================")
    print("Welcome to clx-cli, your personal command line based calculator.")
    print("Type in your expression and I'll solve it up for ya!")
    print("==================================================================")

    exp = input(">>>")

    print(parser(exp))
    

if __name__ == "__main__":
    main()