import matplotlib.pylab as plt
import numpy as np
import seaborn as sns
import pandas as pd


data = pd.read_csv("BostonCrime.csv")

def loadCrimes():
    districtArray = data.iloc[:, 4:5].to_numpy()
    dayArray = data.iloc[:, 10:11].to_numpy()
    matchedArray = np.concatenate((districtArray, dayArray), axis = 1)    
    return matchedArray
def loadCrimeMonth():
    districtArray = data.iloc[:, 4:5].to_numpy()
    dayArray = data.iloc[:, 9:10].to_numpy()
    matchedArray = np.concatenate((districtArray, dayArray), axis = 1)    
    return matchedArray
def loadCrimeHour():
    districtArray = data.iloc[:, 4:5].to_numpy()
    dayArray = data.iloc[:, 11:12].to_numpy()
    matchedArray = np.concatenate((districtArray, dayArray), axis = 1)    
    return matchedArray

def loadDistricts():
    allDistricts = data["DISTRICT"].unique() #np array
    c = (allDistricts != "External")
    allDistricts = allDistricts[c]
    allDistricts = allDistricts[~pd.isnull(allDistricts)]
    return allDistricts


def dayDistrictNum():
    matchedArray = loadCrimes()
    allDistricts = loadDistricts() #['B2' 'D14' 'C11' 'E13' 'D4' 'A7' 'C6' 'A1' 'B3' 'A15' 'E18' 'E5']
    allDays = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    finalArray = []
    for district in allDistricts:
        d = matchedArray[:, 0] == district
        matchedDistrFix = matchedArray[d]
        for day in allDays:
            c = matchedDistrFix[:, 1] == day
            matchedDayFix = matchedDistrFix[c]
            total = len(matchedDayFix)
            tempArrayOfDays = [district, day, total]
            finalArray.append(tempArrayOfDays)
    df = pd.DataFrame(finalArray, columns =['Day of Week', 'District', 'Number of Crimes'])
    df = df.pivot("District", "Day of Week", "Number of Crimes")
    return df
    
def perCapitaCrime():
    districtPop = [59702, 43880, 111982, 37468, 24577, 40508, 33688, 13827, 36480, 20504, 27517, 30336]
    allDistricts = loadDistricts()
    firstList = dayDistrictNum()
    for i in range(len(districtPop)):
        firstList[allDistricts[i]] = firstList[allDistricts[i]]/districtPop[i]
    return firstList

def SoxSeasons():
    matchedArray = loadCrimeMonth()
    monthArray = np.array(range(0, 12))
    districts = loadDistricts()
    FinalReturn = []
    for district in districts:
        d = matchedArray[:, 0] == district
        matchedDistrFix = matchedArray[d]
        for month in monthArray:
            c = matchedDistrFix[:, 1] == month
            matchedDayFix = matchedDistrFix[c]
            total = len(matchedDayFix)
            tempArrayOfDays = [district, month, total]
            FinalReturn.append(tempArrayOfDays)
    df = pd.DataFrame(FinalReturn, columns =['District', 'month', 'Number of Crimes'])
    newdf = df.pivot("month", "District", "Number of Crimes")
    newdf = newdf.drop(labels = [0,11], axis=0, inplace=False) 
    newdf.index = ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
    return newdf
def perCapitaSoxSeasons():
    districtPop = [59702, 43880, 111982, 37468, 24577, 40508, 33688, 13827, 36480, 20504, 27517, 30336]
    allDistricts = loadDistricts()
    hotFuzz = SoxSeasons()
    for i in range(12):
        hotFuzz[allDistricts[i]] = hotFuzz[allDistricts[i]]/districtPop[i]
    return hotFuzz

def hourCrimes():
    matchedArray = loadCrimeHour()
    hourArray = np.array(range(0, 24))
    districts = loadDistricts()
    FinalReturn = []
    for district in districts:
        d = matchedArray[:, 0] == district
        matchedDistrFix = matchedArray[d]
        for hour in hourArray:
            c = matchedDistrFix[:, 1] == hour
            matchedDayFix = matchedDistrFix[c]
            total = len(matchedDayFix)
            tempArrayOfDays = [district, hour, total]
            FinalReturn.append(tempArrayOfDays)
    df = pd.DataFrame(FinalReturn, columns =['District', 'hour', 'Number of Crimes'])
    newdf = df.pivot("District", "hour", "Number of Crimes")
    newdf = newdf.transpose()
    return newdf
def perCapitaHourCrimes():
    districtPop = [59702, 43880, 111982, 37468, 24577, 40508, 33688, 13827, 36480, 20504, 27517, 30336]
    allDistricts = loadDistricts()
    hotFuzz = hourCrimes()
    for i in range(12):
        hotFuzz[allDistricts[i]] = hotFuzz[allDistricts[i]]/districtPop[i]
    return hotFuzz

def main():
#
#
#
# HOW TO USE:
# Uncomment out one group of lines at a time to display different graphs.
#
#
#

    #sns.heatmap(dayDistrictNum())
    #plt.xlabel('District')
    #plt.ylabel('Day of Week')


    
    #df = perCapitaCrime()    
    #df_norm_col=(df-df.mean())/df.std()
    #sns.heatmap(df_norm_col, cmap='viridis')
    #plt.xlabel('District')
    #plt.ylabel('Day of Week')
    

    #sns.heatmap(SoxSeasons())
    

    #sns.heatmap(hourCrimes())
    #plt.ylabel('Hour (Army Time)')


    #df = perCapitaHourCrimes()
    #df_norm_col1=(df-df.mean())/df.std()
    #sns.heatmap(df_norm_col1, cmap='viridis')
    #plt.ylabel('Hour (Army Time)')
    

    #df = perCapitaSoxSeasons()    
    #df_norm_col1=(df-df.mean())/df.std()
    #sns.heatmap(df_norm_col1, cmap='viridis')
    
    plt.show()
if __name__ == "__main__":
    main()