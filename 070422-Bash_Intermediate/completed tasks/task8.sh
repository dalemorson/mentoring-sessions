#!/bin/bash

read -p "Enter a list of users" users

for user in ${users}
do
    echo "${user}"
done