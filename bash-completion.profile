# check for bash
[ -z "$BASH_VERSION" ] && return

# check for correct version of bash
bash=${BASH_VERSION%.*}; bmajor=${bash%.*}; bminor=${bash#*.}
if [ -r /etc/bash_completion ] && \
   [ $bmajor -eq 2 -a $bminor '>' 04 -o $bmajor -gt 2 ] ; then
    # source completion code
    . /etc/bash_completion
fi
unset bash bminor bmajor
