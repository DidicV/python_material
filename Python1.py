
'''

#1111111

def mile_kilometri(mile):
	kilometri = miles * 1.60934
	return kilometri

miles=float(input("Indica mile: "))

kilometri=mile_kilometri(miles)

print("Rezultat " ,kilometri)

'''



#222222222222222

'''
def secunde_totale(hours, minutes, secunds):
 	
 	result=(3600*hours)+(60*minutes)+secunds
 	return result

hours=int(input("Ore: "))
minutes=int(input("Minute: "))
secunds=int(input("Secunde: "))
result=secunde_totale(hours, minutes, secunds)

print("Timpul total: "+str(result))
'''



#33333333333

'''
def suprafata_dreptunghi(latime, lungime):

	aria = latime * lungime
	perimetru = (latime*2) + (lungime * 2)
	return (aria, perimetru)

latime = float(input("Latimea: "))
lungime = float(input("Lungimea: "))
aria, perimetru=suprafata_dreptunghi(latime, lungime)

print("Aria dreptunghiului: ", aria)
print("Perimetrul dreptunghiului: ",perimetru)

'''


#44444444444444
'''

def circumferinta(raza):

	aria = pi * (raza * raza)
	cmf = (pi * 2) * raza
	return (aria, cmf)

raza = float(input("Raza (cm): "))
aria, cmf = circumferinta(raza)

print("Aria cercului: "+str(aria)+" cm^2")
print("Circuferinta: "+str(cmf)+ " cm")

'''



#5555555555555

'''

def depozit_valoare(valoarea_curenta, rata_anuala, ani_depozit):
	valoarea = valoarea_curenta *(1+rata_anuala/100)*ani_depozit
	return valoarea

val_curent = float(input("Valoarea curenta: "))
rat_anul = float(input("Rata anula: "))
ani_depoz = int(input("Ani depozit: "))
valoarea = depozit_valoare(val_curent, rat_anul, ani_depoz)
print("Pretul total: "+ str(valoarea))


'''


#66666666666666



def virsta_persoana(an, luna, zi):
	
	from datetime import date
	now = date.today ()
	zile = date(int(an), int(luna), int(zi))
	zile = now-zile
	return zile

an = int(input("Anul: "))
luna=int(input("Luna: "))
zi=int(input("Data: "))
zile = virsta_persoana(an, luna, zi)

print ("Varsta in zile: " + str(zile))



#   PARTEA DOUA



#1111111111111
'''


def numar_par(x):	
	if x%2==0:
		bolean = "True"
	else:
		bolean = 'False'
	return bolean		
		
x=int(input("Numar: "))
bolean = numar_par(x)

print(bolean)
'''


#2222222222222222

'''

def gaseste_nume(name):
	if name == "Ion":
		bolean = "True"
	elif name == "Elena":
		bolean = "True"
	elif name == "Maria":
		bolean = "True"
	else:
		bolean = "False"

	return bolean

name = input("Nume: ")
bolean=gaseste_nume(name)
 
print(bolean)

'''


#33333333333333333

'''

def an_bisect(an):

	if an % 4 == 0:
		bolean = "True"
	else:
		bolean = "False"	
	return bolean	

an = int(input("An: "))
bolean=an_bisect(an)

print(bolean)

'''


#4444444444444444

'''

def intersectare_interval(a, b, c, d):
	if (d>=a) and (c<=b):
		bolean = "True"
	else:
		bolean = "False"
	return bolean	

a = int(input("Primul interval A: "))
b = int(input("Primul interval B: "))
c = int(input("Al doilea interval C: "))
d = int(input("Al doilea interval D: "))
bolean=intersectare_interval(a, b, c, d)

print(bolean)

'''



#5555555555555555555

'''

def numele_si_virsta(numele, varsta):
	
	if varsta < 0:
		print("Eroare de varsta !")
		exit()
	else:	
		return (numele, varsta)

name = input("Numele: ")
age = int(input("Ani: "))
numele, varsta = numele_si_virsta(name, age)

print(str(numele)+ " este " + str(varsta) + " de ani." )


'''


#666666666666666

'''
def afiseaza_numere(number):
	if number>100 or number<0:
		print("Eroare numere 1-100")
		exit()
	x =  number % 10
	y =  round((number - x) / 10)
	print("Numarul consta din " + str(y) + " zeci si "+ str(x) +" unitati.")

number=int(input("Numar: "))
afiseaza_numere(number)
'''


#77777777777777

'''

def cauta_nume(name):
	if name == 'Vasile':
		bolean = 'Moraru'
	elif name == 'Mihail':
		bolean = 'Perebinos'
	elif name == 'Ion':
		bolean = 'Sirghit'
	elif name == 'Stefan':
		bolean = 'Buzurniuc'
	else:
		bolean = "Eroare. Nu este profesor"		
	return bolean	

name = input("Numele: ")
bolean = cauta_nume(name)
print(bolean)

'''


#888888888888


'''


def pig_latin(cuvant):
	     if (cuvant[0] == "A" or cuvant[0] == "a" or cuvant[0] == "E" or cuvant[0] == "e" or cuvant[0]                                              == "I" or cuvant[0] == "i" or cuvant[0] == "O" or cuvant[0] == "o" or cuvant[0] == "U" or cuvant[0] == "u" ):
result = cuvant + "way"
		
	else:
		temp=cuvant[0]
		result=(cuvant[1:]+temp+"ay")
	return result

cuvant = input("Introdu un cuvant: ")

result=pig_latin(cuvant)

print(str(result))


'''


































