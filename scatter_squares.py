import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5, 6, 7]
y_values = [1, 4, 9, 16, 25, 36, 49]

plt.scatter(x_values, y_values, s=20)

#Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()