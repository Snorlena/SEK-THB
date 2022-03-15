import requests
import datetime
import matplotlib.pyplot as plt
import numpy as np

x = datetime.datetime.now()

fromYear = x.strftime("%y")
fromMonth = x.strftime("%m")

monthNow = int(x.strftime("%m"))
if monthNow == 1:
    fromMonth = "12"
    fromYear = int(x.strftime("%y")) -1
    fromYear = str(fromYear)
elif monthNow < 10:
    fromMonth = int(x.strftime("%m")) -1
    fromMonth = "0" + str(fromMonth)
else:
    fromMonth = int(x.strftime("%m")) - 1
    fromMonth = str(fromMonth)

fromDate = fromYear + "-" + fromMonth + "-" + x.strftime("%d")
toDate = x.strftime("%Y-%m-%d")
skro = requests.get("https://www.riksbank.se/sv/statistik/sok-rantor--valutakurser/?c=cAverage&f=Day&from=" + fromDate +"&g130-SEKTHBPMI=on&s=Dot&to=" + toDate + "&export=csv")

f = open("skrot.csv", "w")
f.write(skro.text)
f.close

f = open("skrot.csv", "r")
next(f)

database = {}

for line in f:
    line = line.strip("\n")
    line = line.split(";")
    line = line[0] + ";" + line[3]
    line = line.split(";")
    currentValue = float(line[1])
    currentValue = 1 / currentValue
    currentValue = round(currentValue, 4)
    database[line[0]] = currentValue


print("1 SEK =", currentValue, "THB")

x = list(database.keys())
y = list(database.values())
xpoints = np.array(x)
ypoints = np.array(y)

plt.plot(xpoints, ypoints)
plt.xticks(rotation=45)
plt.show()
