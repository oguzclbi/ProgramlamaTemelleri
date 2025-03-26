bellekler=["RAM", "ROM"] 
ekran_kartlari=["Paylaşımlı", "Paylaşımsız"]
sabit_diskler=["SSD"]
birimler=bellekler, ekran_kartlari, sabit_diskler 
print(birimler) #(['RAM', 'ROM'], ['Paylaşımlı', 'Paylaşımsız'], ['SSD'])
print(birimler[0][1]) #ROM
print(birimler[1][1]) #Paylaşımsız
print(birimler[0][1], birimler[2][0]) #ROM, SSD