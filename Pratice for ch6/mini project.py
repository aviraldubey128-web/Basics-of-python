# Print a countdown before something “exciting” happens (like “Launching...” or “Happy New Year!”).

import time

countdown = (int(input("Enter the number of seconds for the countdown: ")))

print("Countdown starting...")
for i in range (countdown, 0,-1):
    print(i)
    time.sleep(1)
print("Launching... the app")