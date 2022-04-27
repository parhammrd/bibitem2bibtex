# script to search the bibitem in google scholar and make the bibtex by your cites

import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def askgoogle(browser, query):

	browser.get('https://scholar.google.com')

	inputfield = browser.find_element(By.ID, 'gs_hdr_tsi')
	inputfield.send_keys(query)

	browser.find_element(By.ID, 'gs_hdr_tsb').click()
	time.sleep(10)

	items = browser.find_elements(By.CLASS_NAME, 'gs_ri')

	for item in items:
		# print(item.find_element(By.CLASS_NAME, 'gs_rt').text)
		# print(item.find_element(By.CLASS_NAME, 'gs_a').text)
		if True:#input(':'):
			item.find_element(By.CLASS_NAME, 'gs_fl').find_element(By.CLASS_NAME, 'gs_nph').click()
			time.sleep(3)

			cites = browser.find_elements(By.CLASS_NAME, 'gs_citi')
			for ct in cites:
				if ct.text == 'BibTeX':
					lref = ct.get_attribute('href')
					break
		break

	browser.get(lref)
	return browser.find_element(By.TAG_NAME, 'pre').text

if __name__ == '__main__':

	# TARGET = input('Set your Fullname .tex file in local directory: \n')
	TARGET = 'myrefs.tex'

	with open(TARGET, 'r') as tfile:
		Sources = re.findall(r'\\bibitem{(.*?)}(.*)', tfile.read())

	print('There are ' + str(len(Sources)) + ' Bibitems')

	bs = webdriver.Chrome(executable_path='../chromedriver')
	for item in Sources:
		if (True):
			bibtex = askgoogle(bs, item[1])

		pls = re.search(r'\w{(.*?),', bibtex)

		with open('citation.bib', 'a') as wfile:
			wfile.write(bibtex[:pls.span()[0]+2]+item[0]+bibtex[pls.span()[1]-1:]+'\n')

		break
	
	# print(bibtex)

	bs.close()
