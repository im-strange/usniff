
red = "\033[0;1;31m"
blue = "\033[1;38;5;111m"
bd = "\033[0;1;40m"
orn = "\033[1;38;5;208m"
gy = "\033[0;1;2m"
gr = "\033[1;32m"
yl = "\033[1;33;40m"
n = "\x1B[0m"
ln = "\u2502"
t = "\u251C"
info = f"{bd}[{blue}INFO{bd}]{n}"
info_err = f"{bd}[{red}INFO{bd}]{n}"
warning = f"{bd}[{yl}WARNING{bd}]{n}"

import os
import argparse
import re
import time

try:
  import requests
except ModuleNotFoundError:
  print(f"{info_err} Module {orn}requests{n} not found")
  print(f"{info} Try running {orn}pip install requests{n}")
  exit(1)

try:
  import bs4
  from bs4 import BeautifulSoup
except ModuleNotFoundError:
  print(f"{info_err} Module {orn}beautifulsoup4 not found{n}")
  print(f"{info} Try running {orn}pip install beautifulsoup4{n}")
  exit(1)

def get_links(website_url, verify=True, write_result=False, output_file=None, find=False):
  fetched_urls = []
  try:
    url = website_url
    request = requests.get(url, verify=verify)
    soup = BeautifulSoup(request.text, 'html.parser')

    if find:
      new_list = []
      for link in soup.find_all("a"):
        fetched_urls.append(link.get('href'))
      for link in fetched_urls:
        matched = re.findall(find.lower(), link.lower())
        if len(matched) != 0:
          new_list.append(link)
      fetched_urls = new_list
      for link in fetched_urls:
        print(f"{info} {link}")
        time.sleep(0.1)

    else:
      for link in soup.find_all("a"):
        print(f"{info} {link.get('href')}")
        fetched_urls.append(link.get('href'))
        time.sleep(0.1)

    if write_result:
      try:
        with open(output_file, "a") as file:
          for url in fetched_urls:
            file.write(url+"\n")
          file.close()
      except FileNotFoundError:
        pass

  except requests.exceptions.SSLError as e:
    print(f"{info_err} {e}")
    time.sleep(0.1)
    print(f"\n{info} The target website needs certificate verification.")
    time.sleep(0.1)
    print(f"{info} Try {orn}-vF{n} to bypass certificate validation.")
    time.sleep(0.1)
    print(f"\n{warning} Please note that {orn}-vF{n} will cause the certificate not to be verified. This will expose your application to security risks.")

  except requests.exceptions.ConnectionError as e:
    print(f"{info_err} {e}")
    time.sleep(0.1)
    print(f"\n{info} Most likely caused by incorrect url or connection error.")

  except requests.exceptions.MissingSchema as e:
    print(f"{info_err} {e}")
    print(f"{info} There is problem in URL.")

  return fetched_urls

example = """example:
  usniff -u https://example.com
  usniff -u https://mywebsite.com -vF
  usniff -u https://unknownSite.com -o output.txt
  usniff -u https://examplesite.com -vF -o output.txt
  usniff -u https://mysite.com --find .php
"""

description = "Find all links in a web page"

parser = argparse.ArgumentParser(
	description = description,
	epilog = example,
	prog = None,
	formatter_class = argparse.RawDescriptionHelpFormatter,
        add_help = True,
        usage = None
	)

version = "USniff 1.0"

parser.add_argument("-u", "--url", help="Url of the target website.")
parser.add_argument("-vF", "--false-verify", help="Bypasses certificate validation completely.", action="store_false", dest="allow_verify")
parser.add_argument("-f", "--find", help="Search in url.", dest="find_key", action="store", nargs="?", const=False, metavar="str")
parser.add_argument("--output-file", help="Write output into a file.", action="store", dest="output_file", nargs="?", metavar="file")
parser.add_argument("-V", "--version", help="Print version.", action="version", version=version)
args = parser.parse_args()

if args.url is None:
  print(f"{info} URL must be specified.")
  print(f"{info} See 'usniff --help'")
  exit(1)

if __name__ == "__main__":
  get_links(args.url, args.allow_verify, args.output_file, args.output_file, args.find_key)
