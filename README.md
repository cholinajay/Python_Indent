# Python_Indent
This Project is about detecting the indentation error of a python code and getting the line number of the place where error is detected.



# Course Mini Project Problem Statement: To implement an indentation error detector for Python 
 
 
 
# Abstract: 
The project intends to detect indentation errors in Python which is one of the most common errors that occur while writing code in Python. 
 
 
The syntax of a language is the set of rules that define what parts of the language can appear in which places. If you insert tab A into slot B, so to speak, you'll create a statement that has invalid syntax. Because there are lots of slots in Python that don't accept most tabs, generating a syntax error is not hard. 
 
 
Indentation of program statements is critical to the readability of code. Python enforces it with an iron fist. Therefore it is critical to detect inconsistent indentation. With this in mind, our project aims to detect errors in indentation for Python. The code for the  same has been implemented in Python.	 

The Following steps were taken: 
 
 
 1)Preprocessing 
 
❏ The python code was preprocessed by first removing the EOL(End Of Line ‘\n’) ❏ Then  each line of the code was read into a python list. 
 
 2)Error Checking 
❏ Then for each element in a list: 
❏ Checking was done to see whether there are any keywords that had a possibility of indentation. 
❏ If any indentation isn’t matching , then error was thrown. 
❏ It is repeated for the whole program. 
❏ For nested indentations, the concept of scope was introduced. 
❏ For each outer indentation scope is always 1 
❏ Scope is incremented for each level of indentation. 
 
 
 3) Output 
❏ Once error is detected , corresponding Line Number is printed to indicate indentation error at that line. 
 
 
 Test Cases :  
 
The error checking was tested for various cases, which include  
1.	if 
2.	If-else 
3.	Simple Function definitions 
4.	Nested if-else 
5.	Nested function definitions 
 
 
 
# Example: 
 
1) Nested if-else 
 
Input: 
 if(a>b): 
 	a=10  	b=20  	if(c>20): 
 	c=10 
                      b=10   // Note that there is inconsistent indentation at this point 
 	a=20 
 	print("End of inner if")  	else: 
 	a=20  	b=15 
 	c=45 
 	print("End of else") 
 	print("End of outer if") a=25 sum = a+b 
 
 
 
Output: 
 
(‘INDENT error at line no’,6) 
 
2) Nested function definitions 
 
Input: 
 
def manhattan_distance(start, end): 
 	sx, sy = start  	ex, ey = end  	def fun(a): 
 	a=20 
                      a=10  // Note that there is inconsistent indentation at this point 
 	return a 
 	return abs(ex - sx) + abs(ey - sy) 
 
Output: 
 
(‘INDENT error at line no’,6) 


Course Mini Project Problem Statement: To implement an indentation error detector for Python 
 
 
 
Abstract: 
The project intends to detect indentation errors in Python which is one of the most common errors that occur while writing code in Python. 
 
 
The syntax of a language is the set of rules that define what parts of the language can appear in which places. If you insert tab A into slot B, so to speak, you'll create a statement that has invalid syntax. Because there are lots of slots in Python that don't accept most tabs, generating a syntax error is not hard. 
 
 
Indentation of program statements is critical to the readability of code. Python enforces it with an iron fist. Therefore it is critical to detect inconsistent indentation. With this in mind, our project aims to detect errors in indentation for Python. 
  
    The code for the  same has been implemented in Python.	 
 
 
 
 
 
 
 
The Following steps were taken: 
 
 
1)Preprocessing 
 
❏ The python code was preprocessed by first removing the EOL(End Of Line ‘\n’) ❏ Then  each line of the code was read into a python list. 
 
2)Error Checking 
❏ Then for each element in a list: 
❏ Checking was done to see whether there are any keywords that had a possibility of indentation. 
❏ If any indentation isn’t matching , then error was thrown. 
❏ It is repeated for the whole program. 
❏ For nested indentations, the concept of scope was introduced. 
❏ For each outer indentation scope is always 1 
❏ Scope is incremented for each level of indentation. 
 
 
3) Output 
❏ Once error is detected , corresponding Line Number is printed to indicate indentation error at that line. 
 
 
Test Cases :  
 
