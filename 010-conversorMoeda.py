brazilCurrency = float(input('Insira o valor em reais: '))
dollarQuote= 5.35
conversion = brazilCurrency / dollarQuote

input('{0:.2f} reais equivale a {1:.2f} dolars'.format(brazilCurrency, conversion))