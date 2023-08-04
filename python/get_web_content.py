import requests
from bs4 import BeautifulSoup

def get_first_word_from_website(domain):
    url = "https://www.%s.com/" % domain
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response is not successful
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

if __name__ == "__main__":
    website_url = input("Enter the domain: ")
    first_word = get_first_word_from_website(website_url)
    if first_word:
        print("The first word on the website is:", first_word)
    else:
        print("Failed to fetch the first word from the website.")