import sys
from queue import PriorityQueue
import random
import math

#Creating global vars
clock = -1
serverIdle = True
readyQueueCount = -1
t = -1
eventQ = PriorityQueue()

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
    t = 0
    eventQ.queue.clear()
    sched_event(1, t)


def sched_event():
    event = Event()
