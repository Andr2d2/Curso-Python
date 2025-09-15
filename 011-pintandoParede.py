wallHeight = float(input('Altura da parede: '))
wallWidth = float(input('Largura da parede: '))

wallArea = wallHeight * wallWidth
paintGallonVolume = 2
paintNeeded = wallArea / paintGallonVolume

print('Dimensões da parede: {0:.2f} x {1:.2f}'.format(wallHeight, wallWidth))
print('Área da parede: {0:.2f}m²'.format(wallArea))
print('É necessário {0:.2f} L de tinta para pintar toda a parede'.format(paintNeeded))