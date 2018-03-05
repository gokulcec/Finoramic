import json
import subprocess
from pprint import pprint

with open("depends.json") as fd:
	data = json.load(fd)

	lst = []
	for Module  in data ['Dependencies']:
		try :
			subprocess.check_call('pip install ' + Module, shell = True)
		except subprocess.CalledProcessError :
 			lst.append(Module)

	if not lst:
		print('Congrts All packages installed successfully')
	else:
		print('Sorry the following packages not installed, try again later')
		pprint(lst)
