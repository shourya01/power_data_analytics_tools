import fileinput
import os


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


header = "Timestamp,Geothermal,Biomass,Biogas,Small Hydro,Wind Total,Solar PV,Solar Thermal,Hour,Renewables,Nuclear,Thermal,Imports,Hydro\n"

#replace_line("test.txt", 0, header)

for filename in os.listdir("Data"):
    if filename.endswith(".txt"):
        replace_line("Data\\" + filename, 0, header)
        print("...Done")
