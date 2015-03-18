people= {
    'Jacques' : {
        'age':'32',
        'phone':'2031923091',
        'addr':'Lanarkshire 33'
        },
    'Marguerietta' : {
        'age':'32',
        'phone':'2093384234',
        'addr':'Sainstburger 21'
        },
    'Simonette' : {
        'age':'22',
        'phone':'2391238218',
        'addr':'Etcetera 211'
        }
    }
    
        

labels={'phone':'phone number','addr':'address'}
name=input('Name: ')
request=input('Phone number (p) or address (a)?')
if request=='p': key='phone'
if request=='a': key='addr'

label=labels.get(key,key)

person=people.get(name,{})

result=person.get(key,'not available')


print ("%s's %s is %s." % (name,label,result))

