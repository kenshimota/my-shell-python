from os import path 

class WriteOut:
    def __init__(self, filename):
        self.mode = 'w'
        self.filename = filename
        if not path.isfile(filename) and not path.isdir(filename):
            self.write('')

    def only_append(self):
        self.mode = 'a'

    def write(self, message):
        with open(self.filename, self.mode) as f:
            f.write(message)


