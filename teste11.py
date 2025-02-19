def grauscelsius(celsius):
    return (celsius * 9 / 5) + 32 

celsius = float(input("Digite a temperatura em graus celsius: "))

fahrenheit = grauscelsius(celsius)

print(f"{celsius} C equivalem a {fahrenheit:.2f}F")