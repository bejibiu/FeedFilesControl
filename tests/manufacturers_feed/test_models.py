import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from manufacturers_feed.models import Brand, Feed


@pytest.mark.django_db
def test_create_brand_with_name():
    brand = Brand(name="bosh")
    assert brand.name == "bosh"


@pytest.mark.django_db
def test_create_feed_models(tmp_path):
    brand_ = Brand(name="Legas")
    brand_.save()
    feed = Feed()
    feed.brand = brand_
    feed.feed_file = SimpleUploadedFile('test-bosh_file', b'example')
    feed.save()
    saved_feed = Feed.objects.all()
    assert saved_feed.count() == 1
    assert brand_.name in saved_feed.first().feed_file.path