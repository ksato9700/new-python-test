def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the Internet"


def test_http_error():
    assert http_error(400) == "Bad request"
    assert http_error(404) == "Not found"
    assert http_error(418) == "I'm a teapot"
    assert http_error(401) == "Something's wrong with the Internet"
