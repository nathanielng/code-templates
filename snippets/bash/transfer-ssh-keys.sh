#/usr/bin/env bash
if [ "$2" = "" ]; then
    echo "Usage: $0 [to|from] [user_id@hostname] [safe]"
    exit 1
fi

if [ "$1" = "to" ]; then
    op="to"
elif [ "$1" = "from" ]; then
    op="from"
else
    echo "Usage: $0 [to|from] [user_id@hostname] [safe]"
    exit 1
fi

server="$2"
while true; do
    read -p "Transfer ~/.ssh/id_rsa.pub ${op} ${server}? " ans
    case $ans in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer with 'y' for yes or 'n' for no.";;
    esac
done

if [ "$op" = "to" ]; then
    mkdir -p $HOME/.ssh
    chmod 700 $HOME/.ssh
    cd $HOME/.ssh
    if [ ! -e "id_rsa.pub" ]; then
        ssh-keygen -t rsa
    fi
    
    if [ "$2" = "safe" ]; then
        ssh ${server} \
            "mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
    else
        cat id_rsa.pub | ssh ${server} "cat >>  ~/.ssh/authorized_keys"
    fi
elif [ "$op" = "from" ]; then
    rsync -av ${server}:.ssh/id_rsa.pub .
    if [ -e "id_rsa.pub" ]; then
        echo "cat id_rsa.pub >> ~/.ssh/authorized_keys"
        cat id_rsa.pub >> ~/.ssh/authorized_keys
    else
        echo "Failed to copy ${server}:.ssh/id_rsa.pub"
    fi
fi
