import random

#Drop
NB2000 = 3882.62
NE2000 = 2470.52

#Drop
NB2001 = 2407.65
NE2001 = 2059.38

#Drop#
NB2002 = 2022.46
NE2002 = 1387.08

NB2003 = 1447.72
NE2003 = 2006.68

#Drop#
NB2004 = 2086.92
NE2004 = 2175.44

NB2005 = 2088.61
NE2005 = 2205.32

NB2006 = 2305.62
NE2006 = 2415.29

NB2007 = 2434.25
NE2007 = 2504.65

#drop
NB2008 = 2439.94
NE2008 = 1632.21

NB2009 = 1571.59
NE2009 = 2269.15

NB2010 = 2317.17
NE2010 = 2652.87

#drop#
NB2011 = 2703.17
NE2011 = 2605.15

NB2012 = 2674.22
NE2012 = 3101.66

NB2013 = 3125.63
NE2013 = 4131.91

NB2014 = 4174.67
NE2014 = 4726.81

NB2015 = 4704.07
NE2015 = 5007.41

NB2016 = 4643.63
NE2016 = 5383.12

NB2017 = 5521.06
NE2017 = 6903.39

#drop#
NB2018 = 7136.56
NE2018 = 6738.86

NB2019 = 6971.48
NE2019 = 9020.77

GainTotal = round((NE2019 - NB2000),2)
print("The gain from 2000 to 2019 is", GainTotal)


YT2000 = (NE2000 - NB2000)
print("The loss for 2000: ", round(YT2000,2))
YT2001 = (NE2001 - NB2001)
print("The loss for 2001: ", round(YT2001,2))
YT2002 = NE2002 - NB2002
print("The loss for 2002: ", round(YT2002,2))
YT2003 = NE2003 - NB2003
print("The gain for 2003: ", round(YT2003,2))
YT2004 = NE2004 - NB2004
print("The loss for 2004: ", round(YT2004,2))
YT2005 = NE2005 - NB2005
print("The gain for 2005: ", round(YT2005,2))
YT2006 = NE2006 - NB2006
print("The gain for 2006: ", round(YT2006,2))
YT2007 = NE2007 - NB2007
print("The gain for 2007: ", round(YT2007,2))
YT2008 = NE2008 - NB2008
print("The loss for 2008: ", round(YT2008,2))
YT2009 = NE2009 - NB2009
print("The gain for 2009: ", round(YT2009,2))
YT2010 = NE2010 - NB2010
print("The gain for 2010: ", round(YT2010,2))
YT2011 = NE2011 - NB2011
print("The loss for 2011: ", round(YT2011,2))
YT2012 = NE2012 - NB2012
print("The gain for 2012: ", round(YT2012,2))
YT2013 = NE2013 - NB2013
print("The gain for 2013: ", round(YT2013,2))
YT2014 = NE2014 - NB2014
print("The gain for 2014: ", round(YT2014,2))
YT2015 = NE2015 -NB2015
print("The gain for 2015: ", round(YT2015,2))
YT2016 = NE2016 - NB2016
print("The gain for 2016: ", round(YT2016,2))
YT2017 = NE2017 - NB2017
print("The gain for 2017: ", round(YT2017,2))
YT2018 = NE2018 - NB2018
print("The gain for 2018: ", round(YT2018,2))
YT2019 = NE2019 - NB2019
print("The gain for 2019: ", round(YT2019,2))

