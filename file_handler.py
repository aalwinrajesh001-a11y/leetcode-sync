
"""Module for handling file creation and writing code solutions to disk."""

from pathlib import Path

# Dictionary mapping various language inputs to their standard file extensions
languages = {
	"python":"py",
	"py":"py",
	"cpp":"cpp",
	"c++":"cpp",
	"c plus plus":"cpp",
	"java":"java",
	"c":"c"
	}

def create_solution_file( topic, name, language, code ) :

	"""
	Creates a directory structure for a topic and writes the solution code to a file.

	The file name is formatted to lowercase with underscores replacing spaces.
	The file is saved under the 'solutions/{topic}/' directory.

	Args:
		topic (str): The data structure or algorithmic topic (e.g., 'ARRAY').
        	name (str): The name of the LeetCode problem.
        	language (str): The programming language used for the solution.
        	code (str): The source code of the solution.

	Returns:
        	None
    	"""

	name = name.lower()
	name = name.replace( " ", '_' )

	language = languages.get( language )

	file_name = name + "." + language


	path = Path.cwd() / 'solutions'/ topic / file_name
	path.parent.mkdir( parents = True, exist_ok = True )
	print( "\nFILE CREATED." )

	path.write_text( code, encoding = "utf-8" )
	print( "\nCODE ADDED IN FILE." )

	return
