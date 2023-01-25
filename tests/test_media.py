import anvil.media


class TestMediaClass:
    url = "https://upload.wikimedia.org/wikipedia/commons/d/d5/Nimrat_Kaur_graces_the_red_carpet_of_Belvedere_Studio_%2804%29.jpg"

    def test_media_class(self):
        example_text = b'Hello, world'
        file_name = 'new.txt'
        media_object = anvil.BlobMedia(content_type='text/plain', content=example_text, name=file_name)
        assert 'text/plain' == media_object.content_type
        assert example_text.decode() == media_object.get_bytes()
        assert len(example_text) == media_object.length

    def test_URLmedia(self):
        urlresponse = anvil.URLMedia(self.url)
        assert self.url == urlresponse.url
        assert 'image/jpeg' == urlresponse.content_type
        assert 119865 == urlresponse.length
        assert urlresponse.content
