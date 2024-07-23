# dspace-tools

### diffoverlay.sh

zsh script to run a unified, colour diff on `dspace-api` > `dspace/modules/additions` and `dspace-server-webapp` > `dspace/modules/server`.

This is useful when you want to remind yourself of changes made (since git diff isn't so helpful in this case) and after rebasing a branch, to look out for any changes in the base classes that you need to manually merge or otherwise deal with in your overlay code.

### json5diff.py

Requires json5 package (`pip install json5`). Compares two i18n json5 files to report keys found in 1st but not 2nd, and 2nd but not in 1st.

Only the keys are compared, and comments and blank lines are ignored. When printed to stdout, however, it will be in the form of a comment with the value included so it is easy to copy and paste into the json5 file that needs the key to be translated.

Usage example: `python json5diff.py src/assets/i18n/en.json5 src/assets/i18n/de.json5`
