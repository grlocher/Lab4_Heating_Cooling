def heating_cooling(actual_temp: float,
                    desired_temp: float) -> float:

    if actual_temp < desired_temp:
        print('Run heat')
    elif actual_temp > desired_temp:
        print('Run A/C')
    else:
        print('Standby')


actual_temp = float(input('Enter the current temperature: '))
desired_temp = float(input('Enter the desired temperature: '))
print(f'Current temp {actual_temp}')
print(f'Desired temp {desired_temp}')

heating_cooling(actual_temp, desired_temp)


def convert_temp(temp_celsius: float, target_unit: str):

    if target_unit == 'F':
        return (temp_celsius * 9 / 5) + 32
    elif target_unit == 'K':
        return temp_celsius + 273.15
    else:
        return temp_celsius


temp_celsius = float(input('Enter the temperature in Celsius: '))
target_unit = str(input('Enter the desired temperature unit: ').upper())
print(f'Current temperature in Celsius {temp_celsius}')
print(f'Temperature is desired in {target_unit}')
print(f'New temperature is {convert_temp(temp_celsius, target_unit)}')