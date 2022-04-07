#!/bin/bash

read -p "Enter a string" string1
read -p "Enter the same string" string2

if [[ ${string1} == ${string2} ]]
then
    echo "Strings match!"
fi