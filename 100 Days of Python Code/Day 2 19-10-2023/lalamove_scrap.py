import requests
from bs4 import BeautifulSoup

# Make a request to the website URL
response = requests.get("https://web.lalamove.com")

# Parse the HTML response
soup = BeautifulSoup(response.content, "html.parser")

# Extract the source code of the website
source_code = soup.prettify()

# Save the source code to a file
with open("source_code.html", "w") as f:
    f.write(source_code)

# Print the source code to the console
print(source_code)