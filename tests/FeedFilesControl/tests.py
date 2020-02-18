from django.urls import reverse, resolve

from manufacturers_feed.views import index


def test_reverse_home_page():
    found = resolve('/')
    assert found.func == index


def test_home_page_return_needed_template(client):
    response = client.get(reverse("index"))
    assert 'manufacturers_feed/index.html' in [t.name for t in response.templates]


def test_save_post_manufactures(client, brand_bosh_post):
    response = client.post(reverse("index"), data=brand_bosh_post)
    assert brand_bosh_post["brand_name"] in response.content.decode()
