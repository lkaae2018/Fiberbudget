import math
L=35
#math.ceil runder op til det højste tal d.v.s 2,2 bliver rundet op til 3
print(math.ceil(L/10))
#Printer ud dæmpningen som skal lægges til fiberbugdettet afhængig af antal 10km fiberstrækninger
print(math.ceil(L/10)*0.5)

fiber=float(input("Indtast antal km SM fiber?"))
splidsninger=int(input("Antal splidsninger?"))
konnekteringer=int(input("Antal konnekteringer?"))
#Udregn dæmpningen for 1310nm og 1550nm!
#Træk sikerhedsmargin og reperationer dæmpning fra
#Beregn en samlet dæmpning for de øvereste tal i variable!
while True:
    Transmitpower=float(input("Indtast TX power for SFP modul[dBm]"))
    receivesensitivity=float(input("Indtast modtager følsomhed[dBm]"))
    


