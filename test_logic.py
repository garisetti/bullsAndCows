from game.utils import calculate_bulls_and_cows

def test_logic():
    # Test 1: Exact match
    bulls, cows = calculate_bulls_and_cows("ROAD", "ROAD")
    assert bulls == 4 and cows == 0, f"Test 1 Failed: {bulls}, {cows}"
    print("Test 1 Passed: Exact match")

    # Test 2: No match
    bulls, cows = calculate_bulls_and_cows("ROAD", "MIKE")
    assert bulls == 0 and cows == 0, f"Test 2 Failed: {bulls}, {cows}"
    print("Test 2 Passed: No match")

    # Test 3: Partial match (Bulls and Cows)
    # Secret: ROAD, Guess: DOME
    # D is in ROAD (pos 3), guess D is pos 0 -> Cow
    # O is in ROAD (pos 1), guess O is pos 1 -> Bull
    # M not in ROAD
    # E not in ROAD
    # Result: 1 Bull, 1 Cow
    bulls, cows = calculate_bulls_and_cows("ROAD", "DOME")
    assert bulls == 1 and cows == 1, f"Test 3 Failed: {bulls}, {cows}"
    print("Test 3 Passed: Partial match (1B, 1C)")

    # Test 4: All Cows
    # Secret: ROAD, Guess: DORA
    # D (0) -> R (0) No, D in ROAD? Yes -> Cow
    # O (1) -> O (1) Yes -> Bull
    # R (2) -> A (2) No, R in ROAD? Yes -> Cow
    # A (3) -> D (3) No, A in ROAD? Yes -> Cow
    # Wait, DORA vs ROAD
    # D (0) != R (0), D in ROAD? Yes. Cow.
    # O (1) == O (1). Bull.
    # R (2) != A (2), R in ROAD? Yes. Cow.
    # A (3) != D (3), A in ROAD? Yes. Cow.
    # Result: 1 Bull, 3 Cows
    bulls, cows = calculate_bulls_and_cows("ROAD", "DORA")
    assert bulls == 1 and cows == 3, f"Test 4 Failed: {bulls}, {cows}"
    print("Test 4 Passed: Mixed (1B, 3C)")

if __name__ == "__main__":
    test_logic()
