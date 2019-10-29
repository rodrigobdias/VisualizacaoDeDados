from die import Die
import pygal

# Cria dois dados D6
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []

for _ in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analisa os resultados
frequencies = []

max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [x_labels for x_labels in range(2, die_1.num_sides + die_2.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')