# that reverse a string

def reverse(text):
    max_i = len(text) - 1

    rev = ""    # rev = 0 -> rev += "asda" -> Error
    for i in range(len(text)):
        text[i]  # a h o j
        rev += text[max_i - i]  # j o h z

    return rev


assert reverse("ahoj") == "joha"
assert reverse("kekel") == "lekek"
assert reverse("") == ""
