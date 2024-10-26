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
arrivalRate = int(sys.argv[1])
serviceTime = float(sys.argv[2])
totalTurnaround = -1 #Tracks total turnaround time, for averaging later.
completedProcesses = -1
busyTime = -1 #Time the CPU is busy

#weightedProcsInQueue stores number of procsInQueue weighted by their time in queue
#needs to be updated on each departure and arrival.
weightedProcsInQueue = -1

#Essentially equivalent to the struct, but in python.
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
    t = clock + exponential_dist(1/arrivalRate) #Generating first event time t
    eventQ.queue.clear()
    totalTurnaround = 0
    completedProcesses = 0
    weightedProcsInQueue = 0
    sched_event(1, t)

#Adds single event to priority queue, based on time and time
#time dictates priority in queue.
def sched_event(type: int, time: float):
    event = Event(type, time)
    eventQ.put((time, event))

def arr_handler(e: Event, beginClock: float, endClock: float):
    sched_event(1, clock + exponential_dist(1/arrivalRate))
    weightedProcsInQueue += readyQueueCount * (endClock - beginClock)
    if serverIdle:
        serverIdle = False
        sched_event(-1, clock + exponential_dist(serviceTime))
    else: 
        readyQueueCount += 1

def dep_handler(e: Event, beginClock: float, endClock: float):
    weightedProcsInQueue += readyQueueCount * (endClock - beginClock)
    if readyQueueCount == 0:
        serverIdle == True
    else:
        readyQueueCount -= 1
        sched_event(-1, clock + exponential_dist(serviceTime))


#run() handles the loops and logic of the simulation
def run():
    init()
    while (completedProcesses != 10000):
        e = eventQ.get()[1]
        old_clock = clock
        clock = e.time #update clock to time event begins
        match e.type:
            case 1:
                arr_handler(e, old_clock, clock)
            case -1:
                dep_handler(e, old_clock, clock)

while eventQ.qsize() != 0:
    print (eventQ.get()[1].time) #FIXME testing
