# USniff (URL Sniffer)
A powerful python tool for extracting url from a website
&nbsp; 

## Installation
1. Clone the repo.
```
git clone https://github.com/im-strange/usniff
```
2. Change directory.
```
cd usniff
```
3. Change `setup.sh` mode to executable.
```
chmod +x setup.sh
```
4. Reload `.bashrc` file.
```
source ~/.bashrc
```

&nbsp; 
## Usage
```python
usniff.py [-h] [-u URL] [-vF] [-f [str]]
          [--output-file [file]] [-V]
```
&nbsp; 

## Options
| commands | description |
| --- | --- |
| `-h` `--help` |  show this help message and exit. |
| `-u` `--url`  |  Url of the target website.
| `-vF` `--false-verify` |  Bypasses certificate validation completely.
| `-f` `--find` |  Search in url.
| `-o` `--output-file` |  Write output into a file.
| `-V` `--version`  |      Print version.

&nbsp; 
<sub>Use the repository's content only for legal and ethical purposes.</sub>
