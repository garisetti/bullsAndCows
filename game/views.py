from django.shortcuts import render, redirect
from .utils import get_secret_word, calculate_bulls_and_cows

def index(request):
    if 'secret_word' not in request.session:
        request.session['secret_word'] = get_secret_word()
        request.session['attempts'] = 0
        request.session['history'] = []
        request.session['game_over'] = False
        request.session['message'] = "Start guessing!"

    context = {
        'history': request.session.get('history', []),
        'message': request.session.get('message', ""),
        'game_over': request.session.get('game_over', False),
        'attempts': request.session.get('attempts', 0),
    }
    return render(request, 'game/index.html', context)

def guess(request):
    if request.method == 'POST':
        user_guess = request.POST.get('guess', '').upper().strip()
        secret_word = request.session.get('secret_word')
        
        if not secret_word:
             return redirect('index')

        if len(user_guess) != 4 or not user_guess.isalpha():
            request.session['message'] = "Please enter a valid 4-letter word."
            return redirect('index')
            
        # Check for duplicates in history (optional, but good UX)
        history = request.session.get('history', [])
        for entry in history:
            if entry['guess'] == user_guess:
                request.session['message'] = "You already guessed that word!"
                return redirect('index')

        bulls, cows = calculate_bulls_and_cows(secret_word, user_guess)
        
        request.session['attempts'] += 1
        history.insert(0, {'guess': user_guess, 'bulls': bulls, 'cows': cows})
        request.session['history'] = history
        
        if bulls == 4:
            request.session['game_over'] = True
            request.session['message'] = f"Congratulations! You guessed the word '{secret_word}' in {request.session['attempts']} attempts."
        else:
            request.session['message'] = f"Guess: {user_guess} | Bulls: {bulls}, Cows: {cows}"
            
        request.session.modified = True
        
    return redirect('index')

def reset(request):
    request.session.flush()
    return redirect('index')
