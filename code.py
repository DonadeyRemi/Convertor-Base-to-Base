
class numeration():
    hexadecimal_l = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    binaire_l = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
    decimal_l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    
    def __init__(self,number,base):
        self.number = number 
        self.base = base

    def binaire(self):
        if self.base == "binaire":
            return self.number
        
        elif self.base == "decimal":
            reste = []
            number = float(self.number)
            while number != 0 :
                reste.append(int(number % 2))
                number = int(number/2)
            reste.reverse()
            return reste

        elif self.base == "hexadecimal":
            number = list(self.number)
            resul = []
            for i in range(len(number)):
                try :
                    numeration.hexadecimal_l.index(number[i])
                    print()
                except ValueError:
                    print(ValueError,"hexadecimal number it is not good writed {}".format(number[i]))
                else:
                    pos = numeration.hexadecimal_l.index(number[i])
                    bit4 = numeration.binaire_l[pos]
                    resul.append(bit4)
            resultat = list()
            for res in resul:
                resultat += res
            return resultat

    def decimal(self):
        if self.base == "decimal":
            return self.number
        elif self.base == "binaire":
            number = self.number
            try:
                if not isinstance(number,list):
                    raise TypeError
            except TypeError:
                print(TypeError,"number must be a list if is a binaire base if not change fonction")
            else:
                result = 0
                number.reverse()
                for i in range(len(number)):
                    a = number[i]*2**i
                    result += a
                return result
        
        elif self.base == "hexadecimal":
            number = list(self.number)
            number.reverse()
            resultat = 0
            for i in range(len(number)):
                pos = numeration.hexadecimal_l.index(number[i])
                res = numeration.decimal_l[pos]
                resu = res*16**i
                resultat += resu
            return resultat

    def hexadecimal(self):
        if self.base == "hexadecimal":
            return self.number
        elif self.base == "binaire":
            number = self.number
            if len(number) < 4 :
                number.reverse()
                while len(number) != 4:
                    number.append(0)
                number.reverse()
                pos = numeration.binaire_l.index(number)
                resultat = numeration.hexadecimal_l[pos]
                return resultat
            elif len(number) == 4:
                pos = numeration.binaire_l.index(number)
                resultat = numeration.hexadecimal_l[pos]
                return resultat
            elif len(number) > 4 :
                number.reverse()
                l = len(number)
                c = int(l/4)
                nu = list()
                for i in range(c):
                    u = 4
                    u *= i 
                    n = number[u:u+4]
                    nu.append(n)
                n_f = number[c*4:len(number)]
                if n_f != []:
                    while len(n_f) != 4:
                        n_f.append(0)
                    nu.append(n_f)
                resultat = ""
                for n in nu :
                    n.reverse()
                    pos = numeration.binaire_l.index(n)
                    res = numeration.hexadecimal_l[pos]
                    resultat += res
                resultat = resultat[::-1]
                return resultat

        elif self.base == "decimal":
            number = self.number
            reste = list()
            while number != 0 :
                reste.append(int(number % 16))
                number = int(number/16)
            
            reste.reverse()
            print(reste)
            resultat = ""
            for r in reste:
                pos = numeration.decimal_l.index(r)
                res = numeration.hexadecimal_l[pos]
                resultat += res
            return resultat
                
        
        
        


if __name__ == "__main__":
    n = numeration(29,"decimal")
    print(n.hexadecimal())
        