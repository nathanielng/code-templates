#/usr/bin/env bash
function help() {
    echo "Usage: $0 [user_id@hostname] [remote_repo] [local_repo]"
    echo "- creates a git repo (extension .git) initialised with"
    echo "  git init --bare on a remote host"
    echo "- if a local repo is specified, the following action is performed:"
    echo "  'git remote add <host> user_id@hostname:git/<remote_repo>.git'"
    exit 1
}

if [ -z "$2" ]; then
    help
fi

server="$1"
remote_repo="$2"
dest="\$HOME/git/${remote_repo}.git"
host_address="${server#*@}"
host="${host_address%%.*}"

ssh ${server} "mkdir -p $dest && cd $dest && git init --bare"

if [ -n "$3" ]; then
    local_repo="$3"
    cd ${local_repo}
    git remote add ${host} ${server}:git/${remote_repo}.git
fi

