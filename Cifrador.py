import hashlib
texto= open("mensajedeentrada.txt","r")
mensaje= texto.read()
texto.close()

c=mensaje.encode("utf-8")#Esto deja el mensaje en un formato para que la libreria pudea obtener el hash
Hash = hashlib.sha256(c)

def rot_encode(n): #Root N
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

def encryptRailFence(text, key): #Rail Fence
  
    rail = [['\n' for i in range(len(text))] 
                  for j in range(key)] 
    dir_down = False
    row, col = 0, 0
      
    for i in range(len(text)): 
          
        if (row == 0) or (row == key - 1): 
            dir_down = not dir_down 
          
        rail[row][col] = text[i] 
        col += 1
          
        if dir_down: 
            row += 1
        else: 
            row -= 1

    result = [] 
    for i in range(key): 
        for j in range(len(text)): 
            if rail[i][j] != '\n': 
                result.append(rail[i][j]) 
    return("" . join(result))

#====================Encriptador

criptado1=((rot_encode(7)(mensaje)))
criptado2= encryptRailFence(criptado1, 3)
criptado_Final= ((rot_encode(21)(criptado2)))


mensajec = open("mensajeseguro.txt", "w")
mensajec.write(criptado_Final+" 7yc0")
mensajec.write(Hash.hexdigest())
mensajec.close()
