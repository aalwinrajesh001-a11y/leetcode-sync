
"""Module for automating Git version control workflows, including staging, committing, and pushing."""

import subprocess

def git_push( problem_name ) :

	"""
	Automates the process of adding, committing, and pushing a solved problem to GitHub.

    	This function executes `git add .`, followed by a commit with a message 
    	formatted as 'SOLVED : {problem_name}', and finally executes `git push`.
    	If any Git command fails, it catches the exception and logs the process details.

    	Args:
        	problem_name (str): The name of the LeetCode problem being pushed.

    	Returns:
        	bool: True if the entire Git workflow completed successfully, False otherwise.
    	"""

	try :
		commit_msg = "SOLVED : " + problem_name
		print( "\nADDING FILE..." )
		subprocess.run( [ 'git','add' ,'.' ], capture_output = True, text = True , check = True )
		print( "\nFILE STAGED SUCCESSFULLY." )

		print( "\nCOMMITING..." )
		subprocess.run( [ 'git', 'commit', '-m' , commit_msg ], capture_output = True, text = True , check = True )
		print( f"\nSUCCESSFULLY COMMITTED WITH COMMIT MESSAGE : '{commit_msg}' " )

		print( "\nPUSHING TO GIT HUB..." )
		subprocess.run( [ 'git', 'push' ], capture_output = True, text = True, check = True )
		print( "\n\tSUCCESFULLY PUSHED.\n" )
	except subprocess.CalledProcessError as e :
		print( "\nAUTOMATION FAILED !" )
		print( f"FAILED DURING EXECUTION OF : {" ".join(e.cmd)}" )
		print( f"\nEXIT CODE :{e.returncode}" )
		print( f"\n ERROR  DETAILS :\n{e.stderr.strip()}" )
		return False
	return True
