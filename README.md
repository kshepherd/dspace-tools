# dspace-tools

### diffoverlay.sh

zsh script to run a unified, colour diff on `dspace-api` > `dspace/modules/additions` and `dspace-server-webapp` > `dspace/modules/server`.

This is useful when you want to remind yourself of changes made (since git diff isn't so helpful in this case) and after rebasing a branch, to look out for any changes in the base classes that you need to manually merge or otherwise deal with in your overlay code.
