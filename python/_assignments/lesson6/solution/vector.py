import math


def is_float(str):
    pass


def size_dict(vektor):
    x = vektor.get("x")
    y = vektor.get("y")
    z = vektor.get("z")

    # TODO will it work? (it wil not for two floats - ex. x=3.1 y=1.4 z=4)
    test = f'{x}{y}{z}'  # 31211

    if is_float(test) == True:
        size = math.sqrt(x**2 + y**2 + z**2)
        return size
    else:
        return print("Funkci musíme zadat slovník s parametry x, y a z, které obsahují číselné hodnoty")


def size_tuple(vektor):
    # destructuring
    x, y, z = vektor
    # x = vektor[0]
    # y = vektor[1]
    # z = vektor[2]

    test = str(f'{x}' + f'{y}' + f'{z}')
    if is_float(test) == True:
        size = math.sqrt(x**2 + y**2 + z**2)
        return size
    else:
        return print("Funkci musíme zadat tuple se třemi číselnými hodnotami")
