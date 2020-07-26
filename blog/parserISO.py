class ParserIso:

        
    def __init__(self):
        self.iso = ""
        self.camposIso = []
        self.dicCamposFijos = {3: 6,4: 12,5: 12,6: 12,7: 10,8: 8,9: 8,
        10: 8,11: 6,12: 6,13: 4,14: 4,15: 4,16: 4,17: 4,18: 4,19: 3,20: 3,21: 3,22: 3,23: 3,
        24: 3,25: 2,26: 2,27: 1,28: 9,29: 9,30: 9,31: 9,37: 12,38: 6,39: 2,40: 3,41: 16,
        42: 15,43: 40,49: 3,50: 3,51: 3,52: 16,53: 16,64: 16,65: 8,66: 1,67: 2,68: 3,
        69: 3,70: 3,71: 4,72: 4,73: 6,74: 10,75: 10,76: 10,77: 10,78: 10,79: 10,80: 10,
        81: 10,82: 12,83: 12,84: 12,85: 12,86: 16,87: 16,88: 16,89: 16,90: 42,91: 1,92: 2,
        93: 5,94: 7,95: 42,96: 16,97: 17,98: 25}

        self.dicCamposVar = {2: 2,32: 2,33: 2,34: 2,35: 2,36: 3,44: 2,45: 2,46: 3,47: 3,48: 3,54: 3,
        55: 3,56: 3,57: 3,58: 3,59: 3,60: 3,61: 3,62: 3,63: 3,99: 2,100: 2,101: 2,102: 2,103: 2,
        104: 3,105: 3,106: 3,107: 3,108: 3,109: 3,110: 3,111: 3,112: 3,113: 3,114: 3,115: 3,
        116: 3,117: 3,118: 3,119: 3,120: 3,121: 3,122: 3,123: 3,124: 3,125: 3,126: 3,127: 3}
    
    def darIso(self,tira):
        n = tira.find("ISO")
        if n < 0:	
            return ""
        else:
            return tira[n:]	

    def desplegarHexa(self,caract):
        if (caract == '0' ): return "0000" 
        if (caract == '1' ): return "0001"
        if (caract == '2' ): return "0010"
        if (caract == '3' ): return "0011"
        if (caract == '4' ): return "0100"
        if (caract == '5' ): return "0101"
        if (caract == '6' ): return "0110"
        if (caract == '7' ): return "0111"
        if (caract == '8' ): return "1000"
        if (caract == '9' ): return "1001"
        if (caract == 'A' ): return "1010"
        if (caract == 'B' ): return "1011"
        if (caract == 'C' ): return "1100"
        if (caract == 'D' ): return "1101"
        if (caract == 'E' ): return "1110"
        if (caract == 'F' ): return "1111"
        return False

    def parsearIso(self,aiso):
        iso = self.darIso(aiso) 
        if iso == "":
            return []
        
        res = []
        camposFijos = self.dicCamposFijos.keys()
        camposVar = self.dicCamposVar.keys()
        bitmap = iso[16:48]
        posAct = 48
        campo = 1
        for i in range (32):
            hex = self.desplegarHexa(bitmap[i])
            for j in range(4):
                if hex[j] == "1":
                    varDesc = "Campo " + str(campo) + ": "
                    varCamp = ""
                    if campo in camposFijos:
                        long = self.dicCamposFijos[campo]
                        #print("campo " + str(campo) + ":[" + iso[posAct:posAct+long] + "]")
                        varCamp = varCamp + iso[posAct:posAct+long]
                        posAct = posAct + long
                    if campo in camposVar:
                        longLong = self.dicCamposVar[campo]
                        longLong = int (longLong)
                        long = int(iso[posAct:posAct+longLong])
                        posAct = posAct + longLong
                        varCamp = varCamp + iso[posAct:posAct+long]
                        #print("campo " + str(campo) + ":[" + iso[posAct:posAct+long] + "]")
                        posAct = posAct + long
                  
                    aConcat = [varDesc,varCamp]
                    res.append(aConcat)
                campo = campo + 1 
        return res
        

