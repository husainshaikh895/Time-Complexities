import matplotlib.pyplot as plt

power =[]
nums = []

for i in range(40):
	power.append(3**i)
	nums.append(i)

plt.bar(range(len(power)), list(power), align='center', color='g')
plt.xticks(range(len(nums)), list(nums))
plt.xlabel("3 ^ n")
plt.ylabel("Numbers")
plt.title("3 ^ n graph visualisation")
plt.show()
