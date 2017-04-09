# Rsyslog-OpenDXL

## Introduction

Rsyslog is an open-source software utility used on UNIX and Unix-like computer systems for multi-threaded implementation of message logging.
It implements the basic syslog protocol, extends it with content-based filtering, rich filtering capabilities, flexible configuration options and adds features such as using TCP for transport.
McAfee Data Exchange Layer can be a communication bus where the syslog message can be forwarded for further consume of information.

![Alt text](https://cloud.githubusercontent.com/assets/24607076/24838967/0c684b54-1d4a-11e7-8a06-d43aade6f368.png "Structure")

## Requirements
#### Rsyslog comes as the default logging program in many Unix systems:

Fedora, openSUSE, Debian GNU/Linux, Ubuntu, Red Hat Enterprise Linux, SUSE Linux Enterprise Server, Solaris, FreeBSD, Gentoo, Arch Linux

#### McAfee OpenDXL

https://www.mcafee.com/us/developers/open-dxl/index.aspx

1. Python SDK Installation [link](https://opendxl.github.io/opendxl-client-python/pydoc/installation.html)
2. Certificate Files Creation [link](https://opendxl.github.io/opendxl-client-python/pydoc/certcreation.html)
3. ePO Certificate Authority (CA) Import [link](https://opendxl.github.io/opendxl-client-python/pydoc/epocaimport.html)
4. ePO Broker Certificates Export  [link](https://opendxl.github.io/opendxl-client-python/pydoc/epobrokercertsexport.html)



## Rsyslog and DXL client Setup
* tested on Debian 8.7 and ubuntu 16.04 LTS

#### Installing Rsyslog from Package

> $ sudo yum install rsyslog

or (dependig on the distro)

> $ sudo apt-get install rsyslog

#### Receiving Messages from a Remote System
Edit the /etc/rsyslog.conf file and uncomment the lines relating to the protocol module used.

```clj
# for TCP use:
module(load="imtcp") # needs to be done just once 
input(type="imtcp" port="514")
# for UDP use:
module(load="imudp") # needs to be done just once 
input(type="imudp" port="514")
```
#### copy the files 

DXL configuration file for rsyslog
> /etc/rsyslog.d/10-dxl.conf

DXL messages pubblisher
> /usr/share/rsyslog/opendxl/send-dxl.py

private key for the client
> /usr/share/rsyslog/opendxl/certs/client.key

certificate for the client
> /usr/share/rsyslog/opendxl/certs/client.crt

broker certificate
> /usr/share/rsyslog/opendxl/certs/brokercert.crt

DXL configuration file for the broker connection
> /usr/share/rsyslog/opendxl/dxl.conf

#### edit the dxl.conf
```clj
[Certs]
BrokerCertChain=certs/brokercert.crt
CertFile=certs/client.crt
PrivateKey=certs/client.key

[Brokers]
{}={};8883;
```

#### rsyslog service needs to be restarted
(ex. Debian)
> service rsyslog restart

#### an example of payload injected into the DXL:
```clj
2017-04-09 06:30:13,067 dxlclient.client - INFO - Message received for topic /events/syslog
2017-04-09 06:30:13,068 __main__ - INFO - Event Subscriber - Event received:
   Topic: /events/syslog
   Payload: {"TYPE_PAYLOAD": "syslog", "PAYLOAD": " Started OpenBSD Secure Shell server.", "SRC_HOST": "host01"}
```


