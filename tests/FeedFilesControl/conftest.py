import pytest
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture()
def brand_bosh_post():
    xlsx = SimpleUploadedFile("file.xlsx", b"file_content",
                              content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    return {'brand_name': 'bosh', 'feed_file': xlsx}

