from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# Tests targeting the high/low hint direction bug:
# The original code returned "Go HIGHER!" when guess was too high,
# and "Go LOWER!" when guess was too low — the opposite of correct.

def test_too_high_hint_says_go_lower():
    # Guess is above the secret, so the hint must tell the player to go LOWER
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected hint to say LOWER, got: {message}"

def test_too_low_hint_says_go_higher():
    # Guess is below the secret, so the hint must tell the player to go HIGHER
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say HIGHER, got: {message}"
