start = int(input("Zadej dolni mez interval: "))
end = int(input("Zadej horní mez intervalu: "))

while start > end:
    print("Spatne zadane hodnoty intervalu, zadej hodnoty znovu")
    start = int(input("Zadej dolni mez interva "))
    end = int(input("Zadej horní mez intervalu: "))

# if start > end:
#     print("Zadal jsi špatnou hodnotu, zkus to znovu!")
#     exit()

suma = 0
for i in range(start, end+1):
    suma = suma + i

print("Soucet cisel v intervalu je", suma, suma, suma)
