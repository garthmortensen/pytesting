from greet import greet


def test_greet_simple(capsys):  # capture system output
    greet("world")
    captured_out, captured_err = capsys.readouterr()
    assert (
        captured_out.strip() == "hello world!"
    )  # strip to remove prints \n. Could also use 'in' keyword
