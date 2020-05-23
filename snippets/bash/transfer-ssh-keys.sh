#/usr/bin/env bash
function help() {
    echo "Usage: $0 [to|from] [user_id@hostname] [safe]"
    echo "  Copies the following files to/from local & remote machines:"
    echo "         | id_rsa.pub        ~/.ssh/authorized_keys"
    echo "  -------|-----------------------------------------"
    echo "  'to'   | local machine  ->  remote machine"
    echo "  'from' | remote machine ->  local machine"
    echo
    echo "Notes:"
    echo "1. the 'safe' option will create remote files/folders"
    echo "   if they do not exist and set the correct permissions."
    echo "2. this script does not check whether the authorized key has already"
    echo "   been copied and therefore could create duplicates"
    exit 1
}

function get_yes_no() {
    #  $1 - prompt
    #  $2 - default response
    local ans
    while true; do
        read -n 1 -p "$1 " ans
        echo
        case "$ans" in
            [Yy] )
                return 1
                ;;
            [Nn] )
                return 0
                ;;
            * )
                if [[ "$2" =~ [Yy] ]]; then
                    return 1
                elif [[ "$2" =~ [Nn] ]]; then
                    return 0
                fi
                ;;
        esac
        echo "Invalid response--only 'y' or 'n' is permitted"
    done
}

if [ "$2" = "" ]; then
    help
fi

if [ "$1" = "to" ]; then
    op="to"
elif [ "$1" = "from" ]; then
    op="from"
else
    help
fi

server="$2"
get_yes_no "Transfer ~/.ssh/id_rsa.pub ${op} ${server}? [y/n]"
if [[ "$?" -eq 0 ]]; then
    exit
fi

if [ "$op" = "to" ]; then
    mkdir -p $HOME/.ssh
    chmod 700 $HOME/.ssh
    cd $HOME/.ssh
    if [ ! -e "id_rsa.pub" ]; then
        echo "id_rsa.pub does not exist locally and will be regenerated"
        ssh-keygen -t rsa
    fi
    
    if [ "$3" = "safe" ]; then
        ssh ${server} \
            "mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
    fi
    echo "cat id_rsa.pub | ssh ${server} \"cat >>  ~/.ssh/authorized_keys\""
    cat id_rsa.pub | ssh ${server} "cat >>  ~/.ssh/authorized_keys"
elif [ "$op" = "from" ]; then
    rsync -av ${server}:.ssh/id_rsa.pub .
    if [ -e "id_rsa.pub" ]; then
        echo "cat id_rsa.pub >> ~/.ssh/authorized_keys"
        cat id_rsa.pub >> ~/.ssh/authorized_keys
    else
        echo "Failed to copy ${server}:.ssh/id_rsa.pub"
    fi
fi
