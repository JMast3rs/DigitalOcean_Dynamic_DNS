
#Domain Example home.example.com

TIME=$(date +%Y-%m-%d_%H-%M-%S)
token="Digital Ocean API token"
domain="example.com"
subdomain="home"

ip=$(curl --silent ipinfo.io/ip)
record_id=$(curl --silent --request GET --header "Content-Type: application/json" --header "Authorization: Bearer $token" "https://api.digitalocean.com/v2/domains/$domain/records" | jq ".[] | . [] | select(.name==\"${subdomain}\")" 2>/dev/null | grep "id" | sed --regexp-extended "s/[^0-9]//g")
curl --silent -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer $token" -d '{"data":"'$ip'"}' "https://api.digitalocean.com/v2/domains/$domain/records/$record_id" > /dev/null;
echo -e "\n==DNS updated with IP: $ip=="
echo "IP updated with $ip @ $TIME" >> DNSlog.txt