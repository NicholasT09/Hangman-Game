Hangman Game Diary
Day 1 - Initial Setup and Game Design
Objective: The game starts with a simple idea — a Hangman game using Pygame.

Key Features:

Pygame initialization and window setup (1000x500 window).

Basic UI elements: a title and the word display.

Letters are displayed as clickable buttons on the screen.

Image-based hangman status (7 images representing stages of the hangman).

Challenges:

Deciding how to organize the word dictionary based on difficulty levels.

How to handle user input, including mouse clicks and keyboard events.

Next Steps:

Set up the game loop, handle player interactions, and update the game state accordingly.

Day 2 - User Interface and Input Handling
Objective: Focus on improving the UI for user interaction.

New Features:

Display the word with blanks for unguessed letters.

Clicking on letters updates the game state, showing whether the guess is correct or incorrect.

Implemented a "Hint" button that reveals a random letter from the word.

Implemented a "Clue" button to toggle displaying a clue for the word.

Challenges:

Making sure that letters can only be clicked once (visibility control).

Handling mouse events effectively to detect which letter the player is selecting.

The hangman images update based on incorrect guesses.

Next Steps:

Implement functionality to end the game when the word is guessed correctly or the player loses.

Day 3 - Word and Clue Management
Objective: Add word and clue management based on difficulty.

New Features:

Added a function to select random words from different difficulty levels: easy, medium, and hard.

Display a clue for each word based on the selected difficulty.

Functionality to toggle the clue’s visibility.

Challenges:

Ensuring that the words chosen fit the difficulty levels properly.

Deciding the format of the clues and how to display them.

Next Steps:

Implement a function to display the game result (win/lose).

Handle the flow of the game between starting, playing, and displaying the results.

Day 4 - Game State and End Conditions
Objective: Finalize the game state logic, including handling win/loss conditions.

New Features:

After each guess, check if the player has won by comparing guessed letters to the word.

If the player guesses all letters, display a "You WON!" message.

If the player makes 6 incorrect guesses (hangman status reaches 6), display a "You LOST!" message with the word revealed.

Added a delay after displaying the result before restarting or quitting the game.

Challenges:

Ensuring the game ends when the player either wins or loses, with no further inputs allowed.

Managing the flow of the game from one round to another (starting, playing, and displaying results).

Next Steps:

Final testing to ensure all conditions work correctly.

Polish the graphics and UI elements, ensuring smooth interactions and transitions.

Day 5 - Final Touches and Testing
Objective: Test the game thoroughly, fix any remaining bugs, and add finishing touches.

New Features:

Added smooth transitions between game states (starting the game, playing the game, and ending the game).

Fixed minor UI issues such as button positioning and text alignment.

Optimized code for better readability and organization.

Thoroughly tested different difficulty levels to ensure words are selected randomly and clues are useful.

Challenges:

Managing edge cases, like a situation where all letters are guessed or when a user presses the ESC key.

Balancing difficulty so that the game is fun but not too easy or too difficult.

Next Steps:

Finalize the code, make sure all features work seamlessly, and prepare for release.

Day 6 - Game Ready for Deployment
Objective: Ensure that the game is fully ready for release.

Changes Made:

Refined the end game screen, showing the word with a clean message for either win or loss.

Cleaned up unused variables and optimized images for performance.

Checked the game's compatibility with different screen sizes (ensuring that the game scales well).

Challenges:

Final tweaks to the overall user experience (e.g., making sure there are no distractions during gameplay).

Ensuring the game runs smoothly on lower-end devices.

Next Steps:

Publish the game and gather feedback for future updates.

Future Improvements and Ideas
Multiplayer Mode: Allow two players to take turns guessing letters.

Sound Effects: Add sound effects for correct/incorrect guesses, win/loss events, and button clicks.

Difficulty Customization: Allow the player to define custom word lists for different difficulty levels.

Leaderboard: Track player scores and display the fastest time to win or the most games won.
