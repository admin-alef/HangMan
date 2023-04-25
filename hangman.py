class HangMan():
    def __init__(self, name):
        self.name = name

    def playHangManGame(self, word):
        (count, limit) = 0, 5
        (letters1, letters2, guessed) = list(word), list(word), []
        display = '#' * len(word)

        while(count < limit):
            if len(letters1)==0:
                print(f"Congratulation {self.name}, you won!")
                print(f"Your guessed word was: {display}!")
                break

            guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
            while len(guess) == 0 or len(guess) > 1:
                print('Invalid input. Enter a single letter\n')
                guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()

            if guess in guessed:
                print('Oops! You already tried that guess, try again!\n')
                continue

            if guess in letters1:
                ''' [2] Comment following 3 lines and Uncomment lines 35,36,37,38 '''
                letters1.remove(guess)
                index = word.find(guess)
                display = display[:index] + guess + display[index + 1:]

                ''' [2] Solving problem with multiple letters '''
                # for pos,let in enumerate(letters2):
                #     if(let == guess):
                #         display = display[:pos] + guess + display[pos + 1:]
                #         letters1.remove(guess)

            else:
                guessed.append(guess)
                count += 1
                if(count == 1):
                    print('   _____ \n'
                         '  |       \n'
                         '  |       \n'
                         '  |       \n'
                         '  |       \n'
                         '  |       \n'
                         '  |       \n'
                         '__|__\n')
                    print(f'Wrong guess: {limit - count} guesses remaining\n')

                elif(count == 2):
                    print('   _____  \n'
                          '  |     | \n'
                          '  |       \n'
                          '  |       \n'
                          '  |       \n'
                          '  |       \n'
                          '__|__\n')
                    print(f'Wrong guess: {limit - count} guesses remaining\n')

                elif(count == 3):
                    print('   _____  \n'
                          '  |     | \n'
                          '  |     | \n'
                          '  |       \n'
                          '  |       \n'
                          '  |       \n'
                          '__|__\n')
                    print(f'Wrong guess: {limit - count} guesses remaining\n')

                elif(count == 4):
                    print('   _____  \n'
                          '  |     | \n'
                          '  |     | \n'
                          '  |     O \n'
                          '  |       \n'
                          '  |       \n'
                          '__|__\n')
                    print(f'Wrong guess: {limit - count} guesses remaining\n')

                elif(count == 5):
                    print('   _____  \n'
                          '  |     | \n'
                          '  |     | \n'
                          '  |     O \n'
                         f'  |    /|\   <--{self.name}\n'
                          '  |    / \ \n'
                          '__|__\n')
                    print('Wrong guess: You have been hanged!!!')
                    print(f'The guessed word was: {word}')