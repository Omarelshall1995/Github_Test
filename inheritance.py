class Person:
	hackme = True

	def __init__(self, name, age):
		
		self.name = name
		self.age = age
	def print_name(self):
			print("My name is {}".format(self.name))
	def print_age(self):
			print("My age is {}".format(self.age))
	def birthday(self):
	
		self.age += 1
		print("My Birthday is {}".format(self.age))


class Hacker(Person):
	def __init__(self,name,age,cves):
		super().__init__(name,age)
		self.cves = cves

	def print_name(self):
		print("My name is {} and i have {} CVEs".format(self.name, self.cves))
	def total_cves(self):
		return self.cves

bob = Person("Bob", 30)
alice = Hacker("Alice", 20, 5)

bob.print_name()
alice.print_name()
print(bob.age)
alice.birthday()
print(alice.total_cves())
print(issubclass(Person, Hacker))
print(issubclass(Hacker, Person))

print(isinstance(bob, Person))
print(isinstance(alice, Hacker))
print(isinstance(alice, Hacker))