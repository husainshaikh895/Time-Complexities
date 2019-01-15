import matplotlib.pyplot as plt
from math import log, ceil

power =[]
nums = []

for i in range(5, 100):
	power.append((i * (log(i))))
	nums.append(i)

plt.bar(range(len(power)), list(power), align='center', color='r')
plt.xticks(range(len(nums)), list(nums))
plt.xlabel("n * log(n)")
plt.ylabel("Numbers")
plt.title("n * log(n) graph visualisation")
plt.show()
