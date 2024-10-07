import random

rs=random.randint(1,50)
ds=5

print("sayi tahmin oyununa hosgeldiniz")

print(f"1 ve 50 arasinda bir sayi tuttum. bu sayiyi {ds} denemede bulmaya calismalisin")

while ds>0:
    tahmin=int(input("tahmin ettiginiz sayiyi girin:"))
    if tahmin>50 or tahmin<1:
       print("1 ve 50 arasinda bir sayi girmen gerekiyor.\ntekrar basla.")
       exit()

    if tahmin>rs:
        print("tutturamadin...daha kucuk sayi girmen gerekiyor.")

    elif tahmin<rs:
        print("tutturamadin...daha buyuk sayi girmen gerekiyor.")

    elif tahmin==rs:
        print("tebrikler. sayiyi bulmayi basardin")

    ds-=1
    print(f"kalan hakkin:{ds}")

    if ds==0:
        print(f"uzgunum...sayiyi bulamadin...aklimdaki sayi: {rs} idi")


