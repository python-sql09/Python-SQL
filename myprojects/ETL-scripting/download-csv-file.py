import requests
# URL of the CSV file
url = "https://the-software-guild.s3.amazonaws.com/datascience/track1-1909/got_chars.csv"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content of the request to a file
    with open("got_chars.csv", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully!")
else:
    print("Failed to download the file. Status code:", response.status_code)