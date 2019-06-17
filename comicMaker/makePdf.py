import img2pdf,os,os.path

class makePdf:

	def mangaLike(chapter):
		filename = chapter.replace('.','-')+".pdf"
		if os.path.exists(filename) and os.stat(filename).st_size!=0:
			#print("    "+filename+" already exists!")
			os.remove(filename)
			#return
		try:
			sortedlist=[]
			imagelist=[]
			for i in os.listdir('.'):
				if i.endswith(".jpg"):
					temp=int(i[i.find("page-")+5 : i.find(".jpg")])
					sortedlist.append(temp)
			sortedlist.sort()
			for i in sortedlist:
				imagelist.append(chapter.replace('.','-')+"_page-"+str(i)+".jpg")
			#print(imagelist)
			with open(filename, "wb") as f:
				f.write(img2pdf.convert([i for i in imagelist]))
			print("    "+filename+" saved!")
		except:
			#raise
			print("    Error while creating"+filename+"!")
			os.remove(filename)

	def readComicOnlineTo(chapter):
		filename = chapter.replace('.','-')+".pdf"
		if os.path.exists(filename) and os.stat(filename).st_size!=0:
			#print("    "+filename+" already exists!")
			os.remove(filename)
			#return
		try:
			with open(filename, "wb") as f:
				f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpg")]))

			print("    "+filename+" saved!")
		except:
			#raise
			print("    Error while creating"+filename+"!")
			os.remove(filename)

	def readComicsOnlineRu(chapter):
		filename = chapter.replace('.','-')+".pdf"
		if os.path.exists(filename) and os.stat(filename).st_size!=0:
			#print("    "+filename+" already exists!")
			os.remove(filename)
			#return
		try:
			with open(filename, "wb") as f:
				f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpg")]))

			print("    "+filename+" saved!")
		except:
			#raise
			print("    Error while creating"+filename+"!")
			os.remove(filename)