import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'http://en.wikipedia.org/wiki/List_of_Bob_the_Builder_episodes')

#print (r.status, r.data)

file = open('List_of_Bob_the_Builder_episodes.html', 'w')

#file.write(r.data.decode('utf-8'))
file.write(r.data.decode(encoding='UTF-8'))

file.close()
