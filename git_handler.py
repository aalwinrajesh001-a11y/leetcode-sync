import subprocess

def git_push(problem_name):
	try:
		commit_msg="SOLVED : "+problem_name
		print("\nADDING FILE...")
		subprocess.run(['git','add','.'],capture_output=True,text=True,check=True)
		print("\nFILE STAGED SUCCESSFULLY.")

		print("\nCOMMITING...")
		subprocess.run(['git','commit','-m',commit_msg],capture_output=True,text=True,check=True)
		print(f"\nSUCCESSFULLY COMMITED WITH COMMIT MESSAGE : '{commit_msg}' ")

		print("\nPUSHING TO GIT HUB...")
		subprocess.run(['git','push'],capture_output=True,text=True,check=True)
		print("\n\tSUCCESFULLY PUSHED.\n")
	except subprocess.CalledProcessError as e:
		print("\nAUTOMATION FAILED !")
		print(f"FAILED DURING EXCECUTION OF : {" ".join(e.cmd)}")
		print(f"\nEXIT CODE :{e.returncode}")
		print(f"\n ERROR  DETAILS :\n{e.stderr.strip()}")
		return False
	return True
