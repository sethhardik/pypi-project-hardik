import pytest
from IPYNBrendertest.youtube import get_time_info
from IPYNBrendertest.custom_exception import InvalidURLException

good_url_data = [
    ("https://youtu.be/TrfmV-4acw8", 0),
    ("https://youtu.be/TrfmV-4acw8?t=204",204),
    ("https://youtu.be/watch?v=TrfmV-4acw8&t=24s", 24),
]

URL_id_bad_data = [
    ("https://youtu.be/TrfmV-4acw8asdasdasdasd"), #exception
    ("https://youtu.be/TrfmV-4acw8?t"), #exception
    ("https://youtu.be/watch?v=TrfmV-4acw8?t==204"), # exception
    ("https://youtu.be/watch?v==TrfmV-4acw8?t=204")
]

@pytest.mark.parametrize("URL, response", good_url_data)
def test_get_time_info(URL, response):
    assert get_time_info(URL) == response

@pytest.mark.parametrize("URL", URL_id_bad_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)