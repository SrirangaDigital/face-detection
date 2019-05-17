import os
from PIL import Image
import face_recognition

path1=[]
def pywalker(path):
    global path1
    for root, dirs, files in os.walk(path):
        for file_ in files:
            path1.append(os.path.join(root, file_))
    for name1 in path1:
        print(name1)
        image = face_recognition.load_image_file(name1)

        face_locations = face_recognition.face_locations(image)

        print("Found {} face(s) in this photograph.".format(len(face_locations)))

if __name__ == '__main__':
    pywalker('/home/manu/facerecognition/test/photos/002/0655')
