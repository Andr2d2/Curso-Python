something = input('Digite algo:')
somethingIsnumeric = something.isnumeric
somethingIsalnum = something.isalnum
somethingIsspace = something.isspace
somethingIsalpha = something.isalpha

print('{0} é um número? {1}'.format(something, somethingIsnumeric()))
print('{0} é alfanumérico? {1}'.format(something, somethingIsalnum()))
print('{0} é um espaço vazio? {1}'.format(something, somethingIsspace()))
print('{0} é um texto? {1}'.format(something, somethingIsalpha()))
