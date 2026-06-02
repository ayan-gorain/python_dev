def reverse(str):
    start=0
    end=len(str)-1

    text=list(str)

    while start < end:
        text[start], text[end]=text[end],text[start]

        start+=1
        end-=1

    print("".join(text))
reverse("hello")


# method 2

def reverse2(str):
    print(str[::-1])

reverse("ayan")    