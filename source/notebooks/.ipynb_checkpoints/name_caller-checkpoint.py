students = '''
Eva
Katrina
Sui Li
Anjolaoluwa
Seba
Sarah Nicole Montminy
Cristina
Martine
Harriet
Noor
Venus
Megan
Heeya
Kaitlyn
Sydney
Eduardo
Caitlin
Nutsa
'''

students = students.split()

import numpy as np

def your_turn():
    return f'What do you think {np.random.choice(students, replace = False)}'