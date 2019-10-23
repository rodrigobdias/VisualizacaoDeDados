import matplotlib.pyplot as plt

plt.scatter(2,4, s=100)

#Define o título do gráfico e nomeia os eixos

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()