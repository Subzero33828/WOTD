#from word_of_the_day import fetch_french_words, get_word_of_the_day, send_email
from word_of_the_dayyy import fetch_french_words
from unittest.mock import patch

url = 'https://www.vistawide.com/french/top_100_french_words.htm'

@patch('requests.get')
def test_fetch_french_words(mock_get):
    # Simulate a successful response
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = "<html><body><ul><li>Bonjour</li><li>Merci</li></ul></body></html>"
    
    words = fetch_french_words(url=url)
    assert words == ["Bonjour", "Merci"]

    # Simulate a failure response
    mock_get.return_value.status_code = 404
    words = fetch_french_words(url=url)
    assert words == []

   

