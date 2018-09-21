import configparser
import os

configDir = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
config = configparser.ConfigParser()
config.read(configDir + '/config.ini')


class Rule:
	pass
	
class Condition(Rule):
	pass

class MainRule(Rule):
	pass


'''
FIRST IDEA FOR RULE OBJECT
-	This class simply gets all of the conditions as
	specified in the config file. It doesn't account 
	for AND/OR/NOT conditions though.
	
class Rule:
	def __init__(self,ruleName):
		self.name = ruleName
		conditions = config.options(ruleName)
		for condition in conditions:
			self.setFromConfig(condition)
	
	def setFromConfig(self,attr_name):
		attr_value = config.get(self.name,attr_name).split(', ')
		self.__dict__[attr_name] = attr_value
		
rule1 = Rule("RULE 1")
print(rule1.__dict__)
'''
