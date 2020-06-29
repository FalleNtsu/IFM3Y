# Randomly choose a Mood

import random
General_Mood = ['Happy', 'Sad', 'Excellent','Meh', 'Angry']

def get_mood():
    g_mood = random.choice(General_Mood) 
    return g_mood

