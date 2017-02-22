import os

for x,key in {{cookiecutter.env}}.items(): 
	a = './'+x
	os.makedirs(a)
	
	for z,zkey in key.items():
		q = a+'/'+zkey+'.dB'	
		f=open(q,"w+")
		f.close()
	
	
