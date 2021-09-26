import os


fout = open("power_generation.csv", "a")
fout.write("Timestamp,Geothermal,Biomass,Biogas,Small Hydro,Wind Total,Solar PV,Solar Thermal,Renewables,Nuclear,Thermal,Imports,Hydro\n")

for filename in os.listdir("Data"):
    file = open("Data\\" + filename)
    file.readline() # skip the header
    for line in file:
        fout.write(line)
    file.close()
    print("...Done")
fout.close()
