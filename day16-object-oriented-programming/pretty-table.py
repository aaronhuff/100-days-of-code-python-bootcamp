from prettytable import PrettyTable

"""
Classes create objects
You create them with a constructor
Objects functions are called methods
You pass parameters to a method
Objects variables are called properties
"""

my_table = PrettyTable()
my_table.add_column('Pokemon Name', ['Charmander', 'Squirtle', 'Bulbasaur'])
my_table.add_column('Type', ['Fire', 'Water', 'Earth'])
my_table.align = 'l'

print(my_table)
