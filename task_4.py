k1 = 1
k2 = 1.1
plt.plot(x, np.cos(x*k1), marker = "o")
plt.plot(x, np.cos(x*k2), marker = "x")
plt.plot(x, np.cos(x*k2), marker = "x")
plt.show()