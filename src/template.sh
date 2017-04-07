#!/bin/bash
if [[ -z "$1" ]]; then
    echo "Usage: $0 [arguments]"
    exit 1
fi

file="$1"
if [[ -f "$file" ]]; then
    file_path="${file%/*}"
    file_name="${file##*/}"
    base_name="${file_name%.*}"
    extension="${file_name##*.}"
    if [[ "$file_path" = "$file" ]]; then
        file_path=""
    fi
    echo "File path=${file_path}"
    echo "Filename =${file_name}"
    echo "Basename =${base_name}"
    echo "Extension=${extension}"
fi

home_folder=${PWD}
folder_root="${PWD##*/}"

function get_yes_no() {
    #  $1 - prompt
    #  $2 - default response
    local ans
    while true; do
        read -n 1 -p "$1 " ans
        echo
        case "$ans" in
            [Yy] )
                return 1
                ;;
            [Nn] )
                return 0
                ;;
            * )
                if [[ "$2" =~ [Yy] ]]; then
                    return 1
                elif [[ "$2" =~ [Nn] ]]; then
                    return 0
                fi
                ;;
        esac 
        echo "Invalid response--only 'y' or 'n' is permitted"
    done
}

get_yes_no "Please answer yes or no [y/n]?"
ans="$?"
if [[ "$ans" -eq 0 ]]; then
    echo "Answer was no"
else
    echo "Answer was yes"
fi
