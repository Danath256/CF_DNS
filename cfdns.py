import os
import requests

# Function to fetch current IP address
def get_current_ip():
    try:
        response = requests.get('https://checkip.amazonaws.com/')
        if response.status_code == 200:
            return response.text.strip()
        else:
            print('Failed to fetch current IP address:', response.text)
            return None
    except Exception as e:
        print('An error occurred while fetching current IP address:', e)
        return None

# Get Cloudflare API key from environment variable
api_key = os.environ.get('CLOUDFLARE_API_KEY')
if not api_key:
    print('Cloudflare API key is not set in environment variables.')
    exit()

# Set your Zone ID
zone_id = 'your_zone_id'

# Set the DNS record details
dns_record_name = 'example.com'

# Fetch current IP address
new_ip_address = get_current_ip()
if new_ip_address:
    # Construct the API request URL
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'type': 'A',
        'name': dns_record_name,
        'content': new_ip_address
    }

    # Send the API request to update the DNS record
    response = requests.post(url, headers=headers, json=data)

    # Check the response status
    if response.status_code == 200:
        print('DNS record updated successfully!')
    else:
        print('Failed to update DNS record:', response.text)
