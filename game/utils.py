import random

def get_secret_word():
    """
    Returns a random 4-letter isogram word.
    """
    # A small list of 4-letter isograms for demonstration
    words = [
        "ROAD", "DOME", "LUCK", "TIME", "MIND", "WOLF", "GAME", "PLAY", 
        "WORD", "LOVE", "LIFE", "HOPE", "BLUE", "PINK", "STAR", "MOON"
    ]
    return random.choice(words)

def calculate_bulls_and_cows(secret, guess):
    """
    Calculates the number of Bulls and Cows.
    
    Args:
        secret (str): The secret word.
        guess (str): The user's guess.
        
    Returns:
        tuple: (bulls, cows)
    """
    bulls = 0
    cows = 0
    
    secret = secret.upper()
    guess = guess.upper()
    
    if len(guess) != 4:
        return 0, 0 # Should be handled by validation, but safe fallback
        
    # Calculate Bulls
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
            
    # Calculate Cows
    # Cows are letters that are present in the secret word but in the wrong position.
    # Note: If a letter is a Bull, it cannot be a Cow.
    # Since we are assuming isograms (unique letters), the logic is simpler.
    # If not isograms, we'd need to track used indices.
    # For this implementation, we'll assume isograms as per standard Bulls and Cows.
    
    for i in range(4):
        if guess[i] != secret[i] and guess[i] in secret:
            cows += 1
            
    return bulls, cows
