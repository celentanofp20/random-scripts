import requests
from bs4 import BeautifulSoup

def get_first_word_from_imdb_homepage():
    url = "https://www.wyzant.com/"
    
    # mimic browser user-agent
    # headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    # }

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the response is not successful
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the first word on the IMDb homepage (inside the first heading element)
        first_word = soup.find('h1').text.split()[0]
        return first_word
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

if __name__ == "__main__":
    first_word = get_first_word_from_imdb_homepage()
    if first_word:
        print("The first word on the wyzant homepage is:", first_word)
    else:
        print("Failed to fetch the first word from wyzant homepage.")
