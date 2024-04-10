# temp from celcius to kelvin & celcius to fareneit

temp_celcius = int(input("Enter the temperature in celcius: "))

def temp_kelvin():
    return(temp_celcius+273.15)

def temp_farenheit():
    return(1.8*temp_celcius+32)
    
kelvin = temp_kelvin()
farenheit = temp_farenheit()

print("Given temperature in kelvin is ", kelvin)
print("Given temperature in kelvin is ", farenheit)