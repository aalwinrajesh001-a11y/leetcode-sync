"""Module for managing user terminal inputs for problem details and source code."""

# Dictionary mapping various language inputs to their standard file extensions
languages= {
        "python":"py",
        "py":"py",
        "cpp":"cpp",
        "c++":"cpp",
        "c plus plus":"cpp",
        "java":"java",
        "c":"c"
        }

topics = [ 'ARRAY' , 'STRINGS', 'LINKED LIST', 'TREE', 'GRAPH', 'DYNAMIC PROGRAMMING', 'HASH TABLE' ]

def basic_details() :
	
	"""
	Prompts the user for basic details about the LeetCode problem.

    	Validates that the problem name is not empty, the topic exists in the pre-defined
    	list, and the language is supported.

    	Returns:
        	tuple: A tuple containing:
            	- problem_name (str): The validated name of the problem.
            	- topic (str): The validated, uppercase topic name.
            	- language (str): The validated language string.
   	 """	
	
	problem_name = input( "\tPROBLEM NAME : " )
	while problem_name == "" or problem_name == " " :
		problem_name = input( "\tNAME CANNOT BE EMPTY. PLEASE ENTER A VALID NAME : " )

	topic = input( f"\tPROBLEM TOPIC\n{topics} : " ).upper()
	while topic not in topics :
		topic = input( f"\tINVALID ! PLEASE SELECT FROM THE LSIT \n\t{topics} : " ).upper()
	
	language = input( "\tLANGUAGE (PYTHON/CPP/JAVA) : " )

	while language not in languages :
		language = input( "INVALID !\nENTER A VALID LANGUAGE : " )
	
	return problem_name, topic, language

def input_code() :

	"""
	Prompts the user to input the solution code line-by-line.

    	The user signals the end of the input by typing 'END' on a new line.
    	Recursively prompts the user if the entered code block is empty.

    	Returns:
   	     tuple: A tuple containing:
        	    - code (str): The complete multi-line code string.
            	- n (int): The total number of lines entered.
    	"""


	print( "\n\nEnter the copied code here (Type 'END' in a new line when finished) : \n" )
	code = ""
	lines = []
	while True :
        	line = input()
        	if line.lower() == 'end' :
                	break
	        lines.append(line)
	code = "\n".join(lines)
	n = len(lines)

	if code == "" :
		print( "\n\nERROR! CODE CANNOT BE EMPTY " )
		code, n = input_code()

	return code, n

def check_details(name, topic, language, code) :

	"""
	Prints the gathered problem details and code snippet to the console for verification.

    	Args:
        	name (str): The name of the problem.
        	topic (str): The category/topic of the problem.
        	language (str): The programming language used.
        	code (str): The complete source code.

    	Returns:
        	None
   	 """

        print( f"\n\nDETAILS :\n\t PROBLEM NAME :{name}\n\t TOPIC : {topic}\n\t LANGUAGE : {language}\n\t CODE : \n{code} " )