The error checking was tested for various cases, which include  
1.	if 
2.	If-else 
3.	Simple Function definitions 
4.	Nested if-else 
5.	Nested function definitions 
 
 
 
Example: 
 
1) Nested if-else 
 
Input: 
 if(a>b): 
 	a=10  	b=20  	if(c>20): 
 	c=10 
                      b=10   // Note that there is inconsistent indentation at this point 
 	a=20 
 	print("End of inner if")  	else: 
 	a=20  	b=15 
 	c=45 
 	print("End of else") 
 	print("End of outer if") a=25 sum = a+b 
 
 
 
Output: 
 
(‘INDENT error at line no’,6) 
 
2) Nested function definitions 
 
Input: 
 
def manhattan_distance(start, end): 
 	sx, sy = start  	ex, ey = end  	def fun(a): 
 	a=20 
                      a=10  // Note that there is inconsistent indentation at this point 
 	return a 
 	return abs(ex - sx) + abs(ey - sy) 
 
Output: 
 
(‘INDENT error at line no’,6) 
 
 
Course Mini Project Problem Statement: To implement an indentation error detector for Python 
 
 
 
Abstract: 
The project intends to detect indentation errors in Python which is one of the most common errors that occur while writing code in Python. 
 
 
The syntax of a language is the set of rules that define what parts of the language can appear in which places. If you insert tab A into slot B, so to speak, you'll create a statement that has invalid syntax. Because there are lots of slots in Python that don't accept most tabs, generating a syntax error is not hard. 
 
 
Indentation of program statements is critical to the readability of code. Python enforces it with an iron fist. Therefore it is critical to detect inconsistent indentation. With this in mind, our project aims to detect errors in indentation for Python. 
  
    The code for the  same has been implemented in Python.	 
 
 
 
 
 
 
 
The Following steps were taken: 
 
 
1)Preprocessing 
 
❏ The python code was preprocessed by first removing the EOL(End Of Line ‘\n’) ❏ Then  each line of the code was read into a python list. 
 
2)Error Checking 
❏ Then for each element in a list: 
❏ Checking was done to see whether there are any keywords that had a possibility of indentation. 
❏ If any indentation isn’t matching , then error was thrown. 
❏ It is repeated for the whole program. 
❏ For nested indentations, the concept of scope was introduced. 
❏ For each outer indentation scope is always 1 
❏ Scope is incremented for each level of indentation. 
 
 
3) Output 
❏ Once error is detected , corresponding Line Number is printed to indicate indentation error at that line. 
 
 
Test Cases :  
 
The error checking was tested for various cases, which include  
1.	if 
2.	If-else 
3.	Simple Function definitions 
4.	Nested if-else 
5.	Nested function definitions 
 
 
 
Example: 
 
1) Nested if-else 
 
Input: 
 if(a>b): 
 	a=10  	b=20  	if(c>20): 
 	c=10 
                      b=10   // Note that there is inconsistent indentation at this point 
 	a=20 
 	print("End of inner if")  	else: 
 	a=20  	b=15 
 	c=45 
 	print("End of else") 
 	print("End of outer if") a=25 sum = a+b 
 
 
 
Output: 
 
(‘INDENT error at line no’,6) 
 
2) Nested function definitions 
 
Input: 
 
def manhattan_distance(start, end): 
 	sx, sy = start  	ex, ey = end  	def fun(a): 
 	a=20 
                      a=10  // Note that there is inconsistent indentation at this point 
 	return a 
 	return abs(ex - sx) + abs(ey - sy) 
 
Output: 
 
(‘INDENT error at line no’,6) 
 
 
#  Literature: 
https://docs.python.org/2.0/ref/indentation.html 




# Requirements

->Python == 3.5 and above 



========
Input


Please change the input file to be executed in the code (indent.py)
=======

===========
Execution


python indent.py

==========

Output


       if Indentation Error:
          Prints "line no" where error occured 
       else:
          prints "All ok"

=========


 

