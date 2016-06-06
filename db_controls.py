import dropbox
import os

class DboxControls:

    def __init__(self, fd):
        self.fd = fd
        self.app_key = 'nr50tr1twzdes0d'
        self.app_secret = 'wvnyh40zzd9n78h'
        self.flow = dropbox.client.DropboxOAuth2FlowNoRedirect(self.app_key, self.app_secret)
        print self.flow
        self.init()
    
    def init(self):
        # Have the user sign in and authorize this token
        authorize_url = self.flow.start()
        
        self.client = dropbox.client.DropboxClient("e0Pw41UZ5OIAAAAAAAAAqL6vtkjL1nKutPWGzFACryGLzcHDBb4ndZlC98t5IOae")
        self.delete("test.txt")
        self.upload("test.txt")
        
        print self.list_folder("/")
        
        
    def upload(self, fname):
        try:
            file = open("assets/" + fname, "r")
            path = os.path.join("/", fname)
            upl = self.client.put_file(path, file) 
            print "uploaded ", upl
        except:
            print "Error upload"
        pass
    
    def list_folder(self, folder):
        if folder:
            f_meta = self.client.metadata(folder)
        else:
            f_meta = self.client.metadata("/")
        return f_meta
    
    def delete(self, name):
        try:
            delf=self.client.file_delete("/"+name)
            print "Deleted ",name
        except:
            print "Error delete"
    
    def download(self,name,outName):
        try:
            
            file,metadata=self.client.get_file_and_metadata(name)
            out=open('assets/'+outName,'wb')
            out.write(file.read())
            out.close()
            return True
        except:  
            return False
            
        
    
