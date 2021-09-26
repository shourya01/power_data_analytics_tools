import wget


def download_file(day):
    url = "http://content.caiso.com/green/renewrpt/" + day + "_DailyRenewablesWatch.txt"
    wget.download(url, "Data/" + day + "_DailyRenewablesWatch.txt")


months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
months_leap = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for i in range(6, 13):
    for j in range(1, months[i]+1):
        try:
            download_file("2018" + f"{i:02d}" + f"{j:02d}")
        except:
            print("2018" + f"{i:02d}" + f"{j:02d}")
            continue

for i in range(1, 13):
    for j in range(1, months[i]+1):
        try:
            download_file("2019" + f"{i:02d}" + f"{j:02d}")
        except:
            print("2019" + f"{i:02d}" + f"{j:02d}")
            continue

for i in range(1, 13):
    for j in range(1, months_leap[i]+1):
        try:
            download_file("2020" + f"{i:02d}" + f"{j:02d}")
        except:
            print("2020" + f"{i:02d}" + f"{j:02d}")
            continue

for i in range(1, 13):
    for j in range(1, months[i]+1):
        try:
            download_file("2021" + f"{i:02d}" + f"{j:02d}")
        except:
            print("2021" + f"{i:02d}" + f"{j:02d}")
            continue
