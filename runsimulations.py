import subprocess

service_time = 0.04
for arrival_rate in range(10, 31):
    subprocess.run(["python", "PA2.py", str(arrival_rate), str(service_time)])