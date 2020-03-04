
# bt,wt,tat stands for burst time, waiting time, turn around time  respectively
import matplotlib.pyplot as plt

import random
import matplotlib.pyplot as plt

# x axis values
x = [0.1, 0.22, 0.3,0.4,0.5,0.6,0.7,0.8,0.9]
# corresponding y axis values
y = [50,250 ,300,1000,2000,3000,4300,6400,11200]
z = [40,200 ,200,570,700,1100,1700,2700,4800]
k = [40,100 ,130,400,500,800,1200,1600,2700]
def neg_exp(lambd):
    return random.expovariate(lambd)


class Customer:
    def __init__(self,arrival_date,service_start_date,service_time):
        self.arrival_date = arrival_date
        self.service_start_date = service_start_date
        self.service_time = service_time
        self.service_end_date = self.service_start_date + self.service_time
        self.wait = self.service_start_date - self.arrival_date
x

print("Enter the number of processess: ")
n = int(input())
processes = []
for i in range(0, n):
    processes.insert(i, i + 1)

# Input Burst time of every process
print("\nEnter the burst time of the processes: \n")
bt = list(map(int, input().split()))

# Input Priority of every process
print("\nEnter the priority of the processes: \n")
priority = list(map(int, input().split()))
tat = []
wt = []

print("Enter arrival rate")
lambd = list(map(int, input().split()))

print("Enter service rate")

mu = list(map(int, input().split()))

simulation_time = input("Enter Simulation time")


# Sorting processes burst time, on the basis of their priority
for i in range(0, len(priority) - 1):
    for j in range(0, len(priority) - i - 1):
        if (priority[j] > priority[j + 1]):
            swap = priority[j]
            priority[j] = priority[j + 1]
            priority[j + 1] = swap

            swap = bt[j]
            bt[j] = bt[j + 1]
            bt[j + 1] = swap

            swap = processes[j]
            processes[j] = processes[j + 1]
            processes[j + 1] = swap

wt.insert(0, 0)
tat.insert(0, bt[0])

# Calculating of waiting time and Turn Around Time of each process
for i in range(1, len(processes)):
    wt.insert(i, wt[i - 1] + bt[i - 1])
    tat.insert(i, wt[i] + bt[i])

# calculating average waiting time and average turn around time
avgtat = 0
avgwt = 0
for i in range(0, len(processes)):
    avgwt = avgwt + wt[i]
    avgtat = avgtat + tat[i]
avgwt = float(avgwt) / n
avgwt = float(avgtat) / n
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0, n):
    print(str(processes[i]) + "\t\t" + str(bt[i]) + "\t\t" + str(wt[i]) + "\t\t" + str(tat[i]))
    print("\n")
print("Average Waiting time is: " + str(avgwt))
print("Average Turn Around Time is: " + str(avgtat))

#
# t = 0
# customers= []
# sim= int(simulation_time)
# rho = []
# while t < sim:
#     # print("Simulation start5")
#     for i in range(0, n):
#         if len(customers) == 0:
#             arrival_date = neg_exp(lambd)
#             service_start_date = arrival_date
#
#         else:
#             arrival_date += neg_exp(lambd)
#             # print(arrival_date)
#             service_start_date = max(arrival_date, customers[-1].service_end_date)
#         service_time = (mu*2)
#
#         # create new customer
#         customers.append(Customer(arrival_date, service_start_date, service_time))
#
#         # increment clock till next end of service
#         t = arrival_date
#
#         # calculation of rho
#         rho[i] =  lambd[i]/mu[i]

    # plotting the points
plt.plot(x, y, 'r') # plotting t, a separately
plt.plot(x, z, 'b') # plotting t, b separately
plt.plot(x, k, 'g') # plotting t, c separately

    # naming the x axis
plt.ylabel('Waiting time in ms')

    # naming the y axis
plt.xlabel('Overall-Load')

    # giving a title to my graph
plt.title('Comparision of waiting times of two priority')

    # function to show the plot
plt.show()



# < b > < / b >
