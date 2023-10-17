f = open('data.csv', 'r')

o = open('dictlist.txt', 'w')

for line in f:
    line = line.strip()
    line = line.replace('\'','')
    line = line.split(',')
    outstr = "{'firstname': '%s', 'lastname': '%s', 'email': '%s', 'phone': '%s', 'notes': '%s'}"
    firstname = line[0]
    lastname = line[1]
    email = line[2]
    phone = line[3]
    notes = ','.join(line[4:])
    o.write(outstr % (firstname, lastname, email, phone, notes))
    o.write('\n')

o.close()
f.close()
