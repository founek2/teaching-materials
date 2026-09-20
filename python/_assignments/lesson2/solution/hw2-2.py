from_text = "Zadej dolni mez intervalu: "
end_text = "Zadej horní mez intervalu: "


# start = int(input("Zadej dolni mez intervalu: "))
start = int(input(from_text))
end = int(input(end_text))

while start > end:
    print("Spatne zadane hodnoty intervalu, zadej hodnoty znovu")
    start = int(input(from_text))
    end = int(input(end_text))

# if a > b:
#     print("Zadal jsi špatnou hodnotu, zkus to znovu!")
#     exit()

suma = 0
for i in range(start, end+1):
    suma = suma + i

print("Soucet cisel v intervalu je", suma)
