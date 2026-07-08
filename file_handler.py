import os
l=["python","py","cpp","c++","java","c"]
x=["py","py","cpp","cpp","java","c"]
def navtotopic(topic):
	path=os.path.join(os.getcwd(),'solutions',topic.lower())
	os.makedirs(path,exist_ok=True)
	os.chdir(path)
def openandwrite(name,lang,code):
	if lang.lower() in l:
		lang=x[l.index(lang.lower())]
	with open(f"{name}.{lang}","w") as file:
		file.write(code)
		print("\n\nFILE ADDED.")
	return
	
