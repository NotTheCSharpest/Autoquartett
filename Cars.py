class Car: 

	def __init__(self, name, geschwindigkeit, leistung, verbrauch, 

                     zylinder, hubraum, beschleunigung, zuladung, ladevolumen): 

		self.name = name 
		#angefordert geschwindigkeitsgrenze
		if geschwindigkeit <= 250:
			self.geschwindigkeit = int(geschwindigkeit)
		else:
			self.geschwindigkeit = 250

		self.leistung = int(leistung) 

		self.verbrauch = float(verbrauch) 

		self.zylinder = int(zylinder) 

		self.hubraum = float(hubraum) 

		self.beschleunigung = float(beschleunigung) 

		self.zuladung = int(zuladung) 

		self.ladevolumen = int(ladevolumen) 

  

		 
#Declare our Cars
phae = Car('VW_Phaeton', 250, 309, 15.7, 12, 6.0, 6.7, 600, 500) 
beet = Car('VW_New_Beetle', 185, 85, 8.7, 4, 2.0, 10.9, 419,527) 
toua = Car('VW_Touareg', 225, 230, 12.2, 10, 4.9, 7.8, 500, 555)
jetta = Car('VW_Jetta', 900, 175, 6.5, 8, 4.0, 6.0, 400, 450)            

  
#Make a list of cars
Autos = []
Autos.append(phae)
Autos.append(beet)
Autos.append(toua)
Autos.append(jetta)

#test-car list functionality
#for obj in Autos:
#    print(obj.geschwindigkeit)

def Spielen(car1, car2, sparkles): 

		 

	if getattr(car1, sparkles) > getattr(car2, sparkles): 

		print('{} wins'.format(car1.name)) 

	else: 

			print('{} wins'.format(car2.name)) 

print('Mit welcher Attribute sollen wir spielen? \n Wählen Sie von: \n geschwindigkeit \n \
leistung \n verbrauch \n zylinder \n hubraum \n \
beschleunigung \n zuladung  \n ladevolumen. \n\n\n') 

#Spielen(phae, beet, 'geschwindigkeit') 

  
# max speed of 250 
#mit Spielen() attrib. 2obj vergl. & winnerausgeben 
