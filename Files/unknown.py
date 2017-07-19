import os

class Unknown:

    def __init__(self, path):
        self.path = path
        self.name = self.path.split('\\')[-1]
        
    def read(self):
        os.startfile(self.path)
        
    def rename(self, text):
        newPath = "\\".join(self.path.split('\\')[:-1 or None]) + "\\" + text + self.path.split('.')[-1]
        os.rename(self.path, newPath)
        self.path = newPath