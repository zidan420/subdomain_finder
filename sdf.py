import requests
import argparse
from threading import Thread

# subdomain_finder.py -t hey.com -w ../dir_wordlist.txt

def find_subdomain(url):
	try:
		response = requests.get("http://" + url)
		if response:
				print(f"[***] Discovered subdomain --> {url}")
	except requests.exceptions.ConnectionError:
		pass

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--target', help = 'Specify the target')
	parser.add_argument('-w', '--wordlist', help = 'Specify the Wordlist File')
	args = parser.parse_args()
	target_url = args.target
	wordlist_file = args.wordlist

	if target_url == None or wordlist_file == None:
		parser.print_help()
		exit()

	with open(wordlist_file) as wordlist_file:
		for line in wordlist_file:
			word = line.rstrip("\n")
			test_url = f"{word}.{target_url}"
			t = Thread(target=find_subdomain, args=(test_url,))
			t.start()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit()