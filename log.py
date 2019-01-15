import matplotlib.pyplot as plt
from math import log

power =[]
nums = []

for i in range(5, 100):
	power.append(((log(i))))
	nums.append(i)

plt.bar(range(len(power)), list(power), align='center', color='b')
plt.xticks(range(len(nums)), list(nums))
plt.xlabel("log(n)")
plt.ylabel("Numbers")
plt.title("log(n) graph visualisation")
plt.show()
