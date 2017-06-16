#!/bin/bash

date
python cli.py -i 10.200.96.16 -p 57400 -u admin -pw sp1l4b -r get-oper --file json/get-oper-fib-vrf-default.json
date

