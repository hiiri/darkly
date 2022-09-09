from bs4 import BeautifulSoup
import requests

url = 'http://10.12.179.218'
r = requests.get(url + '/.hidden/')
# r = requests.get(url + '/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/ayuprpftypqspruffmkuucjccv/README')
print(r.status_code)
print(r.text)

soup = BeautifulSoup(r.content) # If this line causes an error, run 'pip install html5lib' or install html5lib
links = soup.select('a')

# Print out the result
def get_links(url):
	# r = requests.get(url + '/.hidden/amcbevgondgcrloowluziypjdh/acbnunauucfplzmaglkvqgswwn/ayuprpftypqspruffmkuucjccv/README')
	# print(r.status_code)
	# print(r.text)

	 # If this line causes an error, run 'pip install html5lib' or install html5lib
	
	
	asd = []
	for link in links:
		r = requests.get(url + '/.hidden/' + link)
		soup = BeautifulSoup(r.content)
		links = soup.select('a')
		if (link.get_text() == 'README'):
			print("reademe")
		# print(link.get_text())
		asd.append(link.get_text())
	return asd
res = get_links(url)
# print(res)

for link in res[1:]:
	print(link)
	ress = get_links(url + '/.hidden/' + link)
	print(url + '/.hidden/' + link)
	# print('-------')
	# print(ress)
	# print('-------')
	