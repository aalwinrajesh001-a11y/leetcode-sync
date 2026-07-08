import subprocess

def git_push(problem):
	commit_msg="SOLVED : "+problem
	print("\nADDING FILE...")
	subprocess.run(['git','add','.'])
	print("\nCOMMITING...")
	subprocess.run(['git','commit','-m',commit_msg])
	print("\nPUSHING TO GIT HUB...")
	subprocess.run(['git','push'])
	print("\n\tSUCCESFULLY PUSHED.\n")
	return
