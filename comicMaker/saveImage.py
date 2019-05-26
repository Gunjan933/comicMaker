from .checkProgress import checkProgress
from .imageConverter import imageConverter
import os,os.path,time,requests

def saveImage(url,chapter,pageNum):
	try:
		filename = chapter.replace('.','_')+"_"+pageNum+".jpg"
		if os.path.exists(filename) and os.stat(filename).st_size!=0:
			print("    "+filename+" already exists!")
			return
		r = requests.get(url, allow_redirects=True)
		open(filename, 'wb').write(r.content)
		checkProgress(url,filename)
	except:
		print("Could not connect, Trying again!")
		time.sleep(10)
		saveImage(url,chapter,pageNum)
		return
	else:
		imageConverter(filename)
		print("    "+filename+" saved!")
