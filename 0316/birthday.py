import random

Trials = 100000
same_birthdays = 0

for _ in range(Trials):
    birthdays = []
    for i in range(15):
        birthday = random.randint(1,365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

print(f'{same_birthdays / Trials * 100}%')

# f-string 관련
# https://blockdmask.tistory.com/429 