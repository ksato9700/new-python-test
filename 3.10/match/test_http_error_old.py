def http_error(status):
    error_string = {
        400: "Bad request",
        404: "Not found",
        418: "I'm a teapot",
    }
    return error_string.get(status, "Something's wrong with the Internet")


def test_http_error():
    assert http_error(400) == "Bad request"
    assert http_error(404) == "Not found"
    assert http_error(418) == "I'm a teapot"
    assert http_error(401) == "Something's wrong with the Internet"
