import tempfile

import pytest

from FeedFilesControl.settings import base as settings


@pytest.fixture(scope='session', autouse=True)
def set_media_temp_folder():
    with tempfile.TemporaryDirectory() as temp_dir:
        settings.MEDIA_ROOT = temp_dir
        yield