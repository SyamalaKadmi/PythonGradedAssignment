# Q2. As a DevOps engineer, it is crucial to monitor the health and performance of servers. Write a Python program to monitor the health of the CPU. Few pointers to be noted:
# ●       The program should continuously monitor the CPU usage of the local machine.
# ●       If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed.
# ●       The program should run indefinitely until interrupted.
# ●       The program should include appropriate error handling to handle exceptions that may arise during the monitoring process.
 
import psutil

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print("Monitoring the cpu usage. Alerts will be displayed when the cpu usage exceeds 80%")
    while True:
        if usage > 80:
            print ("Alert! CPU usage exceeds threshold:  " , usage)

   
check_cpu_usage()

       


