class Notificacion:
	def __init__(self, noti):
		self.noti = noti
		
	def Message(self):
		print(f"alberto: {self.noti}")
		
class Insta(Notificacion):
	def Message(self):
		print(f"alberto: {self.noti}")
		
class Whatsapp(Notificacion):
	def Message(self):
		print(f"alberto: {self.noti}")
		
class Gmail(Notificacion):
	def Message(self):
		print(f"alberto: {self.noti}")
		
noti = input("Ingrese el mensaje que va a mandar: ")
noti1 = Insta(noti)
noti2 = Whatsapp(noti)
noti3 = Gmail(noti)

noti1.Message()
noti2.Message()
noti3.Message()