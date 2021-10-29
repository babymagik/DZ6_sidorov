with open ('nginx_logs.txt') as f:
    data = []
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6])
print(data)



from  itertools import zip_longest
import  json

out_dict = {}
with open('users.csv', encoding='utf-8') as users:
    num_lines_users = sum(1 for line in users)
    num_lines_hobby = sum(1 for line in hobby)

    if num_lines_users < num_lines_hobby
        exit(1)

        user.seek(0)
        hobby.seek(0)
        for line_user, line_user_hobby in zip_longest(users, hobby):
            out_dict[line_user.stip()] = line_user_hobby.strip() of line_user_hobby is not None else line_user_hobby

with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(out_dict, f,)
print(out_dict)


import  sys

price = sys.argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(price + '\n')


11