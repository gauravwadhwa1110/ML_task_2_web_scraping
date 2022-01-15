Python script to scrape an article given the url of the article and store the extracted text in a file

Import Required Libraries
"""

import os
import requests
import re
from bs4 import BeautifulSoup

"""Creating function to get HTML Source Tet of the URL"""

def get_page():
	global url

	url = input("Enter url of a medium article: ")
	print(url)
 	
	# handling possible error
	if not re.match(r'https?://medium.com/',url):
		print('Please enter a valid website, or make sure it is a medium article')
		sys.exit(1)

	# Call get method in requests object, pass url and collect it in res
	hheaders = {'User-Agent': 'Chrome/97.0.4692.71 (Official Build) (64-bit)'}
	res = requests.get(url, headers=hheaders)
	res.raise_for_status()
	soup = BeautifulSoup(res.text, 'html.parser')
	return soup

"""Creating function to remove & replace the HTML tags"""

def clean(text):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>":  "\n"}
    rep = dict((re.escape(k), v) for k, v in rep.items()) 
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    text = re.sub('\<(.*?)\>', '', text)
    return text

"""Creating function to collect clean text in a String"""

def collect_text(soup):
	text = f'url: {url}\n\n'
	para_text = soup.find_all('p')
	print(f"paragraphs text = \n {para_text}")
	for para in para_text:
		text += f"{para.text}\n\n"
	return text

"""Creating function to save file in current directory"""

def save_file(text):
	if not os.path.exists('./scraped_data'):
		os.mkdir('./scraped_data')
	name = input("enter file name :")
	print(name)
	fname = f'scraped_data/{name}.txt'
	
	with open(fname,"w") as f:
		f.write(text)

	print(f'File saved in directory {fname}')

if __name__ == '__main__':
	text = collect_text(get_page())
	save_file(text)

"""# Instructions to Run this python code
	# Give url as https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7
"""