class LogicGate:
		def __init__(self,n):
			self.label = n
			self.output = None

		def getLabel(self):
			return self.label

		def getOutput(self):
			self.outpout = self.performGateLogic()
			return self.output 