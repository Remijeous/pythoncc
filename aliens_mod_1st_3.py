aliens = []

for alien_number in range(30):
    new_alien = {'speed':'low', 'color':'red', 'points':5}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['speed'] == 'low':
        alien['speed'] = 'medum'
        alien['color'] = 'yellow'
        alien['points'] = 10

for alien in aliens[:6]:
    print(alien)
