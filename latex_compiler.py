import fileinput

def generate_letter(text_input, job_number):
    new_text = []

    for line in fileinput.input("Awesome CV/coverletter.tex", inplace=False):
        if fileinput.filelineno()==113:
            line =f'{text_input}\n'
        print('{} {}'.format(fileinput.filelineno(), line), end='') # for Python 3
        new_text.append(line)

    with open(f'applications/letter_{job_number}.tex', 'w') as f:
        for line in new_text:
            f.write(line)