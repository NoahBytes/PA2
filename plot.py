import matplotlib.pyplot as plt

data = {
    "arrival_rate": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    "turnaround_time": [0.111, 0.134, 0.156, 0.170, 0.208, 0.284, 0.271, 0.351, 0.608, 0.823, 0.692, 1.717, 7.224, 8.919, 14.861, 52.413, 184.910, 190.303, 201.048, 200.563, 196.659],
    "throughput": [10.008, 10.988, 12.000, 13.04, 14.05, 15.229, 15.894, 17.133, 18.086, 19.122, 20.048, 20.835, 22.225, 23.129, 23.972, 24.580, 24.874, 24.728, 24.952, 25.117, 25.447],
    "cpu_utilization": [0.402, 0.438, 0.479, 0.517, 0.561, 0.618, 0.629, 0.682, 0.725, 0.767, 0.789, 0.839, 0.889, 0.916, 0.952, 0.988, 0.996, 0.998, 0.9997, 0.9996, 0.9998],
    "ready_queue_processes": [0.267, 0.371, 0.460, 0.564, 0.748, 0.970, 0.974, 1.345, 2.124, 2.514, 2.741, 4.686, 9.399, 13.078, 15.949, 77.840, 240.308, 459.562, 658.500, 972.900, 916.411]
}


# Set up figure and axes for the four subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Performance Metrics vs. Arrival Rate (lambda)", fontsize=16)

# Plot for average turnaround time
axes[0, 0].plot(data["arrival_rate"], data["turnaround_time"], marker='o', color='b')
axes[0, 0].set_title("Average Turnaround Time")
axes[0, 0].set_xlabel("Arrival Rate (lambda)")
axes[0, 0].set_ylabel("Turnaround Time")

# Plot for total throughput
axes[0, 1].plot(data["arrival_rate"], data["throughput"], marker='o', color='g')
axes[0, 1].set_title("Total Throughput")
axes[0, 1].set_xlabel("Arrival Rate (lambda)")
axes[0, 1].set_ylabel("Throughput")

# Plot for average CPU utilization
axes[1, 0].plot(data["arrival_rate"], data["cpu_utilization"], marker='o', color='r')
axes[1, 0].set_title("Average CPU Utilization")
axes[1, 0].set_xlabel("Arrival Rate (lambda)")
axes[1, 0].set_ylabel("CPU Utilization")

# Plot for average processes in the ready queue
axes[1, 1].plot(data["arrival_rate"], data["ready_queue_processes"], marker='o', color='purple')
axes[1, 1].set_title("Average Processes in the Ready Queue")
axes[1, 1].set_xlabel("Arrival Rate (lambda)")
axes[1, 1].set_ylabel("Ready Queue Processes")

# Display the plots
plt.tight_layout( rect=[0, 0, 1, 0.95],h_pad=4, w_pad=3)
plt.show()