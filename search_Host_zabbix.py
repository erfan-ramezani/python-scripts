import requests
import pandas as pd


ZABBIX_URL = "http://x.x.x.x/zabbix/api_jsonrpc.php"
API_TOKEN = "..."


def get_headers():

    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }


def get_hosts_with_tag_fw():

    payload = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["hostid", "host", "name"],
            "selectInterfaces": ["ip"],
            "selectGroups": ["name"],
            "selectTags": ["tag", "value"],
            "filter": {
                "tags": [
                    {"tag": "FW"}
                ]
            }
        },
        "auth": API_TOKEN,
        "id": 1
    }

    response = requests.post(ZABBIX_URL, json=payload, headers=get_headers())
    response.raise_for_status()

    result = response.json().get("result", [])


    filtered_hosts = []
    for host in result:
        for tag in host.get("tags", []):
            if tag.get("tag") == "FW":
                filtered_hosts.append({
                    "Hostname": host.get("name"),
                    "IP-Address": host.get("interfaces", [{}])[0].get("ip"),
                    "Hostgroup": ", ".join([group["name"] for group in host.get("groups", [])])
                })
                break

    return filtered_hosts


def save_to_excel(data, filename="output.xlsx"):

    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    try:
        hosts = get_hosts_with_tag_fw()
        if hosts:
            save_to_excel(hosts)
        else:
            print("No hosts found with tag 'FW'.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Zabbix API: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
