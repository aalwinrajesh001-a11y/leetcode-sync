
import os

from input_handler import basic_details,input_code,check_details
from file_handler import addfile
from git_handler import git_push

print("\n\n\t\tLEETCODE-SYNC TOOL\n\n")

problem_name,topic,language=basic_details()
code,n=input_code()

os.system('clear')

print(f"\nSUCCESSFULLY ADDED {n} LINES OF CODE.")
cn=input("\nDo you want to Check or Push to github (C/P)? ")

os.system('clear')

if cn.lower()=='c':
	check_details(problem_name,topic,language,code)
	input("\nCLICK ENTER TO PROCEED ")
	os.system('clear')

addfile(topic,problem_name,language,code)

success=git_push(problem_name)
if success:
	print("\nDONE !")
else:
	print("\nERROR OCCOURED !")
