#!/bin/sh

if [ -z "$1" -o $# -ne 1 ]; then
  echo "Usage: $0 <bzr-revision>"
  exit 2
fi

rev="$1"
url=http://bzr.debian.org/bzr/bash-completion/current

bzr export -r $rev bash-completion-$(date +%Y%m%d)bzr$rev.tar.bz2 $url
