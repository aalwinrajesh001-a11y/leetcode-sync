
from pathlib import Path

languages={
	"python":"py",
	"py":"py",
	"cpp":"cpp",
	"c++":"cpp",
	"c plus plus":"cpp",
	"java":"java",
	"c":"c"
	}

def addfile(topic,name,language,code):

	name=name.lower()
	name=name.replace(" ",'_')

	language=languages.get(language)

	file_name=name+"."+language


	path=Path.cwd()/ 'solutions'/ topic/ file_name
	path.parent.mkdir(parents=True, exist_ok=True)
	print("\nFILE CREATED.")

	path.write_text(code,encoding="utf-8")
	print("\nCODE ADDED IN FILE.")

	return
