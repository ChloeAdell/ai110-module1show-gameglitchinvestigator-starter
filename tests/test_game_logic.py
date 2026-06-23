from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Targeted tests for the swapped HIGHER/LOWER hint bug ---
# check_guess returns a tuple: (outcome, message). The OUTCOME labels are
# correct, but the MESSAGES point the player in the wrong direction.

def test_too_low_guess_hints_higher():
    # -100 is below any secret (range is 1..100), so the player must go HIGHER.
    # Buggy code currently returns "Go LOWER!" here.
    outcome, message = check_guess(-100, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()

def test_too_high_guess_hints_lower():
    # 60 is above the secret, so the player must go LOWER.
    # Buggy code currently returns "Go HIGHER!" here.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
