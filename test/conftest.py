# conftest.py
import pytest
from responses import mock


@pytest.yield_fixture
def responses():
    """Create and start response mock."""
    rsps = mock
    rsps.start()
    yield rsps
    rsps.stop()
    rsps.reset()
