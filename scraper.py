import requests
import re

r = requests.get('http://10.12.179.218/.hidden/')

used = dict()
usedresp = dict()
def get_links(url):
	# if not (url.startswith('http')):
	# 	return
	r = requests.get(url)
	links = re.findall(r'(?<=a href=").*?(?=")', str(r.text))
	if links:
		links[0] = url
	
	
	# print(links)
	for link in links:
		# readmelink = 'http://10.12.179.218/.hidden/' + link
		readmelink = url + link
		if not link.endswith('README'):
			readmelink += 'README'
		if readmelink.count('.hidden') == 2:
			readmelink = readmelink[29:]
		# print(readmelink)
		if (readmelink not in used and readmelink.startswith('http')):
			r = requests.get(readmelink)
		else:
			continue
		# print(link, url)
		# print('http://10.12.179.218/.hidden/' + link  + 'README')
		# print(readmelink)
		used.update({readmelink: True})

		if (r.content not in usedresp):
			usedresp.update({r.content: True})
			print((r.content))
			print(readmelink)
			
		# print('http://10.12.179.218/.hidden/' + link  + 'README')

		get_links(url + link)
	return links

all_links = []
links = get_links('http://10.12.179.218/.hidden/')


# for link in links:
# 	all_links.append(get_links(link))

# 	print(all_links)


# print(all_links)
# all_links.sort()
# print(all_links)
# print(len(all_links))

# for i in range(len(all_links)):
# 	for j in range(len(all_links[i])):
# 		r = requests.get('http://10.12.179.218/.hidden/' + all_links[i][j] + 'README')
# 		if (r.status_code == 200):
# 			print(r.text)
# 		print('http://10.12.179.218/.hidden/' + all_links[i][j] + 'README')
# r = requests.get('http://10.12.179.218/.hidden/README')
# if (r.status_code == 200):
# 	print(r.text)

# print(all_links[0])

# print(all_links[2])
