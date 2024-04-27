print('Média das notas.')
while True:
    score_one = input('Write your grade: ')
    score_two = input('Write your second grade: ')
    try:
        float_score_one = float(score_one)
        float_score_two = float(score_two)

        mean = (float_score_one + float_score_two) / 2

        if mean < 5:
            print('Failed.')
            print(f'score: {mean}')
            break
        elif 5 < mean < 7:
            print('Recovery.')
            print(f'score: {mean}')
            break
        elif mean > 7:
            print('Passed')
            print(f'score: {mean}')
            break

    except ValueError:
        print('Unacceptable information.')

print('End')