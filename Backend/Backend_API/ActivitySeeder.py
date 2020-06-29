# Randomly choose an activity 

import random

physical_activities = ['Walking','Jogging','Hiking','Yoga','Aerobics']
mental_activities = ['Identifying Cognitive Distortions','Cognitive Restructuring and Reframing',' Problem-Solving','Practice positive mental health']

def get_activity():
    p_activity = random.choice(physical_activities) 
    m_activity = random.choice(mental_activities)
    activity = random.choice([m_activity,p_activity])
    print(activity)
    return activity 