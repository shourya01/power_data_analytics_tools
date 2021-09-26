import pandas as pd
import os


def del_col(filename):
    file = pd.read_csv(filename)
    header = "Timestamp,Geothermal,Biomass,Biogas,Small Hydro,Wind Total,Solar PV,Solar Thermal,Renewables,Nuclear,Thermal,Imports,Hydro"
    keep_col = header.split(',')
    new_file = file[keep_col]
    new_file.to_csv(filename, index=False)


#del_col("test.csv")

for filename in os.listdir("Data"):
    if filename.endswith(".csv"):
        del_col("Data\\" + filename)
        print("...Done: " + filename)
