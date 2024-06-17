import time
import pygame
import threading
import os

lyrics = {
    "00:13.97": ("\nIt's not fair", 0.06),
    "00:18.62": ("It's not fair", 0.06),
    "00:23.05": ("It's not fair", 0.06),
    "00:27.65": ("It's not fair", 0.06),
    "00:29.23": ("I don't wanna have to wake up from this dream", 0.06),
    "00:32.21": ("\nWhen you hold me cozy", 0.08),
    "00:35.78": ("It sweetens up my life with such bliss", 0.09),
    "00:41.30": ("When you warm me rosy....", 0.07),
    "00:44.70": ("It's like my heart is gently sun-kissed", 0.08),
    "00:49.24": ("\nYou're the one...", 0.1),
    "00:52.13": ("The setting sun I'll long for, 'til kingdom come", 0.1),
    "00:59.82": ("Please don't leave me lonely", 0.08),
    "01:03.05": ("Please don't just fade away with my stolen heart", 0.08),
    "01:09.29": ("\nYou change like the seasons", 0.07),
    "01:12.53": ("But you always feel like home somehow", 0.07),
    "01:18.34": ("Your every touch deepens", 0.07),
    "01:21.85": ("The void in my heart that's missing you....", 0.08),
    "01:29.27": ("\nIt's no fair", 0.06),
    "01:31.03": ("I don't wanna have to wake up from this daydream you're my daydream", 0.08),
    "01:38.49": ("It's no fair", 0.06),
    "01:40.16": ("I don't wanna have to wake up from this daydream you're my daydream", 0.08),
    "01:47.46": ("", 0.05)
}

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        os.system('cls')
        print("Misty Memory (Day Version)")
        time.sleep(120)
        pygame.mixer.music.fadeout(2000)

    except pygame.error:
        print("Error loading or playing the music.")


    finally:
        pygame.mixer.quit()
        pygame.quit()


def display_lyrics(lyrics):
    def convert_to_seconds(timestamp):
        minutes, seconds = map(float, timestamp.split(':'))
        return minutes * 60 + seconds

    sorted_lyrics = sorted(lyrics.items(), key=lambda x: convert_to_seconds(x[0]))

    start_time = time.time()
    for timestamp, (line, char_delay) in sorted_lyrics:
        target_time = start_time + convert_to_seconds(timestamp)
        while time.time() < target_time:
            time.sleep(0.01)
        
        
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay) 
        print() 

    end_time = start_time + convert_to_seconds(sorted_lyrics[-1][0]) + 2
    while time.time() < end_time:
        time.sleep(0.01)

music_file_path = "D:\JAREZ\File\python\Python\Misty_Memory_(Day_Version).wav"


music_thread = threading.Thread(target=play_music, args=(music_file_path,))
lyrics_thread = threading.Thread(target=display_lyrics, args=(lyrics,))

music_thread.start()
lyrics_thread.start()


music_thread.join()
lyrics_thread.join()
