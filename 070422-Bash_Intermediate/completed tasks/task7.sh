#!/bin/bash

read -p "Enter a string" string1
read -p "Enter the same string" string2

if [[ ${string1} == ${string2} ]]
then
    echo "Strings match!"
else
    echo "Strings don't match!"
fi