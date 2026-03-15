from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 500)  # Verify fix: Hard range is 1-500

def test_parse_guess():
    # Valid guesses
    assert parse_guess("50") == (True, 50, None)
    assert parse_guess("10.5") == (True, 10, None)
    # Invalid guesses
    assert parse_guess("apple") == (False, None, "That is not a number.")
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess(None) == (False, None, "Enter a guess.")

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_update_score():
    # Win score calculation
    # points = 100 - 10 * (attempt_number + 1)
    # For attempt 0: 100 - 10 * (1) = 90
    assert update_score(0, "Win", 0) == 90
    # For attempt 5: 100 - 10 * (6) = 40
    assert update_score(100, "Win", 5) == 140
    
    # Verify fix: Consistent penalty for incorrect guesses
    assert update_score(100, "Too High", 2) == 95
    assert update_score(100, "Too High", 3) == 95
    assert update_score(100, "Too Low", 1) == 95
