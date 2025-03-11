#Inflasjonsmål målt i KPI-JAE

import numpy as np
import csv
import matplotlib.pyplot as plt

#Finner csv-filen jeg skal jobbe med
filnavn = "Datasett\Inflasjon.csv"

#Lager lister for data
måned = []
inflasjon = []

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")
  x = 0

  for rad in filinnhold:
    måned.append(x)

    #Teller antall måneder etter januar 2015
    x += 1

    inflasjon.append(float(rad[1]))

#Lager liste med årstall
startår = 2015
sluttår = 2025
årstall = list(range(startår, sluttår + 1))

#Gjør at et nytt årstall dukker opp på x-aksen for hver 12 måned som går
år_måned_index = [i * 12 for i in range(len(årstall))]

#Justerer størrelse på graf
fig, ax = plt.subplots(figsize=(10, 5))

plt.plot(måned, inflasjon, label="Inflasjon", color="blue")
plt.title("$Inflasjonstallene \ i \ perioden \ 2015-2025$")
plt.xlabel("$Årstall$")
plt.ylabel("$Inflasjon \ (KPI-JAE)$")
plt.xticks(år_måned_index, årstall)   #Setter x-akseverdiene slik at de samsvarer med datasettet
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8])  #Gjør y-aksen lettere lesbar

plt.grid()
plt.legend()
plt.show()