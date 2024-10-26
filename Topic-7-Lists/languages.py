languages = ['Python', 'Java', 'Javascript', 'Swift', 'C#', 'Swift']

#adds Kotlin to end of languages list
languages.append('Kotlin')

#removes swift string from languages list
languages.remove('Swift')

print(languages)

#prints languages in sequence
for language in languages:
    print(language)

#creates new variable and uses it to print languages separated by !
all_languages = '!'.join(languages)
print(all_languages)
#sorts in alphabetical order
languages.sort()
print(languages)
#reverses order from above
languages.reverse()
print(languages)