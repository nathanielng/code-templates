#!/bin/bash
if [ "$1" = "-dry_run" ]; then
    dry_run="True"
    shift
fi

if [ -z "$3" ]; then
    echo "Usage: $0 [-dry_run] [files] [search_string] [replace_string]"
    echo "  renames multiple files (specified by wildcard) using sed for search & replace"
    exit 1
fi

files=`ls -1 $1 | xargs`
for file in $files; do
    new_file=`echo $file | sed "s/$2/$3/g"`
    if [ -z "$dry_run" ]; then
        mv -i $file $new_file
    else
        echo "mv -i $file $new_file"
    fi
done

