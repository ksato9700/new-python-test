def read_from_file_to_stdout(ifname):
    with open(ifname) as fp:
        print(fp.read())


def read_from_file_to_file(ifname, ofname):
    with open(ifname) as rfp:
        with open(ofname, "w") as wfp:
            wfp.write(rfp.read())


def read_from_file_to_file_new(ifname, ofname):
    with (
        open(ifname) as rfp,
        open(ofname, "w") as wfp,
    ):
        wfp.write(rfp.read())


def test_read_from_file_to_stdout(capfd):
    read_from_file_to_stdout("sample.txt")
    out, err = capfd.readouterr()
    assert out == "abc\nxyz\n\n"
    assert err == ""


def test_read_from_file_to_file(tmpdir):
    wfile = tmpdir.join("copied.txt")
    read_from_file_to_file("sample.txt", wfile.strpath)
    assert wfile.read() == "abc\nxyz\n"


def test_read_from_file_to_file_new(tmpdir):
    wfile = tmpdir.join("copied.txt")
    read_from_file_to_file_new("sample.txt", wfile.strpath)
    assert wfile.read() == "abc\nxyz\n"
