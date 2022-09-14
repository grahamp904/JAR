
import requests
import os
import zipfile

def dload_PA(url,fname,localpath):

  #Remote info
  r_file = fname
  r_url = url + r_file
  
  
  #Local Info
  l_filename = os.path.join(localpath, r_file)
   
   
  r = requests.get(r_url, stream = True)
  with open(l_filename, "wb") as PyZip:
    for chunk in r.iter_content(chunk_size = 1024):
      if chunk:
        PyZip.write(chunk)
  
  
def dload_Tax(server, directory, fname, localpath):
  from ftplib import FTP
 
#Remote info
  r_server = server
  r_directory =directory
  r_file = fname

#Local Info
  l_directory = localpath
  l_filename = os.path.join(l_directory, r_file)

# Open Connection to Server
  ftp = FTP(server)
  ftp.login()
  ftp.cwd(r_directory)

#Download file
  gFile = open(l_filename, "wb")
  ftp.retrbinary("RETR " + r_file, gFile.write)
  gFile.close()

  ftp.quit()




def Unzipper(fname, target):
  with zipfile.ZipFile(fname,"r") as zip_ref:
      zip_ref.extractall(target)






