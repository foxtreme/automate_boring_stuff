import re
print(' begins patterns '.center(70, '='))
message = "Call me 451-582-1256, or at 891-135-1542"

phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_number_regex_parentheses = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# match_object = phone_number_regex.search(message)
match_object = phone_number_regex.findall(message)
match_object_parentheses = phone_number_regex_parentheses.search(message)
print(match_object)
print('with parentheses groups: area code:',
      match_object_parentheses.group(1),
      'phone number:',
      match_object_parentheses.group(2))
# ==================  pipe character regex ==================
print(' begins pipe character '.center(70, '='))
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())  # prints Batmobile
mo = bat_regex.search('Batmotorcycle lost a wheel')
# print(mo.group())  # fails
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group(1))  # prints which sufix was found

# =================== repetitions ======================
print(' begins repetitions '.center(70, '='))
bat_regex = re.compile(r'Bat(wo)?man') # question mark means can appear 1 or 0 times
mo = bat_regex.search("The adventures of Batman")
print(mo.group())
mo = bat_regex.search("The adventures of Batwoman")
print(mo.group())
mo = bat_regex.search("The adventures of Batwowowowoman")
print(mo == None)
message = "My phone number is 555-1234. Call me tomorrow"
print(message)
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_regex.search(message)
print('failed to found it?', mo == None)
print('Now with repetitions \'? mark\' ')
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phone_regex.search(message)
print(mo)
print('Now with * mark')
bat_regex = re.compile(r'Bat(wo)*man')
mo = bat_regex.search("The adventures of Batman")
print(mo)
mo = bat_regex.search("The adventures of Batwoman")
print(mo)
mo = bat_regex.search("The adventures of Batwowowowoman")
print(mo)
print('Now with + mark')
bat_regex = re.compile(r'Bat(wo)+man')
mo = bat_regex.search("The adventures of Batman")
print('Failed to find it?', mo == None)
mo = bat_regex.search("The adventures of Batwoman")
print(mo)
mo = bat_regex.search("The adventures of Batwowowowoman")
print(mo)
print('Now to match specific number of repetitions')
ha_regex = re.compile(r'(Ha){3}')
mo = ha_regex.search('He said HaHaHa')
print(mo)
print('Greedy match')
digit_regex = re.compile(r'(\d){3,5}')
mo = digit_regex.search('1234567890')
print(mo)
print('Non Greedy match')
digit_regex = re.compile(r'(\d){3,5}?')
mo = digit_regex.search('1234567890')
print(mo)
print(' begins findall method '.center(70, '='))

lyrics = '''
On the twelfth day of Christmas
my true love sent to me:
12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree'''

xmas_regex = re.compile(r'\d+ \w+')
mo = xmas_regex.findall(lyrics)
print(mo)
vowel_regex = re.compile(r'[aeiouAEIOU]')
mo = vowel_regex.findall('Robocop eats baby food')
print(mo)
double_vowel_regex = re.compile(r'[aeiouAEIOU]{2}')
mo = double_vowel_regex.findall('Robocop eats baby food')
print(mo)
negative_vowel_regex = re.compile(r'[^aeiouAEIOU]')
mo = negative_vowel_regex.findall('Robocop eats baby food')
print(mo)
print('^ at the beginning of regex means it has to begin with a given pattern')
print('$ at the end of regex means it has to end with a given pattern')
print('wildcard . (dot) means any character but new line')
at_regex = re.compile(r'.{1,2}at')
mo = at_regex.findall('The cat in the hat sat on the flat mat.')
print(mo)
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.findall('First Name: Chris Last Name: Charry')
print(mo)
serve = '<To serve humans> for dinner>.'
non_greedy = re.compile(r'<(.*?)>')
mo = non_greedy.findall(serve)
print('non greedy', mo)
greedy = re.compile(r'<(.*)>')
mo = greedy.findall(serve)
print('greedy', mo)
print('DOT ALL')
prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dot_star = re.compile(r'.*', re.DOTALL)
mo = dot_star.search(prime)
print(mo)
print(' begins sub method '.center(70, '='))
names_regex = re.compile(r'Agent \w+')
mo = names_regex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)
censured = names_regex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print (censured)
names_regex = re.compile(r'Agent (\w)\w+')
mo = names_regex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)
censured = names_regex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Chris.')
print(censured)
verbose_regex = re.compile(r'''
(\d\d\d-)| # area code (without parens,with dash)
(\(\d\d\d\)) # -or- area code with parens and no dash
\d\d\d #first 3 digits
- #second dash
\d\d\d\d #last 4 digits
\sx\d{2.4} # extension, like x1234
''', re.VERBOSE)