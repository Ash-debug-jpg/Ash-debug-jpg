#######################################################################ft_time
"""print("bonjour")
nombre1 = int(input("Entrer un nombre : "))
nombre2 = int(input("Entrer un deuxieme nombre : "))
result = nombre1 * nombre2
answer = f"le produit de {nombre1} et de {nombre2} est : {result}"
print(answer)
##########################################################################ftswap########################################################
A = int(2)
B = int(3)
temp = int(0)
temp = A
A = B
B = temp 
print (A , B)
########################################################################ft_pairimpair############################################################
number = int(input("Entrer un nombre : "))
if number % 2 == 0 :
	print (f"{number} est un nombre pair")
else :
	print (f"{number} est un nombre impair")
	#####################################################################ft_max#################################################################
grand = int(0)	
number1 = int(input("saisissez votre nombre : "))
number2 = int(input("saisissez votre nombre : "))
number3 = int(input("saisissez votre nombre : "))
if number1 < number2 and number3 < number1: 
	 grand = number2
if 	number2 < number1 and number3 < number2:
	 grand = number1
else :
	 grand = number3
print (f"pour {number1}, {number2} et {number3} le plus grand des trois est {grand} ")
#############################################################################################ft_grade###########################################################
grade = int (input("entrer votre note : "))	
if grade >= 10 and grade <= 20:
	print("valide")
if grade < 10 or grade == 0 :
	print("non valide")
if 	grade < 0 or grade > 20 :
	print("ressayer")
######################################################################################################ft_product################################################		
nbr1 = int(input("Saisissez votre nombre : "))
nbr2 = int(input("Saisissez votre deuxieme nombre : "))
product = nbr1 * nbr2
if product > 0 : 
	print (f"{product} est positif")
if product == 0 :
	print (f"{product} est null")	
else :
	print (f"{product} est negatif")
#################################################################################################################ft_absvalue###########################################	
number = int(input("entrer un nombre : "))
if number < 0:
	result = number * (-1)
if number > 0:
	result = number
print (f"la valeur absolue de  {number} est de {result}")"""
###################################################################################################################ft_moyenne###################################################		 	
number1 = int(input("entrer un premier nombre : ")) 
number2 = int(input("entrer un deuxieme nombre : ")) 
number3 = int(input("entrer un troisieme nombre : "))
somme = number1 + number2 + number3
moyenne = somme / 3 
print (moyenne)                           