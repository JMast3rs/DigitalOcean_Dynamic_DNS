# DigitalOcean_Dynamic_DNS
This is a collection of scripts used to update an DNS record on Digital Ocean for a dynamic IP address.
These scripts can run on a Raspberry Pi or any Unix systems. 

## Python
In the python folder you will see a python script, and is designed to run on reboot and every 4 hours.

No additional libraries are needed for this script, basic python3 will work with no problem.

You will want to add a crontab so that the script will run every 4 hours.
You will type **crontab -e** in to terminal.

```
0 */4 * * * python3 /home/pi/dynamic_dns.py  #Every 4 Hours the script will run.
@reboot python3 /home/pi/dynamic_dns.py      #This will run the wait script after boot.
```


## Bash
In the bash folder there is 2 bash scripts, and is designed to run on reboot and every 4 hours.

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

