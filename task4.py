class Board:
    def __init__(self):
        self.board = [["*" for _ in range(8)] for _ in range(8)]

    def display(self):
        for row in self.board:
            print(" ".join(row))

class sahmatTaxtasi:
    def __init__(self, reng):
        self.reng = reng
        
class piyada(sahmatTaxtasi):
    def hərəkət(self):
        print("piyada bir irəli hərəkət edir.")

class top(sahmatTaxtasi):
    def hərəkət(self):
        print("top saquli ve ufuqi hərəkət edir.")

class at(sahmatTaxtasi):
    def hərəkət(self):
        print("At L-şəklində hərəkət edir.")

class fil(sahmatTaxtasi):
    def hərəkət(self):
        print("Fil diaqonal hərəkət edir.")

class vezir(sahmatTaxtasi):
    def hərəkət(self):
        print("Vezir diaqonal, saquli ve ufuqi hərəkət edir.")

class sah(sahmatTaxtasi):
    def hərəkət(self):
        print("Şah bir diaqonal, saquli ve ufuqi istiqamətdə hərəkət edir.")

def test_hereket(piyada):
    print("piyadanin hərəkəti:")
    piyada.hərəkət()
    
def test_hereket(top):
    print("topun hərəkəti : ")
    top.hərəkət()
    
def test_hereket(sah):
    print("sahinn hərəkəti : ")
    sah.hərəkət()

def test_hereket(at):
    print("atin hərəkəti : ")
    at.hərəkət()

taxta = Board()
taxta.display()

# test_hereket(piyada("ag"))

# test_hereket(top("qara"))

# test_hereket(sah("qara"))

test_hereket(at("ag"))
