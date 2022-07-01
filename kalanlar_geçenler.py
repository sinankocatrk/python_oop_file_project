def kaldimi (satir):
  

    liste = satir.split("------------------> ")

    isim = liste[0]

    harf_notu = liste[1]

    temp=0
    
    if harf_notu=="FF\n":
        temp=0
    elif harf_notu== "FD\n":
        temp=0
    elif harf_notu== "DD\n":
        temp=0    
    else:
        temp=1

    if temp==0:
        return isim + " kaldi"
    elif temp==1:
        return isim + " geçti"




with open("notlar.txt","r+",encoding= "utf-8") as file:

    eklenecekler_listesi = []
    geçenler_listesi= []
    kalanlar_listesi= []

    for i in file:

        nesne=kaldimi(i)
        
        liste1 = nesne.split(" ")

        isim = liste1[0]

        soyisim = liste1[1]

        kalma_durumu = liste1[2]

        if (kalma_durumu=="geçti"):
            geçenler_listesi.append(isim +" "+ soyisim +" "+ kalma_durumu +"\n")
        elif (kalma_durumu=="kaldi"):
            kalanlar_listesi.append(isim +" "+soyisim +" "+ kalma_durumu +"\n")



    for i in eklenecekler_listesi:
        

        if (kalma_durumu=="geçti"):
            geçenler_listesi.append(kaldimi(i))

        elif (kalma_durumu=="kaldi"):
            kalanlar_listesi.append(kaldimi(i))

    
    with open("geçenler.txt","w",encoding="utf-8") as file1:
        for i in geçenler_listesi:
            file1.write(i)       
    with open("kalanlar.txt","w",encoding="utf-8") as file2 :
        for i in kalanlar_listesi:
            file2.write(i)  
print(geçenler_listesi)
print(kalanlar_listesi)

        




