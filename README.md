# Sub-Domain-Finder
## Brief Info
It bruteforces for finding subdomains using a dictionary. If you don't have a dictionary, you may use my dictionary (wordlist.txt).

## How to install
git clone https://github.com/zidan420/subdomain_finder.git

## How to use
python3 sdf.py -t [TARGET] -w [WORDLIST]

e.g. 

python3 sdf.py -t google.com -w wordlist.txt


<b>Note:</b> You <b>MUST NOT</b>  use protocol (http:// or https://) and/or www. with target_domain.com. In short it should only be something like google.com <b>NOT</b> www.google.com
