def calculate_pet_ages(humanYears):
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]


# Ejemplo de uso:
human_years = 10  # Puedes cambiar este valor para probar con otros
print(calculate_pet_ages(human_years))