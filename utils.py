import hashlib
import os
import fileRepository

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def size(fname):
    return os.path.getsize(fname)

def formatAnnounceList(fileList): 
    message = "ANNOUNCE\n"
    for file in fileList:
        fileName = os.path.basename(file['fileName'])
        message += fileName + "\t" + str(file['size']) + "\t" + file['md5'] + "\n"

    return message
