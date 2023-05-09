<h1 align="center"> USniff </h1>

<div align="center">

  <p> URL Sniffer </p>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/USniff-1.0.0-red?style=for-the-badge">

</div>

## Description
Usniff is a powerful python tool for extracting 
URLs from a website.

## Installation
1. Clone the repo.
```
git clone https://github.com/im-strange/usniff
```
2. Change directory.
```
cd usniff
```
3. Change `setup.sh` mode to executable and run.
```
chmod +x setup.sh && ./setup.sh
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
| `-vF` `--false-verify` |  Bypasses certificate validation completelyh1
| `-f` `--find` |  Search in url.
| `-o` `--output-file` |  Write output into a file.
| `-V` `--version`  |      Print version.

&nbsp; 
Note :
>*Use the repository's content only for legal and ethical purposes.*
