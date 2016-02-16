from resource import HTTPResource

def test_variable_interpolation():
    """Test if variables are properly interpolated."""

    data = {
        'uri': 'http://example.com/item/{id}/',
        'json': {
            'some_attribute': '{BUILD_ID}',
        },
    }

    values = {
        'id': '123',
        'BUILD_ID': '321',
    }

    expect = {
        'uri': 'http://example.com/item/123/',
        'json': {
            'some_attribute': '321',
        },
    }

    assert HTTPResource._interpolate(data, values) == expect
