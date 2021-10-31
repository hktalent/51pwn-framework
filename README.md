# frwk_51pwn
[![Tweet](https://img.shields.io/twitter/url/http/Hktalent3135773.svg?style=social)](https://twitter.com/intent/follow?screen_name=Hktalent3135773) [![Follow on Twitter](https://img.shields.io/twitter/follow/Hktalent3135773.svg?style=social&label=Follow)](https://twitter.com/intent/follow?screen_name=Hktalent3135773) [![GitHub Followers](https://img.shields.io/github/followers/hktalent.svg?style=social&label=Follow)](https://github.com/hktalent/)


## Legal Disclaimer
Usage of frwk_51pwn for attacking targets without prior mutual consent is illegal.  
frwk_51pwn is for security testing purposes only

## 法律免责声明
未经事先双方同意，使用 frwk_51pwn 攻击目标是非法的。
frwk_51pwn 仅用于安全测试目的

## Overview

frwk_51pwn is an open-sourced remote vulnerability testing and proof-of-concept development framework developed by the [**51pwn Team**](https://51pwn.com/). 
It comes with a powerful proof-of-concept engine, many powerful features for the ultimate penetration testers and security researchers.

## Features
* PoC scripts can running with `attack`,`verify`, `shell` mode in different way
* Plugin ecosystem
* Dynamic loading PoC script from any where (local file, redis, database, Seebug ...)
* Load multi-target from any where (CIDR, local file, redis, database, Zoomeye, Shodan ...)
* Results can be easily exported
* Dynamic patch and hook requests 
* Both command line tool and python package import to use
* IPV6 support
* Global HTTP/HTTPS/SOCKS proxy support
* Simple spider API for PoC script to use
* Integrate with [Seebug](https://www.seebug.org) (for load PoC from Seebug website)
* Integrate with [ZoomEye](https://www.zoomeye.org) (for load target from ZoomEye `Dork`)
* Integrate with [Shodan](https://www.shodan.io) (for load target from Shodan `Dork`)
* Integrate with [Ceye](http://ceye.io/) (for verify blind DNS and HTTP request)
* Integrate with Fofa (for load target from Fofa `Dork`)
* Friendly debug PoC scripts with IDEs
* More ...

## Screenshots

### frwk_51pwn console mode
[![asciicast](https://asciinema.org/a/219356.png)](https://asciinema.org/a/219356)

### frwk_51pwn shell mode
[![asciicast](https://asciinema.org/a/203101.png)](https://asciinema.org/a/203101)

### frwk_51pwn load PoC from Seebug 
[![asciicast](https://asciinema.org/a/207350.png)](https://asciinema.org/a/207350)

### frwk_51pwn load multi-target from ZoomEye
[![asciicast](https://asciinema.org/a/133344.png)](https://asciinema.org/a/133344)

### frwk_51pwn load multi-target from Shodan
[![asciicast](https://asciinema.org/a/207349.png)](https://asciinema.org/a/207349)

## Requirements

- Python 3.6+
- Works on Linux, Windows, Mac OSX, BSD

## Installation

The quick way:

``` bash
$ pip3 install frwk_51pwn
```

Or click [here](https://github.com/51pwn-framework/frwk_51pwn/archive/master.zip) to download the latest source zip package and extract

``` bash
$ wget https://github.com/51pwn-framework/frwk_51pwn/archive/master.zip
$ unzip master.zip
$ cd frwk_51pwn-master
$ pip3 install -r requirements.txt
```


The latest version of this software is available at: https://51pwn.com

## Documentation

Documentation is available in the [```docs```](./docs) directory.

## Usage

```
cli mode

	# basic usage, use -v to set the log level
	frwk_51pwn -u http://example.com -r example.py -v 2

	# run poc with shell mode
	frwk_51pwn -u http://example.com -r example.py -v 2 --shell

	# search for the target of redis service from ZoomEye and perform batch detection of vulnerabilities. The thread is set to 20
	frwk_51pwn -r redis.py --dork service:redis --threads 20

	# load all poc in the poc directory and save the result as html
	frwk_51pwn -u http://example.com --plugins poc_from_pocs,html_report

	# load the target from the file, and use the poc under the poc directory to scan
	frwk_51pwn -f batch.txt --plugins poc_from_pocs,html_report

	# load CIDR target
	frwk_51pwn -u 10.0.0.0/24 -r example.py --plugins target_from_cidr

	# the custom parameters `command` is implemented in ecshop poc, which can be set from command line options
	frwk_51pwn -u http://example.com -r ecshop_rce.py --attack --command "whoami"

console mode
    poc-console
```
#### test
```
$ python3 test.py
```

### How compatible pocsuite3
in your python3 code
```
import frwk_51pwn as pocsuite3
```

## How to Contribute

1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
2. Fork [the repository](https://github.com/51pwn-framework/frwk_51pwn) on GitHub to start making your changes to the **dev** branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a pull request and bug the maintainer until it gets merged and published. Make sure to add yourself to [THANKS](./docs/THANKS.md).


## Links

* [Contributors](./CONTRIBUTORS.md)
* [Change Log](./CHANGELOG.md)
* [Bug tracking](https://github.com/51pwn-framework/frwk_51pwn/issues)
* [Copyright](./COPYING)
* [frwk_51pwn](https://51pwn.com)
* [Seebug](https://www.seebug.org)
* [ZoomEye](https://www.zoomeye.org)
* [51pwn](https://51pwn.com)
