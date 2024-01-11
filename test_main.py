import main


def test_run_auction_one_person(capfd, monkeypatch):
    inputs = ["Jill", "10", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.run_auction()
    out, err = capfd.readouterr()
    assert "The winner of the bid is Jill with a bid of $10\n" in out


def test_run_auction_many_bidders(capfd, monkeypatch):
    inputs = ["Jill", "10", "yes", "Bob", "100", "yes", "Alice", "50", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.run_auction()
    out, err = capfd.readouterr()
    assert "The winner of the bid is Bob with a bid of $100" in out


def test_run_auction_negative_and_zero_bid(capfd, monkeypatch):
    inputs = ["Jill", "-10", "0", "200", "yes", "Bob", "100", "yes", "Alice", "50", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.run_auction()
    out, err = capfd.readouterr()
    assert "Bids smaller or equal to zero are not allowed." in out
    assert "The winner of the bid is Jill with a bid of $200" in out


def test_run_auction_same_bid_price(capfd, monkeypatch):
    inputs = ["Jill", "200", "yes", "Bob", "200", "yes", "Alice", "50", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.run_auction()
    out, err = capfd.readouterr()
    assert "The winner of the bid is Jill with a bid of $200" in out

def test_run_auction_bad_bid_price(capfd, monkeypatch):
    inputs = ["Jill", "10.5", "10", "yes", "Bob", "200", "yes", "Alice", "50", "no"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    main.run_auction()
    out, err = capfd.readouterr()
    assert "The winner of the bid is Bob with a bid of $200" in out