from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os

mainServer = SimpleXMLRPCServer(("0.0.0.0", 8889))
secondaryServer = xmlrpc.client.ServerProxy("http://127.0.0.1:8890")

dirName = "Source Data"
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " + dirName + " telah dibuat!")
else:    
    print("Directory " + dirName +  " sudah ada!")

listFileDB = os.listdir("./" + dirName)

def req_create(name):
	pathDataFolder = os.path.join(dirName, name)
	if not os.path.exists(pathDataFolder):
		open(pathDataFolder, 'w')
		print("File " + name + " telah dibuat!")
		listFileDB.append(name)
		secondaryServer.reqCreate(name)
		return 0
	else:
		return 1

def req_edit(name, data):
	pathDataFolder = os.path.join(dirName, name)
	with open(pathDataFolder, 'a') as f:
		f.write(data + "\n")
	print("File " + name + " telah diedit!")
	secondaryServer.reqEdit(name, data)
	return 0

def req_delete(name):
	pathDataFolder = os.path.join(dirName, name)
	if os.path.exists(pathDataFolder):
		os.remove(pathDataFolder)
		print("File " + name + " telah dihapus!")
		secondaryServer.reqDelete(name)
		for i, j in enumerate(listFileDB):
			if j == name:
				listFileDB.pop(i)
		return 0
	else:
		return 1

def req_look_inside(name):
	pathDataFolder = os.path.join(dirName, name)
	if os.path.exists(pathDataFolder):
		with open(pathDataFolder, 'r') as f:
			contentFile = f.read()
		return contentFile
	else:
		return 1

def req_list():
	return listFileDB

mainServer.register_function(req_create, "reqCreate")
mainServer.register_function(req_edit, "reqEdit")
mainServer.register_function(req_delete, "reqDelete")
mainServer.register_function(req_look_inside, "reqLookInside")
mainServer.register_function(req_list, "reqList")
mainServer.serve_forever()