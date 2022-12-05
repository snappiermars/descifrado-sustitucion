arch = open("textoCifrado.txt", "r")
texto = arch.read()
texto2=""
texto = texto.lower()
alfabeto="abcdefghijklmnopqrstuvwxyz"

for c in texto:
    if c == "á":
        c="a"

datos = texto.split()
dic=[]
for p in datos:
    if not(p in dic):
        dic.append(p)
dic.sort()

diccio = open("diccita.txt", "w")
cad = ""
for p in dic:
    cad+=p+" "
diccio.write(c)
diccio.close()

##Creacion histograma
histo = {}
for c in alfabeto:
    histo[c]=0
print (histo)
for c in texto:
    if c in alfabeto:
        histo[c]+=1
print(histo)

arch2 = open ("histo.csv", "w")

for e in histo.keys():
    arch2.write(e+","+ str(histo[e])+"\n")
arch2.close()
