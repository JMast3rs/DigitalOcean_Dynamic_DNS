import requests, json

DIGITALOCEAN_BASE_URL = "https://api.digitalocean.com"
DIGITALOCEAN_TOKEN = ""

def getDomainRecordsList(DOMAIN_NAME):
    url = f"{DIGITALOCEAN_BASE_URL}/v2/domains/{DOMAIN_NAME}/records"

    headers = {
    "Authorization": f"Authorization: Bearer {DIGITALOCEAN_TOKEN}",
    "Content-Type": "application/json"
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()

def putDomainRecord(DOMAIN_NAME, SUB_DOMAIN_NAME, DOMAIN_RECORD_ID, IP_ADDRESS):
    url = f"{DIGITALOCEAN_BASE_URL}/v2/domains/{DOMAIN_NAME}/records/{DOMAIN_RECORD_ID}"

    headers = {
    "Authorization": f"Authorization: Bearer {DIGITALOCEAN_TOKEN}",
    "Content-Type": "application/json"
    }

    data = {"type": "A", "data": IP_ADDRESS, "name": SUB_DOMAIN_NAME}

    response = requests.request("PUT", url, headers=headers, data=json.dumps(data))

    return response.json()

def getMyIP():
    url = f"https://ifconfig.me/ip"

    headers = {
    "Content-Type": "application/json"
    }

    response = requests.request("GET", url, headers=headers)

    return response.text

def main():

        target_root_domain = "example.com"
        target_sub_domain = "dns"
        my_ip = getMyIP()

        all_domain_records = getDomainRecordsList(target_root_domain)

        for record in all_domain_records["domain_records"]:
            if record["type"] == "A" and record["name"] == target_sub_domain and not record["data"] == my_ip:
                print(putDomainRecord(target_root_domain, target_sub_domain, record["id"], my_ip))

main()
