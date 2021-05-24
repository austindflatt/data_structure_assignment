
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

def print_month():
    print('Pi day is in:', months[2])

birthday_locations = ['home', 'miami', 'california', 'atlanta', 'nashville']

birthday_locations.extend(['Puerto Rico', 'New York', 'Los Cabos'])

print(birthday_locations)

i = 0

while i < len(birthday_locations):
    print(birthday_locations[i])
    i += 1