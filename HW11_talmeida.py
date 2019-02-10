# This code prints out plots for the following.
# Plot 1: Position [mm] v time [s]
# Plot 2: 3 subplots: position[mm] v time[s], velocity[mm/s] v time[s], 
# acceleration[mm/s^2] v time[s]
# Plot 3: velocity [in] v position [in]
# Plot 4: position[mm], velocity[mm/s], acceleration[mm/s^2] v time[s]
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
import matplotlib.pyplot as plt
import csv

with open('soundData.csv', 'r', newline='') as file:
    # opens csv file and breaks it into spreadsheet by commas
    reader = csv.reader(file, delimiter=',')
    soundData = []
    # for every row in reader, that data set is added to soundData list
    for row in reader:
        soundData.append(row)

time = []
pos = []
vel = []
acc = []
#---------------------------------------------------
#  Computations
#---------------------------------------------------
for row in soundData:
    time.append(float(row[0]))
    pos.append(float(row[1]))
    vel.append(float(row[2])) # in mm / s
    acc.append(float(row[3])) # in mm / s^2
#---------------------------------------------------
#  Outputs
#--------------------------------------------------- 
figure1 = plt.figure(1)
plt.plot(time, pos, c='red', marker='^')
plt.title("Position v Time") 
plt.xlabel("Time [s]") 
plt.ylabel("Position [mm]")

figure2 = plt.figure(2)
figure2a = figure2.add_subplot(232)
plt.plot(time, pos, c='black')
plt.title("Position v Time") 
plt.xlabel("Time [s]") 
plt.ylabel("Position [mm]")

figure2b = figure2.add_subplot(234)
plt.plot(time, vel, c='blue')
plt.title("Velocity v Time") 
plt.xlabel("Time [s]") 
plt.ylabel("Velocity [mm/s]")

figure2c = figure2.add_subplot(236)
plt.plot(time, acc, c='yellow', marker = "s")
plt.title("Acceleration v Time") 
plt.xlabel( "Time [s]") 
plt.ylabel( "Acceleration [mm/s^2]" )

velIN = [] # inches / min
posIN = [] # inches

for row in vel:
    velIN.append(float(row) * (.0393701 / 60))
   
for row in pos:
    posIN.append(float(row) * .0393701)

figure3 = plt.figure(3)
plt.plot(velIN, posIN, c='orange', ls = '--')
plt.title("Position v Velocity") 
plt.xlabel("Position [in]") 
plt.ylabel("Velocity [in/min]")

figure4 = plt.figure(4)
plt.plot(time, pos, c="blue", marker = "*", label = "Position [mm] v Time")
plt.plot(time, vel, c= "red", marker = "D", label = "Velocity [mm/s] v Time")
plt.plot(time, acc, c= "green", label = "Acceleration [mm/s^2] v Time")
plt.title("Position, Velocity, Acceleration v Time") 
plt.xlabel( "Time [s]") 
plt.legend(loc="best")
