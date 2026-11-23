#stopping elements
stp = ['%','^','*','**',"(",')','-','+','/']
no = ['1','2','3','4','5','6','7','8','9','0']

#global result
res = 0

def parser(exp):
    #the current logic is to check for bodmas. And pass the relavant pair of numbers 
    #with the operand to a evaluater function

    

    #any hinderance???
    cur = ''
    #check for first ()
    '''
    #does not work at all
    
    if "(" in exp:
        
        fs_par = exp.index('(')
        ls_par = exp[::-1].index(')')
        cur+= exp[fs_par+1:4-ls_par]

    if cur!='':
        new = parser(cur)
        cur = cur[0:fs_par] + new + cur[ls_par+1:] 
    '''

    
    for i in exp:
        '''if i == "(":
            fs_par = exp.index('(')
            ls_par = exp[::-1].index(')')
            cur+= exp[fs_par:4-ls_par]
            return cur
        else: '''


        if exp[0] in no and exp[1] in stp and exp[2] in no:
            #print(exp)

            #to check if the exp is finished
            st = 0
            
            #res += evaluater(exp[0:3])
            #local var to store exp
            lvar =''
            lvar = exp[0:3]
            #print(exp)
            exp = exp[3:]
            #print(exp)

            res = str(evaluater(lvar))
            exp = res + exp

            
            

            for i in exp:
                if i not in stp:
                    st +=0
                else: 
                    st+=1


            if st == 0:
                #should return if no operand left
                return exp
            #add code to check if the exp is 5+5
            
        else: 
            #print(exp[0],exp[1],exp[2])
            error(exp)


def error(exp):
    pass
    #print(exp)
    #print("There's something wrong with your expression!")



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