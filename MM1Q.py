import matplotlib.pyplot as plt

import random
import csv
# importing the required module


# define a class called 'Customer'

x = []
y = []
z = []
k = []
l = []

class Customer:
    def __init__(self,arrival_date,service_start_date,service_time):
        self.arrival_date = arrival_date
        self.service_start_date = service_start_date
        self.service_time = service_time
        self.service_end_date = self.service_start_date + self.service_time
        self.wait = self.service_start_date - self.arrival_date

# a simple function to sample from negative exponential


def neg_exp(lambd):
    return random.expovariate(lambd)

def QSim(lambd=False,mu=False,simulation_time=False):

    print("Simulation start")
    if not lambd:
        lambd= int(input("Enter arrival rate"))

    if not mu:
        mu = int(input("Enter arrival rate"))

    if not simulation_time:
        simulation_time = input("Enter arrival rate")
    # print(lambd)
    # print(simulation_time)
    # print("Simulation start4")
    t = 0
    customers= []
    sim= int(simulation_time)
    # while(t < simulation_time):
    while t < sim:
        # print("Simulation start5")
        if len(customers) == 0:
            arrival_date = neg_exp(lambd)
            service_start_date = arrival_date

        else:
            arrival_date+= neg_exp(lambd)
            service_start_date = max(arrival_date, customers[-1].service_end_date)
        service_time = neg_exp(mu)

        # create new customer
        customers.append(Customer(arrival_date, service_start_date, service_time))
        print(customers)
        # increment clock till next end of service
        t = arrival_date

        # calculate summary statistics
    Waits = [a.wait for a in customers]
    print(Waits)
    Mean_Wait = sum(Waits) / len(Waits)

    Total_Times = [a.wait + a.service_time for a in customers]
    Mean_Time = sum(Total_Times) / len(Total_Times)

    Service_Times = [a.service_time for a in customers]
    Mean_Service_Time = sum(Service_Times) / len(Service_Times)

    Utilisation = sum(Service_Times) / t

    # output summary statistics to screen
    # print("Simulation start3")
    print("")
    print("Summary results")
    print("")
    print("No of customer",len(customers))
    print("Mean Services",Mean_Service_Time)
    print("Mean Wait: ", Mean_Wait)
    print("Mean Time in System: ",Mean_Time)
    print("Utilisation: ",Utilisation)
    print("")

    # prompt user to output full data set to csv
    if input("Output data to csv (True/False)? "):
        outfile = open('MM1Q-output-(%s,%s,%s).csv' % (lambd, mu, simulation_time), 'w')
        output = csv.writer(outfile)
        output.writerow(
            ['Customer', 'Arrival_Date', 'Wait', 'Service_Start_Date', 'Service_Time', 'Service_End_Date'])
        i = 0

        for customer in customers:
            i = i + 1
            outrow = []
            y.append(customer.wait)
            x.append(i)
            z.append(customer.service_time)
            k.append(customer.service_end_date)


            outrow.append(i)
            outrow.append(customer.arrival_date)
            outrow.append(customer.wait)
            outrow.append(customer.service_start_date)
            outrow.append(customer.service_time)
            outrow.append(customer.service_end_date)
            output.writerow(outrow)
        outfile.close()

        # Function to plot
        plt.plot(x, y)
        # naming the x axis
        plt.xlabel('No of customer')
        # naming the y axis
        plt.ylabel('Customer Wait Time')
        # giving a title to my graph
        plt.title('Waiting time Per customer')
        # function to show the plot
        plt.show()

        # Function to plot
        plt.plot(x, z)
        # naming the x axis
        plt.xlabel('No of customer')
        # naming the y axis
        plt.ylabel('Customer Service Time')

        # giving a title to my graph
        plt.title('Service time Per customer')

        # function to show the plot
        plt.show()

        # Function to plot
        plt.plot(x, y)
        # naming the x axis
        plt.xlabel('No of customer')
        # naming the y axis
        plt.ylabel('Customer Service end-date')

        # giving a title to my graph
        plt.title('Service end-date Per customer')

        # function to show the plot
        plt.show()

    print("")

    return

QSim()






