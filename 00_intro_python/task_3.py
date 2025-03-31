def tem_farenhit():
    temperature = float(input("Enter temperature in Fahrenheit! "))
    degrees_celsius = (temperature - 32) * 5.0/9.0
    print(f"Temperature:{temperature: .1f}F = {degrees_celsius:.2f}C") 
tem_farenhit()