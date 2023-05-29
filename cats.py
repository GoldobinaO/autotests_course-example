cats_data = [('Мартин', 5, 'Алексей', 'Егоров'),
             ('Фродо', 3, 'Анна', 'Самохина'),
             ('Вася', 4, 'Алексей', 'Егоров')]

result = {}
for cat in cats_data:
    temp = cat[0] + ', ' + str(cat[1])
    result.setdefault(cat[2:], []).append(temp)
for k, v in result.items():
    our_str = (' '.join(k) + ':', '; '.join(v))

    print(our_str)
