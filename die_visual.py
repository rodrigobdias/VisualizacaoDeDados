from die import Die

# Cria um D6
die = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []

for _ in range(100):
    result = die.roll()
    results.append(result)

print(results)