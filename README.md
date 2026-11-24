# clx-cli
A basic calculator that works in the command terminal. The user should input an expression like 3+(4*3)/9 and the calculator will follow bodmas and ouptut the result. 

The calculator first directs the expresion (exp) to a parsing functino which identifies any parantheses block and evaulates them first using recursion logic. Then it updates the exp string and evaulates the rest of the exp.

The calculator is able to understand these symbols: %,^,*,**,(,),-,+,/

This was the first logic that hit my head and I decided to go with it as it would also help me revise recursive functions.

I used Gemini only to help me with the git commands to commit and push (I forgot them). All code is written by me.

23/11/26
Currently the calculator is able to compute an expression accurately (doesn't follow bodmas though!), provided that the final sum at any stage the result of an operation is not a 2 digit number, ie, you you give 6+7+3 it will go into an error because currently the logic checks only for a digit, operand, digit before evaulating and cannot handle 2 digits then an operand as it would go into error state.  
24/11/26
Made a new branch to test out some new parsing logic.