class Pokemon: 
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print('This Pokemon says ' + self.name + ' ' + self.name + '!')

  def display_details(self):
    print('Entry Number: ' + str(self.entry))
    print('Name: ' + str(self.name))
    print('Type(s): ' + str(self.types))
    print('Description: ' + str(self.description))
    print(self.name + ' has ' + str(self.is_caught) + ' been caught!')

charizard = Pokemon(6, 'Charizard', 'Fire/Flying', 'Charizard breathes fire of such great heat that it melts anything.', False)
charizard.display_details()
print()
sprigatito = Pokemon(906, 'Sprigatito', 'Grass', 'Sprigatito is a grass cat Pokémon. It is very curious and loves to play.', True)
sprigatito.display_details()
print()
eevee = Pokemon(133, 'Eevee', 'Normal', 'Eevee has an unstable genetic makeup that suddenly mutates due to the environment in which it lives.', True)
eevee.display_details()
eevee.speak()