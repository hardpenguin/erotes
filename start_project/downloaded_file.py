import urllib

class DownloadedFile(object): # file to be downloaded from a specified URL
    
    def __init__(self,Link):
        self.Link=Link
        self.Name=self.Link.split("downloads/")[1] # determine the target name for urlretrieve

    def Download(self,Destination): # downloads the file from object defined URL to specified path
        self.Destination=Destination
        urllib.urlretrieve(self.Link,self.Destination)
        # I gave up on handling download errors as bitbucket willingly serves a HTML file for wrong links
