# Kalkulator na funkcjach

def suma(a,b):
	wynik = a+b
	print("suma:",wynik)

def roznica(a,b):
	wynik = a-b
	print("roznica:",wynik)

def iloczyn(a,b):
	wynik = a*b
	print("iloczyn:",wynik)

def iloraz(a,b):
	if b!=0:
		wynik = a/b
		print("iloraz:",wynik)
	else:
		print("error")


iloraz(3,0)