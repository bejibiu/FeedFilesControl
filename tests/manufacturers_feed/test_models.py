import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from FeedFilesControl.settings import base as settings
from manufacturers_feed.models import Brand, Feed


@pytest.mark.django_db
def test_create_brand_with_name():
    brand = Brand(name="bosh")
    assert brand.name == "bosh"


@pytest.mark.django_db
def test_create_feed_models(tmp_path):
    brand_ = Brand()
    brand_.save()
    feed = Feed(brand_, SimpleUploadedFile('test-bosh_file', b'example'))
    feed.save()
    print(settings.MEDIA_ROOT)
    assert feed.feed_file
