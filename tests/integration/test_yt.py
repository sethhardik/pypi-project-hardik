import pytest
from IPYNBrendertest.youtube import render_Youtube_video
from IPYNBrendertest.custom_exception import InvalidURLException


class TestYTvideoRenderer:
    good_url_data = [
        ("https://youtu.be/TrfmV-4acw8", "success"),
        ("https://youtu.be/TrfmV-4acw8?t=204","success"),
        ("https://youtu.be/watch?v=TrfmV-4acw8&t=24s", "success"),
    ]
    
    URL_id_bad_data = [
        ("https://youtu.be/TrfmV-4acw8asdasdasdasd"), #exception
        ("https://youtu.be/TrfmV-4acw8?t"), #exception
        ("https://youtu.be/watch?v=TrfmV-4acw8?t==204"), # exception
        ("https://youtu.be/watch?v==TrfmV-4acw8?t=204")
    ]
    
    
    @pytest.mark.parametrize("URL, response", good_url_data)
    def test_render_YT_success(self, URL, response):
        assert render_Youtube_video(URL) == response
    
    @pytest.mark.parametrize("URL", URL_id_bad_data)
    def test_render_YT_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_Youtube_video(URL)