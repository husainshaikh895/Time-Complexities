import matplotlib.pyplot as plt

squares =[]
nums = []

for i in range(100):
	squares.append(i**2)
	nums.append(i)

plt.bar(range(len(squares)), list(squares), align='center', color='b')
plt.xticks(range(len(nums)), list(nums))
plt.xlabel("Squares")
plt.ylabel("Numbers")
plt.title("Square graph visualisation")
plt.show()
