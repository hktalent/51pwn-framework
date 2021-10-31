# Usage

- **frwk_51pwn**: a cool and hackable command line program

## frwk_51pwn

It supports three modes:

 - ```verify```
 - ```attack```
 - ```shell```

You can also use ```frwk_51pwn -h``` for more details.

```
usage: frwk_51pwn [options]

optional arguments:
  -h, --help            show this help message and exit
  --version             Show program's version number and exit
  --update              Update frwk_51pwn
  -v {0,1,2,3,4,5,6}    Verbosity level: 0-6 (default 1)

Target:
  At least one of these options has to be provided to define the target(s)

  -u URL [URL ...], --url URL [URL ...]
                        Target URL (e.g. "http://www.site.com/vuln.php?id=1")
  -f URL_FILE, --file URL_FILE
                        Scan multiple targets given in a textual file
  -r POC [POC ...]      Load POC file from local or remote from seebug website
  -c CONFIGFILE         Load options from a configuration INI file

Mode:
  frwk_51pwn running mode options

  --verify              Run poc with verify mode
  --attack              Run poc with attack mode
  --shell               Run poc with shell mode

Request:
  Network request options

  --cookie COOKIE       HTTP Cookie header value
  --host HOST           HTTP Host header value
  --referer REFERER     HTTP Referer header value
  --user-agent AGENT    HTTP User-Agent header value
  --random-agent        Use randomly selected HTTP User-Agent header value
  --proxy PROXY         Use a proxy to connect to the target URL
  --proxy-cred PROXY_CRED
                        Proxy authentication credentials (name:password)
  --timeout TIMEOUT     Seconds to wait before timeout connection (default 30)
  --retry RETRY         Time out retrials times.
  --delay DELAY         Delay between two request of one thread
  --headers HEADERS     Extra headers (e.g. "key1: value1\nkey2: value2")

Account:
  Telnet404、Shodan、CEye、Fofa account options

  --login-user LOGIN_USER
                        Telnet404 login user
  --login-pass LOGIN_PASS
                        Telnet404 login password
  --shodan-token SHODAN_TOKEN
                        Shodan token
  --fofa-user FOFA_USER
                        fofa user
  --fofa-token FOFA_TOKEN
                        fofa token
  --quake-token QUAKE_TOKEN
                        quake token
  --censys-uid CENSYS_UID
                        Censys uid
  --censys-secret CENSYS_SECRET
                        Censys secret

Modules:
  Modules(Seebug、Zoomeye、CEye、Fofa、Quake Listener) options

  --dork DORK           Zoomeye dork used for search.
  --dork-zoomeye DORK_ZOOMEYE
                        Zoomeye dork used for search.
  --dork-shodan DORK_SHODAN
                        Shodan dork used for search.
  --dork-censys DORK_CENSYS
                        Censys dork used for search.
  --dork-fofa DORK_FOFA
                        Fofa dork used for search.
  --dork-quake DORK_QUAKE
                        Quake dork used for search.
  --max-page MAX_PAGE   Max page used in ZoomEye API(10 targets/Page).
  --search-type SEARCH_TYPE
                        search type used in ZoomEye API, web or host
  --vul-keyword VUL_KEYWORD
                        Seebug keyword used for search.
  --ssv-id SSVID        Seebug SSVID number for target PoC.
  --lhost CONNECT_BACK_HOST
                        Connect back host for target PoC in shell mode
  --lport CONNECT_BACK_PORT
                        Connect back port for target PoC in shell mode
  --comparison          Compare popular web search engines
  --dork-b64            Whether dork is in base64 format

Optimization:
  Optimization options

  --plugins PLUGINS     Load plugins to execute
  --pocs-path POCS_PATH
                        User defined poc scripts path
  --threads THREADS     Max number of concurrent network requests (default 1)
  --batch BATCH         Automatically choose defaut choice without asking.
  --requires            Check install_requires
  --quiet               Activate quiet mode, working without logger.
  --ppt                 Hiden sensitive information when published to the
                        network
  --pcap                use scapy capture flow
  --rule                export rules, default export reqeust and response
  --rule-req            only export request rule
  --rule-filename RULE_FILENAME
                        Specify the name of the export rule file

Poc options:
  definition options for PoC

  --options             Show all definition options

```

**-f, --file URLFILE**

Scan multiple targets given in a textual file

```
$ frwk_51pwn -r pocs/poc_example.py -f url.txt --verify
```

> Attack batch processing mode only need to replace the ```--verify``` to ``` --attack```.

**-r POCFILE**

POCFILE can be a file or Seebug SSVID. frwk_51pwn plugin can load poc codes from any where.


```
$ frwk_51pwn -r ssvid-97343 -u http://www.example.com --shell
```

**--verify**

Run poc with verify mode. PoC(s) will be only used for a vulnerability scanning.

```
$ frwk_51pwn -r pocs/poc_example.py -u http://www.example.com/ --verify
```

**--attack**

Run poc with attack mode, PoC(s) will be exploitable, and it may allow hackers/researchers break into labs.

```
$ frwk_51pwn -r pocs/poc_example.py -u http://www.example.com/ --attack
```

**--shell**

Run poc with shell mode, PoC will be exploitable, when PoC shellcode successfully executed, frwk_51pwn will drop into interactive shell.

```
$ frwk_51pwn -r pocs/poc_example.py -u http://www.example.com/ --shell
```

**--threads THREADS**

Using multiple threads, the default number of threads is 1

```
$ frwk_51pwn -r pocs/poc_example.py -f url.txt --verify --threads 10
```

**--dork DORK**

If you are a [**ZoomEye**](https://www.zoomeye.org/) user, The API is a cool and hackable interface. ex:

Search redis server with ```port:6379``` and ```redis``` keyword.


```
$ frwk_51pwn --dork 'port:6379' --vul-keyword 'redis' --max-page 2

```
**--dork-shodan DORK**

 If you are a [**Shodan**](https://www.shodan.io/) user, The API is a cool and hackable interface. ex:

 Search libssh server  with  `libssh` keyword.

 ```
 frwk_51pwn -r pocs/libssh_auth_bypass.py --dork-shodan libssh --thread 10
 ```

**--dork-fofa DORK**

 If you are a [**Fofa**](fofa) user, The API is a cool and hackable interface. ex:

 Search web server thinkphp with  `body="thinkphp"` keyword.


 ```
 $ frwk_51pwn -r pocs/check_http_status.py --dork-fofa 'body="thinkphp"' --search-type web --thread 10
 ```

**--dork-quake DORK**

 If you are a [**Quake**](quake) user, The API is a cool and hackable interface. ex:

 Search web server thinkphp with  `app:"ThinkPHP"` keyword.


 ```
 $ frwk_51pwn -r pocs/check_http_status.py --dork-quake 'app:"ThinkPHP"' --thread 10
 ```

**--dork-b64**

 In order to solve the problem of escaping, use --dork-b64 to tell the program that you are passing in base64 encoded dork.
 

```
$ frwk_51pwn --dork cG9ydDo2Mzc5 --vul-keyword 'redis' --max-page 2 --dork-b64
```

**--rule**
 Export suricate rules, default export reqeust and response and The poc directory is /pocs/.
 
 Use the --pocs-path parameter to set the directory where the poc needs to be ruled
 
```
$ frwk_51pwn --rule
```

**--rule-req**
 In some cases, we may only need the request rule, --rule-req only export request rule.

```
$ frwk_51pwn --rule-req
```

If you have good ideas, please show them on your way.

## Example

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
