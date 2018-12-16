# Star expression can also be usefull when combned with certain kind of string processing operations

line = 'nobody:*:2:-2:Unpriviledged user:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print('Uname:'+uname)
print('Unusable fields', fields)
print('homedir'+homedir)
print('sh'+sh)
