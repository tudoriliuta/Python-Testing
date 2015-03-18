people = {
	'Alice':{
		'phone':'2341',
		'addr':'Foo drive 23',
                'rel':'Single'
		},
	'Beth':{
		'phone':'9102',
		'addr':'Etc screet 18',
                'rel':'Married'
		},
	'Cecil':{
		'phone':'3158',
		'addr':'Exter street 11',
                'rel':'Ubiquitous'
		}
	}
labels={
	'phone':'phone number',
	'addr':'address',
        'rel':'relationship status'
	}
name=input('Name: ')
request=input('Phone number (p), relationship status (r) or address (a)?')
if request=='p':key='phone'
if request=='a':key='addr'
if request=='r':key='rel'

if name in people: print ("%s's %s is %s." %(name,labels[key],people[name][key]))

if request=='r':key='rel'
total=0
store=input('How satisfied were you with the service? (from 1 to 10): ')
if request=='1'or'2'or'3'or'4'or'5'or'6'or'7'or'8'or'9'or'10': print('Thank you for your input')
else:
    print('You are fucked up')
print ('Total score is: ',store)

