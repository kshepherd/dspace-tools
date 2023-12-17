#!/bin/zsh

function find_and_diff() {
    local a_directory="$1"
    local b_directory="$2"

    local a_files=("${a_directory}"/**/*.java)

    for a_file_path in "${a_files[@]}"; do
        local relative_path=${a_file_path#$a_directory/}
        local b_file_path="${b_directory}/${relative_path}"

        if [ -e "$b_file_path" ]; then
            diff --unified=2 --color=always "$a_file_path" "$b_file_path"
        fi
    done
}

# Directory pairs to check
dspaceapi_directory="dspace-api"
additions_directory="dspace/modules/additions"

dspacewebapp_directory="dspace-server-webapp"
server_directory="dspace/modules/server"

find_and_diff "$dspaceapi_directory" "$additions_directory"
find_and_diff "$dspacewebapp_directory" "$server_directory"