AM0 = ((YT2000 / NB2000) * 100)
print("2000's percent of change: ", round(AM0,2))
AM1 = ((YT2001 / NB2001) * 100)
print("2001's percent of change: ", round(AM1,2))
AM2 = ((YT2002 / NB2002) * 100)
print("2002's percent of change: ", round(AM2,2))
AM3 = ((YT2003 / NB2003) * 100)
print("2003's percent of change: ", round(AM3,2))
AM4 = ((YT2004 / NB2004) * 100)
print("2004's percent of change: ", round(AM4,2))
AM5 = ((YT2005 / NB2005) * 100)
print("2005's percent of change: ", round(AM5,2))
AM6 = ((YT2006 / NB2006) * 100)
print("2006's percent of change: ", round(AM6,2))
AM7 = ((YT2007 / NB2007) * 100)
print("2007's percent of change: ", round(AM7,2))
AM8 = ((YT2008 / NB2008) * 100)
print("2008's percent of change: ", round(AM8,2))
AM9 = ((YT2009 / NB2009) * 100)
print("2009's percent of change: ", round(AM9,2))
AM10 = ((YT2010 / NB2010) * 100)
print("2010's percent of change: ", round(AM10,2))
AM11 = ((YT2011 / NB2011) * 100)
print("2011's percent of change: ", round(AM11,2))
AM12 = ((YT2012 / NB2012) * 100)
print("2012's percent of change: ", round(AM12,2))
AM13 = ((YT2013 / NB2013) * 100)
print("2013's percent of change: ", round(AM13,2))
AM14 = ((YT2014 / NB2014) * 100)
print("2014's percent of change: ", round(AM14,2))
AM15 = ((YT2015 / NB2015) * 100)
print("2015's percent of change: ", round(AM15,2))
AM16 = ((YT2016 / NB2016) * 100)
print("2016's percent of change: ", round(AM16,2))
AM17 = ((YT2017 / NB2017) * 100)
print("2017's percent of change: ", round(AM17,2))
AM18 = ((YT2018 / NB2018) * 100)
print("2018's percent of change: ", round(AM18,2))
AM19 = ((YT2019 / NB2019) * 100)
print("2019's percent of change: ", round(AM19,2))

TPOC = (AM0 + AM1 + AM2 + AM3 + AM4 + AM5 + AM6 + AM7 + AM8 + AM9 + AM10 + AM11 + AM12 + AM13 + AM14 + AM15 + AM16 + AM17 + AM18 + AM19)
print("The total percent of change from 2000 to 2019 =",round(TPOC,2))

#Average change from 2000 to 2019
APOC = ((AM0 + AM1 + AM2 + AM3 + AM4 + AM5 + AM6 + AM7 + AM8 + AM9 + AM10 + AM11 + AM12 + AM13 + AM14 + AM15 + AM16 + AM17 + AM18 + AM19)/20)
print("The average percent of change for each year from 2000 to 2019 =", round(APOC,2))

#2^64#
#
#Percent of Change#
POC = input("Enter your predictabily percent of increase of decrease: ")
POC1 = input("Enter the year's percent of change: ")
POC2 = (float(POC)/100) * float(POC1)
POC3 = (9178.86 * ((float(POC2) + float(POC1))/100)) + 9178.86
print("The predictability based on the percent of change from the previous year, incorporating another", POC,"% of change,", "The market will change to",round(POC3,2))



 
################## Dow Jones #################

##NB2000 = 3882.62
##NE2000 = 2470.52
##
##NB2001 = 
##NE2001 =
##
##NB2002 = 
##NE2002 =
##
##NB2003 = 
##NE2003 =
##
##NB2004 = 
##NE2004 =
##
##NB2005 = 
##NE2005 =
##
##NB2006 = 
##NE2006 =
##
##NB2007 = 
##NE2007 =
##
##NB2008 = 
##NE2008 =
##
##NB2009 = 
##NE2009 =
##
##NB2010 = 
##NE2010 =
##
##NB2011 = 
##NE2011 =
##
##NB2012 = 
##NE2012 =
##
##NB2013 = 
##NE2013 =
##
##NB2014 = 
##NE2014 =
##
##NB2015 = 
##NE2015 =
##
##NB2016 = 
##NE2016 =
##
##NB2017 = 
##NE2017 =
##
##NB2018 = 
##NE2018 =
##
##NB2019 = 
##NE2019 =
