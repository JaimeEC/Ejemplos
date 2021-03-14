from time import sleep

lexemas = []
def lexico(cadena):
    state = 0
    cache = ""
    pos = 0
    str_length = len(cadena)
    idToken = ""
    while pos < str_length:
        char = cadena[pos] # char = "#"
        if state == 0:
            if char.isalpha():
                state = 1
                cache = cache + char # char="L"
                pos = pos + 1
            elif char == "#":
                state = 2
                cache = cache + char # char="#"
                pos = pos + 1
            elif char == "%" or char == "$":
                state = 4
                cache = cache + char # char="%"|"$"
                pos = pos + 1
                if char == "%":
                    idToken = "desc"
                else:
                    idToken = "precio"
            else:
                print("Error lexico con: ", char)
                pos = pos + 1
        elif state == 1:
            if char.isalpha() or char.isdigit() or char == "_":
                cache = cache + char # char="%"|"$"
                pos = pos + 1
            else:
                state = 0
                #Estamos en un estado de aceptación
                lexemas.append([cache, "id"])
                cache = ""
        elif state == 2:
            if char.isalpha():
                state = 3
                cache = cache + char
                pos = pos + 1
            else:
                print("Error lexico con: ", cache)
                state = 0
                cache = ""
        elif state == 3:
            if char.isalpha():
                cache = cache + char
                pos = pos + 1
            else:
                state = 0
                #Estamos en un estado de aceptación
                lexemas.append([cache, "codb"])
                cache = ""
        elif state == 4:
            if char.isdigit():
                state = 5
                cache = cache + char
                pos = pos + 1
            else:
                state = 0
                print("Error lexico con: ", cache)
                cache = ""
        elif state == 5:
            if char.isdigit():
                cache = cache + char
                pos = pos + 1
            elif char == ".":
                state = 6
                cache = cache + char
                pos = pos + 1
            else:
                state = 0
                lexemas.append([cache, idToken])
                cache = ""
        elif state == 6:
            if char.isdigit():
                state = 7
                cache = cache + char
                pos = pos + 1
            else:
                state = 0
                print("Error lexico con: ", cache)
                cache = ""
        elif state == 7:
            if char.isdigit():
                cache = cache + char
                pos = pos + 1
            else:
                state = 0
                lexemas.append([cache, idToken])
                cache = ""
        if pos == str_length: #n-1    n
            if len(cache) != 0:
                if state == 1:
                    lexemas.append([cache, "id"])
                elif state == 3:
                    lexemas.append([cache, "codb"])
                elif state == 5 or state == 7:
                    lexemas.append([cache, idToken])
                else:
                    print("Error lexico con: ", cache)

def muestraLexemas():
    print()
    for e in lexemas:
        print(e)


def sintaxis(lista):
    state = 0
    for e in lista:
        sleep(0.5)
        if state == 0:
            if e[1]== "id":
                print("Identificador:", e[0])
                state = 1
            else:
                print("Error sintactico")
                break
        elif state == 1:
            if e[1] == "codb":
                print("Codigo de Barras:", e[0])
                state = 2
            else:
                print("Error sintactico")
                break
        elif state == 2:
            if e[1] == "precio":
                print("Precio:", e[0])
                state = 3
            else:
                print("Error sintactico")
                break
        elif state == 3:
            if e[1] == "desc":
                print("Descuento:", e[0])
                state = 0
            else:
                print("Error sintactico")
                break
            

entrada= "+$120.00 Gas_Propano"
lexico(entrada)
entrada= "##asdf%12.00"
lexico(entrada)
sintaxis(lexemas)
muestraLexemas()
lexemas.clear()
print()
# entrada= "+(Gas_Propano##asdf$120.00+%12.00\n"
# lexico(entrada)
# sintaxis(lexemas)
# lexemas.clear()
# print()
Aentrada= [
    "PapelPaca\n",
    "#POIWER",
    "$12.5",
    "%2.0\n",
    "Cereal#ACPAE$24.99%00.0"]
    
for linea in Aentrada:
    lexico(linea)
sintaxis(lexemas)
lexemas.clear()






#Lexico
# digraph G {

#   rankdir=LR
#   S0[shape="circle"]
#   S1[shape="doublecircle"]
#   S2[shape="circle"]
#   S3[shape="doublecircle"]
#   S4[shape="circle"]
#   S5[shape="doublecircle"]
#   S6[shape="circle"]
#   S7[shape="doublecircle"]
  
#   S0 -> S1[label="L"]
#   S1 -> S1[label="L"]
#   S1 -> S1[label="D"]
#   S1 -> S1[label="_"]
  
#   S0 -> S2 [label="#"]
#   S2 -> S3 [label="L"]
#   S3 -> S3 [label="L"]
  
#   S0 -> S4 [label="%"]
#   S0 -> S4 [label="$"]
#   S4 -> S5 [label="D"]
#   S5 -> S5 [label="D"]
    
#   S5 -> S6 [label="."]
#   S6 -> S7 [label="D"]
#   S7 -> S7 [label="D"]
# }

#Sintactico
# digraph G {

#   rankdir=LR
#   S0[shape="circle"]
#   S1[shape="circle"]
#   S2[shape="circle"]
#   S3[shape="doublecircle"]
#   S4[shape="circle"]
#   S5[shape="doublecircle"]
  
#   S0 -> S1 [label="restaurante"]
#   S1 -> S2 [label="="]
#   S2 -> S3 [label="cadena"]
#   S0 -> S4 [label="cadena"]
#   S4 -> S5 [label=":"]
# }

variable = 234
if variable == True:
    print()
variable2 = True