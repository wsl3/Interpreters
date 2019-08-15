class Iterpreter(object):
	def __init__(self):
		self.localEnv = {}
	def run(self):
		print("{:*^60}\n".format("Small Python"))
		command = input(">>>")
		while True:
			if command == "":
				print(promtp)
				continue
			elif "exit" in command:
				return
			else:
				self.ExcutedCommand(command)
			command = input(">>>")
	def ExcutedCommand(self, command):
		if "print " in command:
			if self.localEnv.get(command[6:]):
				print(self.localEnv[command[6:]])
			else:
				print("Error:localEnv have not {}".format(command[6:]))			
		elif " = " in command:
						
			key = command[0: command.index("=")-1]
			source = command[command.index("=")+2:]
			if " + " in source:
				left = source[0]
				right = source[4]
						
				self.localEnv[key] = self.localEnv[left] + self.localEnv[right]
			else:
				if source.isdigit():
					self.localEnv[key] = int(source)
				else:
					self.localEnv[key] = source[1: len(source)-1]


if __name__ == "__main__":
	virtualBox = Iterpreter()
	virtualBox.run()
