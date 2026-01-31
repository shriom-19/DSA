#day of the week
d=int(input(" enter the date :"))
i=int(input(" enter month in number: "))
y=int(input(" enter year: "))

def day_of_week(d, m, y):
    # Predefined month codes for each month
    month_code = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    # Adjust year for January and February
    if m < 3:
        y -= 1  # If month is January or February, treat them as part of the previous year

    # Calculate the year code
    year_code = (y % 100) + (y % 100) // 4

    # Adjust year code for the century
    year_code = (year_code + (y // 100) // 4 + 5 * (y // 100)) % 7

    # Calculate the day of the week and return the value as an integer
    return (d + month_code[m - 1] + year_code) % 7

print(day_of_week(d,i,y))