# check for bash
[ -z "$BASH_VERSION" ] && return

# check for correct version of bash
bash=${BASH_VERSION%.*}; bmajor=${bash%.*}; bminor=${bash#*.}
if [ $bmajor -eq 2 ] && [ $bminor '>' 04 ] && [ -r /etc/bash_completion ]; then
    # source completion code
    . /etc/bash_completion
fi
unset bash bminor bmajor
