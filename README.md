# PythonTechDegree-Project3
TeamTreeHouse Python TechDegree Project 3 - Phrase Hunter Word Guessing Game

Project Overview

Create a word guessing game: "Phrase Hunter." You’ll use Python and OOP (Object-Oriented Programming) approaches to select a phrase at random, hidden from the player. A player tries to guess the phrase by inputting individual characters.

Flow of the game

Using Python, you’ll create three Python classes with specific attributes and methods. You'll create a Game class for managing the game, and a Phrase class to help with storing attributes of a phrase with specific methods to help determine how to display the phrase in the game.

Your code will choose a random phrase and use some logic you will implement to display each letter of the phrase as underscore character placeholders, _.

Each time the player guesses a letter, the program compares the letter the player has chosen with the random phrase. If the letter is in the phrase, the phrase object is updated so that it displays the chosen letters on the screen.

A player continues to select letters until they guess the phrase (and win), or make five incorrect guesses (and lose).

If the player completes the phrase before they run out of guesses, a winning screen appears. If the player guesses incorrectly five times, a losing screen appears.

A player can guess a letter only once. After they’ve guessed a letter, your programming logic will need to prevent that letter from being guessed a 2nd time.
