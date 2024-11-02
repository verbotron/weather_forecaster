print("\t\t--------------------------")
print("\t\tPrevisão do Tempo de n00b")
print("\t\t--------------------------\n\n")
cidade = input("Fala a cidade, vacilão! ")
print("\n\n")

import requests

def report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Deu ruim..."
    print(T)

print("Guenta aí...\n\n")

report(cidade)
