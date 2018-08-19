name = input('Enter your name: ')
print('Hello dear ',name)
q1 = input('What are you Doing?\n')
import datetime
now = datetime.datetime.now()
time = datetime.time(now.hour, now.minute, now.second)
##print(time)
new_time = str(time)
time_final = new_time.split(':')
time_hours = int(time_final[0])
# print(time_final)
# print(type(time_final))
if time_hours in range(6,10):
    bt = input('Had your Breakfast? Yes/No: ')
    if bt in ['yes','Yes','YES']:
        print('Good, Caryon with your Work!')
        print('If you\'re free ping me in WhatsApp yaar, Lets Chat!')
    else:
        print('Have yor Break fast yaar!')
        print('Don\'t do too much work!!!!')
elif time_hours in range(13,16):
    lt = input('Had your Lunch? Yes/No: ')
    if lt in ['yes','Yes','YES']:
        print('Good, Caryon with your Work!')
        print('If you\'re free ping me in WhatsApp yaar, Lets Chat!')
    else:
        print('Have yor Lunch yaar!')
        print('Don\'t do too much work!!!!')
elif time_hours in range(19,23):
    dt = input('Had your Dinner? Yes/No: ')
    if dt in ['yes','Yes','YES']:
        print('Good, Caryon with your Work!')
        print('If you\'re free ping me in WhatsApp yaar, Lets Chat!')
    else:
        print('Have yor Dinner yaar!')
        print('Don\'t do too much work!!!!')
else:
    print('I think you\'re Busy!!!')
    print('If you\'re free ping me in WhatsApp yaar, Lets Chat!')
input('Press any key to say GoodBye to Koti')
