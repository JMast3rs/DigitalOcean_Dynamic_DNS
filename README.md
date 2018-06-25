# DigitalOcean_Dynamic_DNS
This is a bash script that I am using on a Raspberry Pi on my localnetwork so that it can act as a dynamic DNS.

You will need to install Curl & JQ.

```
sudo apt-get install curl
sudo apt-get install jq
```

You will want to add a crontab so that the script will run every 4 hours.
You will type **crontab -e** in to terminal.

```
0 */4 * * * sh /home/pi/dns.sh      #Every 4 Hours the script will run.
@reboot sh /home/pi/wait.sh         #This will run the wait script after boot.
```

