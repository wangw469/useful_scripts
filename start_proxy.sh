service haproxy restart
kill $(pgrep ss-redir)
kill $(pgrep dingo)
/usr/local/bin/ss-redir -c /etc/config/shadowsocks.json -f /var/run/shadowsocks.pid
/usr/local/bin/ss-redir -c /etc/config/shadowsocks.json -f /var/run/shadowsocks2.pid
screen -dmS dingo /usr/local/bin/dingo -bind 127.0.0.1 -port 5555 -gdns:workers 50
