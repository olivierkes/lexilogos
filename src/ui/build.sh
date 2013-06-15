#!/usr/bin/bash

for i in *.ui;
do 
    echo $i; 
    pyuic4 $i > $(basename $i .ui).py;
done


