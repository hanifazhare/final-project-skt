import xmlrpc.client
import threading

mainServer = xmlrpc.client.ServerProxy("http://127.0.0.1:8889")

flagFile = False

while True:
	print("Menu :")
	print("1. Buat file")
	print("2. Edit file")
	print("3. Hapus file")
	print("4. Lihat isi dalam file")
	print("5. List file")
	print("0. Keluar")
	jawab = input("Pilih = ")
	
	try:
		valJawab = int(jawab)
		if(valJawab == 1):
			print("List file :")
			listTask = mainServer.reqList()
			print(listTask, "\n")
			nameFile = input("Nama file : ")
			createTask = mainServer.reqCreate(nameFile)
			if(createTask == 0):
				print("File " + nameFile + " telah dibuat!\n")
			else:
				print("File " + nameFile + " sudah ada!\n")
		elif(valJawab == 2):
			print("List file :")
			listTask = mainServer.reqList()
			print(listTask, "\n")
			nameFile = input("Nama file : ")
			for i, j in enumerate(listTask):
				if j == nameFile:
					flagFile = True
			if(flagFile == True):
				dataFile = input("Input data kedalam file :\n")
				editTask = mainServer.reqEdit(nameFile, dataFile)
				if(editTask == 0):
					print("File " + nameFile + " telah diedit!\n")
			else:
				print("File " + nameFile + " tidak ada dalam directory!\n")
		elif(valJawab == 3):
			print("List file :")
			listTask = mainServer.reqList()
			print(listTask, "\n")
			nameFile = input("Nama file : ")
			deleteTask = mainServer.reqDelete(nameFile)
			if(deleteTask == 0):
				print("File " + nameFile + " telah dihapus!\n")
			else:
				print("File " + nameFile + " tidak ada dalam directory!\n")
		elif(valJawab == 4):
			print("List file :")
			listTask = mainServer.reqList()
			print(listTask, "\n")
			nameFile = input("Nama file : ")
			lookInsideTask = mainServer.reqLookInside(nameFile)
			if(lookInsideTask == 1):
				print("File " + nameFile + " tidak ada dalam directory!\n")
			else:
				print("Isi file :\n" + lookInsideTask + "\n")
		elif(valJawab == 5):
			print("List file :")
			listTask = mainServer.reqList()
			print(listTask, "\n")
		elif(valJawab == 0):
			break
		else:
			print("Input yang Anda masukkan tidak tersedia!\n")
	except ValueError:
		print("Input yang Anda masukkan harus berupa angka!\n")