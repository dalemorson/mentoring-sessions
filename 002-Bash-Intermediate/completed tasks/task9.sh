#!/bin/bash

function match(){
    if [[ $1 == $2 ]]
    then
        echo "The first argument '$1' matches the second argument '$2'"
    else
        echo "The first argument '$1' does not match the second argument '$2'"
    fi
}

match same same

match same different