import os
from input_handler import basic_details,input_code,check_details
from file_handler import navtotopic,openandwrite
print("\n\n\t\tLEETCODE-SYNC TOOL\n\n")

p_name,topic,lang=basic_details()
code,n=input_code()

os.system('clear')

print(f"\nSUCCESSFULLY ADDED {n} LINES OF CODE.")
cn=input("\nDo you want to Check or Push to github (C/P)? ")

os.system('clear')

if cn=='C':
	check_details(p_name,topic,lang,code)
else:
	os.system('clear')
	navtotopic(topic)
	openandwrite(p_name,lang,code)
