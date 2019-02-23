from googlevoice import Voice
from googlevoice.util import input
def send(number, message):
    user = 'sivaramksm@gmail.com'
    password = 'ram@2222'
    voice = Voice()
    test=voice.login(user, password)
    print(test)
    number=9908997698
    message="hi"
    voice.send_sms(number,message)
send(number=9908997698,message="hi")