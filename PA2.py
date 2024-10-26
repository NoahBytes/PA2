import sys
from queue import PriorityQueue
import random
import math

#Creating/initializing global vars
clock = -1
serverIdle = True
readyQueueCount = -1
t = -1
eventQ = PriorityQueue()
arrival_rate = int(sys.argv[1])
service_time = float(sys.argv[2])
totalTurnaround = -1 #Tracks total turnaround time, for averaging later.
completedProcesses = -1
busyTime = -1 #Time the CPU is busy

#procsInQueue will track the number of processes in the queue.
#Will need to be updated for each departure or arrival
#Will hold tuples of type (# of processes in queue, time in queue)
procsInQueue = []

#Rough equivalent for the struct.
#Type = 1 if arrival
#Type = -1 if departure
class Event():
    def __init__(self, type: int, time: float):
        self.type = type
        self.time = time

#uniform_dist and exponential_dist to generate exponential and poisson variables
def uniform_dist(max_value):
    rand_int = random.randint(0,max_value)
    return (rand_int / max_value)    

def exponential_dist(t):
    uni_float = uniform_dist(10000000)
    return -t*math.log(uni_float)

#init to initialize the beginning state of the system
def init():
    clock = 0
    serverIdle = True
    readyQueueCount = 0
    t = clock + exponential_dist(1/arrival_rate) #Generating first event time t
    eventQ.queue.clear()
    totalTurnaround = 0
    completedProcesses = 0
    sched_event(1, t)

#Adds single event to priority queue, based on time and time
#time dictates priority in queue.
def sched_event(type: int, time: float):
    event = Event(type, time)
    eventQ.put((time, event))

def run():
    while (completedProcesses != 10000):
        e = eventQ.get()
        old_clock = clock
        match e[1].type:
            case 1:
                arr_handler(e)
            case -1:
                dep_handler(e)

init()
while eventQ.qsize() != 0:
    print (eventQ.get()[1].time) #FIXME testing
