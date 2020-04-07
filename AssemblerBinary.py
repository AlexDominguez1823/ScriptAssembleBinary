### Oscar Alejandro Dominguez Duran ###

def main():
    file1 = open("instrucciones.txt", mode="r")
    for linea in file1:    
        instruccion = []
        print(linea)
        input()
        input()
        #se identifica de qué instruccion se trata
        if("add" in linea):
            #se añade el OP
            instruccion.append("000000")
            #se obtiene la representación en binario del RS, RD, RT
            numero_b = replaceSymbols(linea)
            #se añade la representación a la lista
            for j in numero_b:
                instruccion.append(j)
            instruccion.append("00000100000")
            
        elif("sub" in linea):
            #se añade el OP
            instruccion.append("000000")
            #se obtiene la representación en binario del RS, RD, RT, Inmediato
            numero_b = replaceSymbols(linea)
            #se añade la representación a la lista
            for j in numero_b:
                instruccion.append(j)
            instruccion.append("00000100010")
        
        elif("and" in linea):
            #se añade el OP
            instruccion.append("000000")
            #se obtiene la representación en binario del RS, RD, RT, Inmediato
            numero_b = replaceSymbols(linea)
            #se añade la representación a la lista
            for j in numero_b:
                instruccion.append(j)
            instruccion.append("00000100100")

        elif("or" in linea and "x"):
            #se añade el OP
            instruccion.append("000000")
            #se obtiene la representación en binario del RS, RD, RT, Inmediato
            numero_b = replaceSymbols(linea)
            #se añade la representación a la lista
            for j in numero_b:
                instruccion.append(j)
            instruccion.append("00000100101")

        elif("mult" in linea):
            #se añade el OP
            instruccion.append("000000")
            #se obtiene la representacion en binario de RS, RD, RT, Inmediato
            numero_b = replaceSymbols(linea)
            #se añade la representacion a la lista
            for j in numero_b:
                instruccion.append(j)
            instruccion.append("00000011001")

        elif("div" in linea):
            #se añade el OP
            instruccion.append("000000")
            #se obtiene la representacion en binario de RS, RD, RT, Inmediato
            numero_b = replaceSymbols(linea)
            #se añade la representacion a la lista
            for j in numero_b:
                instruccion.append(j)
            instruccion.append("00000011010")

        elif("xor" in linea):
            #se añade el OP
            instruccion.append("000000")
            #se obtiene la representacion en binario de RS, RD, RT, Inmediato
            numero_b = replaceSymbols(linea)
            #se añade la representacion a la lista
            for j in numero_b:
                instruccion.append(j)
            instruccion.append("00000100110")

        else:
            pass

        x = ""
        for j in instruccion:
            x = (x + j)
        
        y=[]
        while x:
            y.append(x[:8])
            x = x[8:]
        
        for j in y:
            with open("binario.txt", mode="a") as text_file:
                text_file.write(j + "\n")
    
def replaceSymbols(linea):
    linea_codigo = linea.split(",")
    i=0
    array = []
    for j in linea_codigo:
        linea_num = j.replace("$", "")
        if("#" in j):
            linea_num = linea_num.replace("#", "")

        if("add" in linea_num):
            linea_num = linea_num.replace("add", "")
            tipo = "R"
        
        elif("sub" in linea_num):
            linea_num = linea_num.replace("sub", "")
            tipo = "R"
        
        elif("and" in linea_num):
            linea_num = linea_num.replace("and", "")
            tipo = "R"

        elif("or" in linea_num and "x" not in linea_num):
            linea_num = linea_num.replace("or", "")
            tipo = "R"
        
        elif("mult" in linea_num):
            linea_num = linea_num.replace("mult", "")
            tipo = "R"

        elif("div" in linea_num):
            linea_num = linea_num.replace("div", "")
            tipo = "R"

        elif("xor" in linea_num):
            linea_num = linea_num.replace("xor", "")
            tipo = "R"

        else:
            pass

        numero_b = binario(linea_num, i, tipo)
        array.append(numero_b)
        i+=1

    return array

def binario(linea_num, i, tipo):
    if(int(linea_num) >= 0):
        numero = int(linea_num)
        numero2 = bin(numero)
        numero_b = numero2[2:]
        if(tipo == "R"):
            if(i < 3):
                while(len(numero_b) < 5):
                    numero_b = ("0" + numero_b)
            else:
                pass
        return numero_b
    
    elif(int(linea_num) < 0):
        numero = abs(int(linea_num))
        numero_b = (numero ^ 65535) + 1
        numero_b = bin(numero_b)
        numero_b = numero_b[2:]
        return numero_b      

    else:
        if(i<2):
            numero = int(linea_num)
            numero2 = bin(numero)
            numero_b = numero[2:]
            while(len(numero_b) < 5):
                    numero_b = ("0" + numero_b)
        
        else:
            numero_b = str(linea_num)
        
        return numero_b

main()
