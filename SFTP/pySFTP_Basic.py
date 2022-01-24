import pysftp
 

Hostname = ""
Username = ""
Password = ""
hostkey = ""

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None   
 
sftp = pysftp.Connection(host=Hostname, username=Username, password=Password,  cnopts=cnopts)
print("Connection successfully established ... ")
 
#list items in directory
for i in sftp.listdir():
    print(i)
    
    localFilePath = r"C:\Users\kylej\Desktop\Python_KG_work\test.csv"
    print(localFilePath)
    sftp.get(i, localFilePath)

 

 
 
 
