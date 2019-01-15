import matplotlib.pyplot as plt

single_value =[]
nums = []

for i in range(100):
	single_value.append(i)
	nums.append(i)

plt.bar(range(len(single_value)), list(single_value), align='center', color='b')
plt.xticks(range(len(nums)), list(nums))
plt.xlabel("N_Value")
plt.ylabel("Numbers")
plt.title("N_value Graph Visualisation")
plt.show()