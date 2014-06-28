
"""
usage:
    python clean_zsh_history.py [path to zsh_history]

    default: $HOME/.zsh_history
"""
__author__ = "xeno1991"

import sys
import os


if __name__ == '__main__':
    if len(sys.argv) == 1:
        home = os.environ['HOME']
        filename = home + "/.zsh_history"
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("usage: python erase_history.py [.zsh_history]")
        sys.exit(1)

    try:
        f = open(filename,"r")
    except:
        print('problem with opening %s' % filename)
        sys.exit(1)

    command_list = list()
    command_set  = set()

    wcl = 0  #count number of lines in .zsh_history
    for line in f:
        wcl += 1
        line = line.strip()
        if line not in command_set:
            if len(line) > 0:
                command_list.append(line)
                command_set.add(line)
    f.close()

    try:
        f = open(filename,"w")
    except:
        print('problem with opening %s' % filename)
        sys.exit(1)

    for line in command_list:
        f.write(line + "\n")
    f.close()

    print("cleand history: %d -> %d" % (wcl, len(command_list)))
