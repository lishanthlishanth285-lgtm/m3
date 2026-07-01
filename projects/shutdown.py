def shut_down():
    print("Shutting down the system...")

option = input("Do you want to shut down the system? (yes/no): ")
if option() == "yes":
    shut_down()
else:
    print("Shutdown canceled.")