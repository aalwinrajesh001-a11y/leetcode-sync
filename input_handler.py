languages={
        "python":"py",
        "py":"py",
        "cpp":"cpp",
        "c++":"cpp",
        "c plus plus":"cpp",
        "java":"java",
        "c":"c"
        }

topics=['ARRAY', 'STRINGS', 'LINKED LIST', 'TREE', 'GRAPH', 'DYNAMIC PROGRAMMING', 'HASH TABLE']

def basic_details():

	problem_name=input("\tPROBLEM NAME : ")
	while problem _name=="" or problem_name==" ":
		problem_name=input("\tNAME CANNOT BE EMPTY. PLEASE ENTER A VALID NAME : ")

	topic=input(f"\tPROBLEM TOPIC\n{topics} : ").upper()
	while topic not in topics:
		topic=input(f"\tINVALID ! PLEASE SELECT FROM THE LSIT \n\t{topics} : ").upper()
	
	language=input("\tLANGUAGE (PYTHON/CPP/JAVA) : ")

	while language not in languages:
		language=input("INVALID !\nENTER A VALID LANGUAGE : ")
	
	return problem_name,topic,language

def input_code():

	print("\n\nEnter the copied code here (Type 'END' in a new line when finished) : \n")
	code=""
	lines=[]
	while True:
        	line=input()
        	if line.lower()=='end':
                	break
	        lines.append(line)
	code="\n".join(lines)
	n=len(lines)

	if code=="":
		print("\n\nERROR! CODE CANNOT BE EMPTY ")
		code,n=input_code()

	return code,n

def check_details(name,topic,language,code):
        print(f"\n\nDETAILS :\n\t PROBLEM NAME :{name}\n\t TOPIC : {topic}\n\t LANGUAGE : {language}\n\t CODE : \n{code} ")
