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

# Edge case tests:

# Edge case 1: Negative number input
# parse_guess accepts -5 as a valid int, but it's outside any game range.
# check_guess should return "Too Low" — not crash.
def test_negative_number_is_too_low():
    from app import parse_guess
    ok, value, err = parse_guess("-5")
    assert ok == True, "parse_guess should accept negative numbers without crashing"
    outcome, message = check_guess(value, 50)
    assert outcome == "Too Low", f"Expected Too Low for negative guess, got: {outcome}"

# Edge case 2: Extremely large number input
# parse_guess accepts 999999 as valid. check_guess should return "Too High" — not crash.
def test_extremely_large_number_is_too_high():
    from app import parse_guess
    ok, value, err = parse_guess("999999")
    assert ok == True, "parse_guess should accept large numbers without crashing"
    outcome, message = check_guess(value, 50)
    assert outcome == "Too High", f"Expected Too High for huge guess, got: {outcome}"

# Edge case 3: Whitespace-only input
# "   " is not a valid number — parse_guess should reject it gracefully with an error message.
def test_whitespace_input_is_rejected():
    from app import parse_guess
    ok, value, err = parse_guess("   ")
    assert ok == False, "parse_guess should reject whitespace-only input"
    assert err is not None, "parse_guess should return an error message for whitespace input"
