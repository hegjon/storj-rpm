#!/bin/sh

version="$1"
if [ -z "$version" ]; then
    echo "No version specific"
    exit 1
fi

rpmdev-bumpspec -c "Updated to version $version" -n "$version" storj.spec

git add storj.spec

git commit -m "Updated to version $version"
