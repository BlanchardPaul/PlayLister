import os

class Unknown:

    def __init__(self, path):
        self.path = path
        self.name = self.path.split('\\')[-1]
        
    def read(self):
        os.startfile(self.path)
        
    def rename(self, text):
        newPath = "\\".join(self.path.split('\\')[:-1 or None]) + "\\" + ''.join(e for e in text.lower() if e.isalnum() or e.isspace()).replace(' ', '.') + self.path.split('.')[-1]
        print(newPath)
        os.rename(self.path, newPath)
        self.path = newPath