class File:

    def __init__(self,file,method):
        self.file = file
        self.method = method

    def __enter__(self):
        self.r = open(self.file,self.method,encoding='utf-8')
        return self.r

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.r.close
        return True


with File('example.txt', 'a') as file:

    file.write('Всем привет!\n')
