import matplotlib.pyplot as plt

power =[]
nums = []

for i in range(40):
	power.append(2**i)
	nums.append(i)

plt.bar(range(len(power)), list(power), align='center', color='b')
plt.xticks(range(len(nums)), list(nums))
plt.xlabel("2 ^ n")
plt.ylabel("Numbers")
plt.title("2 ^ n graph visualisation")
plt.show()
