import urllib.request

class Downloadable(object):
    
    def __init__(self, link):
        self.link = link

        # determine the target name for urlretrieve
        self.name = self.link.split("/")[-1]

    def download(self, destination):
        urllib.request.urlretrieve(self.link, destination)
        # I gave up on handling download errors
        # as bitbucket willingly serves a HTML file for wrong links
