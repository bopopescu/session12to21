import matplotlib.pyplot as plt
#Assuming x is the index in the list Y

# Y=[10,20,300,40,50]
# plt.plot(Y)
# plt.show()

x=list(range(1,11))
y1=[n for n in x ]
y2=[n*n for n in x]
y3=[n*n*n for n in x]
print(x)
print(y1)
print(y2)
print(y3)
"""

plt.plot(x,y1,label="y1")

plt.plot(x,y2,label="y2")

plt.plot(x,y3,label="y3")


plt.legend()

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Polinomial Graph")
plt.grid(True)

# plt.xlim(0,300)
# plt.ylim(0,3000)

plt.savefig("My graph")
plt.show()
"""