#!/bin/bash
ln -sf $(dirname $(readlink -f "$0"))"/select_current_paragraph.py" ~/.config/sublime-text-3/Packages/User/select_current_paragraph.py
