#!/bin/bash
#This script emails user, IP, hostname and today's date
emailaddress=rosenbkt@mail.uc.edu
today=9/6/2020
ip=192.168.33.193
content="User rosenbkt, IP is 192.168.33.193, on 9/6/2020, running machine type of x86_64-redhat-linux-gnu with hostname rosenbkt-centos"
mail -s "IT3038C Linux IP" $emailaddress <<< $(echo -e $content)
