import os
from PIL import Image
import face_recognition
import json

class Fileoperation(object): 
    def __init__(self):
      path1=[]
      os.chdir("/home/manu/facerecognition/facedetect/photos/002/0655/0655.001")
      for root, dirs, files in os.walk(".", topdown = False):
          for file_ in files:
            path1.append(os.path.join(root, file_))
          for name in path1:
              print(name)
              self.image = face_recognition.load_image_file(name)
              self.im = Image.open(name)
              self.head,self.tail=os.path.split(name)
              width, height = self.im.size
              self.h=height
              self.w=width

class Detect(Fileoperation):
    def __init__(self,file_op):
      self.image = file_op.image
      self.tail = file_op.tail
      self.h = file_op.h
      self.w = file_op.w
      face_locations = face_recognition.face_locations(self.image)
      num_faces=len(face_locations)
      facelist=[]
      id=0
      for face_location in face_locations:
          id=id+1
          face_id=str(id)+"_"+self.tail
          top, right, bottom, left = face_location
          tp=top/self.h*100 
          lf=left/self.w*100
          bm=bottom/self.h*100
          ri=right/self.w*100
          facelist.append(face_id)
          facelist.append(tp)
          facelist.append(lf)
          facelist.append(bm)
          facelist.append(ri)
          lenn=len(facelist)
      facelistlen=len(facelist)
      names=[]
      names=["id","top","left","bottom","right"]*facelistlen
      dictionary=[]
      dictionary=list(zip(facelist,names))  
      fh = open("face.json", "a+")
      fh.write(json.dumps({
          "image_id":self.tail,
          "num_faces": num_faces, 
          "faces":dictionary}))
      fh.close()
fileObject1=Fileoperation()
detectObject2=Detect(fileObject1)
