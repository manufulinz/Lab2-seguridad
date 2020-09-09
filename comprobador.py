import hashlib
from tkinter import messagebox
texto= open("mensajeseguro.txt","r")
mensaje= texto.read()
texto.close()

def rot_encode(n): #Root N
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

def decryptRailFence(cipher, key): #Rail Fence
  
    rail = [['\n' for i in range(len(cipher))]  
                  for j in range(key)] 

    dir_down = None
    row, col = 0, 0
      
    for i in range(len(cipher)): 
        if row == 0: 
            dir_down = True
        if row == key - 1: 
            dir_down = False
          

        rail[row][col] = '*'
        col += 1
          
        if dir_down: 
            row += 1
        else: 
            row -= 1
               
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and
               (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
          

    result = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
          
        if row == 0: 
            dir_down = True
        if row == key-1: 
            dir_down = False
              
        if (rail[row][col] != '*'): 
            result.append(rail[row][col]) 
            col += 1
              

        if dir_down: 
            row += 1
        else: 
            row -= 1
    return("".join(result))

#Separador
tex = mensaje.split(" 7yc0")
mensaje = tex[0]
has1 = tex[1]


#Decifrador
des1= ((rot_encode(-21)(mensaje)))
des2= decryptRailFence(des1,3)
des_final =((rot_encode(-7)(des2)))

#Hash demensaje decifrado
c= des_final.encode("utf-8")
has2 = hashlib.sha256(c)
has2 = (has2.hexdigest())

x=has1.split()
y=has2.split()

print("El mensaje es:"+des_final)
#Compara el hash que recibio con el del mensaje
if (x == y):
    print("El mensaje no se a adulterado")

else:
    print("Este mensaje a sido adulterado")
    messagebox.showinfo(message="Este mensaje se a visto adulterado", title="Advertencia")


