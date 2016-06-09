def timeCalculator (time1, time2):
    spaceL1 = time1.find(" ") + 1
    spaceL2 = time2.find(" ") + 1
    time1 = time1[spaceL1:]
    time2 = time2[spaceL2:]
    listOfTime1 = time1.split(":")
    listOfTime2 = time2.split(":")
    time1_seconds = 3600 * int(listOfTime1[0]) + 60 * int(listOfTime1[1]) + int(listOfTime1[2])
    time2_seconds = 3600 * int(listOfTime2[0]) + 60 * int(listOfTime2[1]) + int(listOfTime2[2])
    diff_seconds = time2_seconds - time1_seconds
    hours = diff_seconds / 3600
    minutesAndSeconds = diff_seconds % 3600
    minutes = minutesAndSeconds / 60
    seconds = minutesAndSeconds % 60
    
    finalTime = {
                    "hours"   : hours,
                    "minutes" : minutes,
                    "seconds" : seconds,
                }
    return finalTime

if __name__ == "__main__":
    start = "2016-06-08 21:21:07"
    end = "2016-06-08 22:14:08"
    print timeCalculator(start, end)