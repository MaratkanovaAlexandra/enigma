import inquirer
from enigma import process

def colored(text):
  return '{red}{message}{endcolor}'.format(red='\033[31m', endcolor='\033[0m', message= text)

def validateRotorStart(position, rotor):
  if position > 26 or position < 1:
    exit(colored(rotor.capitalize() + ' rotor start position must be in 1-26'))
  else: 
    return position


print('Hello. I am Enigma machine')

question = [ inquirer.List('action',
  message='Select an option',
  choices=[('Encrypt string', '1'),('Decrypt string', '2')],
  ),
]

answers = inquirer.prompt(question)
action = answers['action']

frtRtrStart = validateRotorStart(int(input('Set first rotor start position (1-26):')), 'first')
sndRtrStart = validateRotorStart(int(input('Set second rotor start position (1-26):')), 'second')
trdRtrStart = validateRotorStart(int(input('Set third rotor start position (1-26):')), 'third')
print()

inputString = input('Your text:')

result = process(frtRtrStart, sndRtrStart, trdRtrStart, inputString, action)
print('Result: ' + result)
