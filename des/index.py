import des
import inquirer


def colored(text):
    return '{red}{message}{endcolor}'.format(red='\033[31m', endcolor='\033[0m', message=text)


def validate(key):
    if len(key) != 4:
        exit(colored('Key must be 4 symbols long'))
    else:
        return key


print('Hello. I am DES')
question = [inquirer.List('action', message='Select an option', choices=[
                          ('Encrypt string', '1'), ('Decrypt string', '2')])]

answers = inquirer.prompt(question)
action = answers['action']

key = validate(input('Enter key (4 symbols): '))
print()


text = input('Your text:')

if action == '1':
    result = des.encrypt(text, key)
    print('key: ' + str(result[0]))
    print('code: ' + str(result[1]))

if action == 's':
    result = des.decrypt(key, text)
    print('text: ' + str(result[0]))
    print('key: ' + str(result[1]))
