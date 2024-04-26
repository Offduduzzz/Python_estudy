import datetime

print('Military enlistment.')

now_year = datetime.datetime.now().year

while True:
    year_user = input('What year were your born in: ')
    try:
        int_year_user = int(year_user)
        age_user = (now_year - int_year_user)
        if now_year - int_year_user > 18:
            print('Mandatory enlistment.')
            print(f'age:{age_user}')
        elif now_year - int_year_user < 18:
            print('Non-mandatory enlistment.')
            print(f'age:{age_user}')
        elif now_year - int_year_user == 18:
            print('You have reached enlistment age.')
            print(f'age:{age_user}')
    except ValueError:
        print('Unacceptable information.')