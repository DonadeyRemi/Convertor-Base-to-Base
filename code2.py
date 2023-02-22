
class numeration():
    hexadecimal_l = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    binaire_l = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,0,1,0,0],[0,1,0,1],[0,1,1,0],[0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]]
    decimal_l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    ASCII_l = ["null","start of heading","start of text","end of text","end of transmission","enquiry","acknowledge","bell","backspace","horizontal tab","NL line feed,new line","vertical tab","NL form feed,new page","carriage return","shift out","shift in","data link escape","device control 1","device control 2","device control 3","device control 4","negative acknowledge","synchronous idle","end of trans. block","cancel","end of medium","substitute","escape","file separator","group separator","record separator","unit separator","Space","!",'"',"#","§","%","&","'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[","\'","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~","DEL"]
    
    def __init__(self,number,base):
        self.base = base
        self.number = None
        if self.base == "binaire":
            try: 
                for bit in number :
                    if int(bit) != 0 and int(bit) != 1:
                        raise ValueError
            except ValueError:
                print(ValueError,"ton nombre doit etre compose de 0 ou de 1")
            else:
                self.number = list()
                for bit in number:
                    self.number.append(int(bit))
        
        elif self.base == "decimal":
            try:
                if not isinstance(int(number),int):
                    raise ValueError
            except ValueError:
                print(ValueError,"ton nombre doit être un nombre et pas un mot")
            else:
                self.number = int(number)
        
        elif self.base == "hexadecimal":
            try :
                for lettre in number:
                    presence = lettre in numeration.hexadecimal_l
                    if presence == False:
                        raise ValueError
            except ValueError:
                print(ValueError,"tu doit rentrer un nombre correct")
            else:
                self.number = number

        elif self.base == "ASCII":
            try :
                if not isinstance(number,str):
                    raise TypeError
                
                presence = number in numeration.ASCII_l
                if presence == False:
                    raise ValueError
            except ValueError:
                print(ValueError,"tu doit rentrer un caractère type ASCII correct")
            except TypeError:
                print(TypeError,"tu dois renter un cractère ASCII en str")
            else:
                self.number = number
        

    def binaire(self):
        try : 
            if self.number == None:
                raise ValueError
        except :
            print(ValueError,"tu doit renter un nombre corect")
        else:
            if self.base == "binaire":
                resultat = ""
                for bit in self.number :
                    resultat += str(bit)
                return resultat
            
            elif self.base == "decimal":
                reste = []
                #number = float(self.number)
                number = self.number
                while number != 0 :
                    reste.append(int(number % 2))
                    number = int(number/2)
                reste.reverse()
                resultat = ""
                for bit in reste:
                    resultat += str(bit)
                return resultat

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

                resultat2 = ""
                for bit in resultat:
                    resultat2 += str(bit)
                return resultat2

            elif self.base == "ASCII":
                pos_dec = int(numeration.ASCII_l.index(self.number))
                nb_decimal = numeration(pos_dec,"decimal")
                nb_binaire = nb_decimal.binaire()
                return nb_binaire


    def decimal(self):
        try : 
            if self.number == None:
                raise ValueError
        except :
            print(ValueError,"tu doit renter un nombre corect")
        else:
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

            elif self.base == "ASCII":
                pos_dec = numeration.ASCII_l.index(self.number)
                return str(pos_dec)

    def hexadecimal(self):
        try : 
            if self.number == None:
                raise ValueError
        except :
            print(ValueError,"tu doit renter un nombre corect")
        else:
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
                    if resultat[0] == "0":
                        resultat = resultat.replace("0","")
                    return resultat

            elif self.base == "decimal":
                number = self.number
                reste = list()
                while number != 0 :
                    reste.append(int(number % 16))
                    number = int(number/16)
                
                reste.reverse()
                resultat = ""
                for r in reste:
                    pos = numeration.decimal_l.index(r)
                    res = numeration.hexadecimal_l[pos]
                    resultat += res
                return resultat

            elif self.base == "ASCII":
                pos_dec = int(numeration.ASCII_l.index(self.number))
                nb_dec = numeration(pos_dec,"decimal")
                nb_hexa = nb_dec.hexadecimal()
                return nb_hexa

    def ASCII(self):
        try : 
            if self.number == None:
                raise ValueError
        except :
            print(ValueError,"tu doit renter un nombre corect")
        else:
            if self.base == "decimal":
                try : 
                    numeration.ASCII_l[self.number]
                except IndexError:
                    print(IndexError,"il n'y a pas de caractère ASCII avec de nombre là")
                    return "pas de caractère ASCII avec ce nombre"
                else:
                    return numeration.ASCII_l[self.number]
        
            elif self.base == "binaire":
                code_dec = self.decimal()
                try : 
                    numeration.ASCII_l[code_dec]
                except IndexError:
                    print(IndexError,"il n'y a pas de caractère ASCII avec de nombre là")
                    return "pas de caractère ASCII avec ce nombre"
                else:
                    return numeration.ASCII_l[code_dec]

            elif self.base == "hexadecimal":
                code_dec = self.decimal()
                try : 
                    numeration.ASCII_l[code_dec]
                except IndexError:
                    print(IndexError,"il n'y a pas de caractère ASCII avec de nombre là")
                    return "pas de caractères ASCII avec ce nombre"
                else:
                    return numeration.ASCII_l[code_dec]
            
            elif self.base == "ASCII":
                return self.number
                

if __name__ == "__main__":
    n = numeration("j","ASCII")
    print(n.ASCII())
    print(n.decimal())
    print(n.hexadecimal())
    print(n.binaire())
    
    
    
        