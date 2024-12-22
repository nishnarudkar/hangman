import random
import hangman_words
import hangman_art
import streamlit as st

if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = random.choice(hangman_words.word_list)
    st.session_state.lives = 6
    st.session_state.correct_letters = []
    st.session_state.display = "_" * len(st.session_state.chosen_word)
    st.session_state.game_over = False

st.title("Hangman Game")
st.code(hangman_art.logo, language="plaintext")

st.write(f"Word to guess: {st.session_state.display}")
st.write(f"Lives left: {st.session_state.lives}/6")
st.code(hangman_art.stages[st.session_state.lives], language="plaintext")

guess = st.text_input("Guess a letter").lower()

if st.button("Submit Guess") and not st.session_state.game_over:
    if len(guess) != 1 or not guess.isalpha():
        st.warning("Please enter a valid single letter.")
    elif guess in st.session_state.correct_letters:
        st.warning(f"You've already guessed the letter: {guess}")
    else:
        new_display = list(st.session_state.display)
        if guess in st.session_state.chosen_word:
            for index, letter in enumerate(st.session_state.chosen_word):
                if letter == guess:
                    new_display[index] = guess
            st.session_state.display = "".join(new_display)
            st.session_state.correct_letters.append(guess)
        else:
            st.session_state.lives -= 1

        if "_" not in st.session_state.display:
            st.session_state.game_over = True
            st.success("Congratulations! You've guessed the word!")
        elif st.session_state.lives == 0:
            st.session_state.game_over = True
            st.error(f"Game Over! The word was: {st.session_state.chosen_word}")

st.write(f"Word to guess: {st.session_state.display}")
st.write(f"Lives left: {st.session_state.lives}/6")
st.code(hangman_art.stages[st.session_state.lives], language="plaintext")
