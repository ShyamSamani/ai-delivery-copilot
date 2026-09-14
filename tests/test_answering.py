from copilot.answering import answer


def test_blank_question_asks_again():
    assert answer("   ") == "Please ask a question."


def test_question_is_echoed_back():
    assert "testing" in answer("Why is testing amber?")