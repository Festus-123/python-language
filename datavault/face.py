word = input("Enter robot face build word : ")

def build_head_cap (number_space, fill_number) :
    head_cap = f'{" " * number_space} {word * fill_number}'
    print(head_cap)
    
def build_eye_line (number_space, eye_space, fill_number) :
    eye_build = f'{word * fill_number} {" " * eye_space} {word * fill_number} {" " * eye_space} {word * fill_number}'
    eye_line = f'{" " * number_space} {eye_build} '
    print(eye_line)
    
def build_nose_line (number_space, nose_space, fill_number):
    nose_build = f'{word * fill_number} {" " * nose_space} {word * fill_number}'
    nose_line = f'{" " * number_space} {nose_build}'
    print(nose_line)

def build_mouth_line (number_space, nose_space, fill_number):
    mouth_build = f'{word * fill_number} {" " * nose_space} {word * fill_number}'
    mouth_line = f'{" " * number_space} {mouth_build}'
    print(mouth_line)

for i in range(4) :
    build_head_cap((10 - i), (18 + i))

for i in range(8) :
    build_eye_line((7 ), (10), (5))

for i in range(2) :
    build_head_cap((7), (21))
    
for i in range(1) :
    build_nose_line((7), (2), (10))

for i in range(2) :
    build_head_cap((7), (21))
    
for i in range(4) :
    build_mouth_line((7), (10), (9))

for i in range(4) :
    build_head_cap((7 + i), (21 - i))
