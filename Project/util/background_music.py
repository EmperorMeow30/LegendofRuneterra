# Module/Imports/Libraries
import pygame
import threading
import time
import os

# Global variable for volume control (0.0 to 1.0)
music_volume = 0.5

def play_music_in_background(music_file):
    # Plays a music file in the background using a separate thread.
    global music_volume  # Access the global variable

    if not os.path.exists(music_file):
        print(f"Error: Music file not found at {music_file}")
        return

    def music_player():
        pygame.mixer.init()

        try:
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play(-1)  # -1 for looping
            pygame.mixer.music.set_volume(music_volume)  # set initial volume
        except pygame.error as e:
            print(f"Error loading or playing music: {e}")
            return

        try:
            while pygame.mixer.music.get_busy():  # Check if music is playing
                pygame.mixer.music.set_volume(music_volume)  # Update volume
                time.sleep(1)  # Prevent thread from busy looping
        except KeyboardInterrupt:
            pygame.mixer.music.stop()

    music_thread = threading.Thread(target=music_player, daemon=True)
    music_thread.start()

def set_music_volume(volume):
    # Sets the music volume.
    global music_volume

    if 0.0 <= volume <= 1.0:
        music_volume = volume
        pygame.mixer.music.set_volume(music_volume)  # Update volume immediately
        print(f"Music volume set to {music_volume}")
    else:
        print("Invalid volume. Volume must be between 0.0 and 1.0")