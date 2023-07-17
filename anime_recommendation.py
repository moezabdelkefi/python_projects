from random import choice

animes = [
    ['naruto', 'action', 'forever', 'series'],
    ['Demon slayer', 'killing','short', 'series'],
    ['The seven deadly since', 'short', 'series'],
    ['Black clover', 'fantasia','japenees', 'series']
]

print('What mood are you in?')
mood = input()

matched_animes = [anime_info[0] for anime_info in animes if anime_info[1] == mood]

if matched_animes:
    random_recommendation = choice(matched_animes)
    print(mood + ' anime recommendation: ' + random_recommendation)
else:
    print('No anime found for the given mood.')
