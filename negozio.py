import requests
import json
rip=True
while rip:
    categorie=requests.get("https://fakeapi.net/products/categories")
    if categorie.status_code != 200:
        print("impossibile")
    else:
        n=0
        x=json.loads(categorie.text) #lista
        for i in x:
            n+=1
            print(f"{n}-{i}")
        giusto=False
        while not giusto:
            try:
                scelta=int(input("scegli: "))
                if scelta>=1 and scelta<=9:
                    giusto=True
                else:
                    print("metti un numero da 1 a 9")
            except:
                print("formato non giusto")
        e=x[scelta-1]
        prodotti=requests.get(f"https://fakeapi.net/products/category/{e}")
        g=json.loads(prodotti.text)
        elencoid=[]
        for r in g["data"]:
            print(r["id"])
            print(r["title"])
            print(r["price"])
        elencoid.append(r["id"])
        giusto=False
        while not giusto:
            try:
                pr=int(input("quale prodotto vuoi visuallizare?"))
                if pr in elencoid:
                    giusto=True
                else:
                    print("errore")
            except:
                print("formato non coretto")
        t=requests.get(f"https://fakeapi.net/products/{pr}")
        h=json.loads(t.text)

        print(h["id"])
        print(h["title"])
        print(h["price"])
        print(h["brand"])
        print(h["description"])



            