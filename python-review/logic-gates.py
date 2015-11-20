
#general class for gates depending on number of input lines. 
class LogicGate:
		def __init__(self,n):
			self.label = n
			self.output = None

		def getLabel(self):
			return self.label

		def getOutput(self):
			self.output = self.performGateLogic()
			return self.output 

#inherits gate label from parent class LogicGate.
#adds ability to get the values from two input lines. 
#first line of the constructor calls upon the parent class. 
class BinaryGate(LogicGate): 
		def __init__(self,n):
			super().__init__(n) 

			self.pinA = None
			self.pinB = None

		def getPinA(self):
			return int(input("Enter Pin A input for gate" + self.getLabel() + "-->"))

		def getPinB(self):
			return int(input("Enter Pin B input for gate" + self.getLabel() + "-->"))

class UnaryGate(LogicGate): #subclass of LogicGate, with only one input line.
		def __init__(self,n):
			super().__init__(n)

			self.pin = None

		def getPin(self):
			return int(input("Enter Pin B input for gate" + self.getLabel() + "-->"))

class AndGate(BinaryGate):
		def __init__(self,n):
			super().__init__(n)

		def performGateLogic(self):

			a = self.getPinA()
			b = self.getPinB()
			if a == 1 and b == 1:
				return 1
			else:
				return 0 


