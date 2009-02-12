#!/bin/sh

if [ -z "$1" -o $# -ne 1 ]; then
  echo "Usage: $0 <git-revision>"
  exit 2
fi

rev="$1"
url="http://git.debian.org/?p=bash-completion/bash-completion.git;a=snapshot;h=$rev;sf=tgz"

curl "$url" > bash-completion-$(date +%Y%m%d)git${rev:0:7}.tar.gz
