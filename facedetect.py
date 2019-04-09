import os
from PIL import Image
import face_recognition
import json

class Fileoperation(object): 
    def __init__(self):
      os.chdir("/home/manu/Desktop/photos/002/0655/0655.001")
      for root, dirs, files in os.walk(".", topdown = False):
          for name in files:
              print(os.path.join(name))
              self.image = face_recognition.load_image_file(name)
              self.im = Image.open(name)
              self.head,self.tail=os.path.split(name)
              width, height = self.im.size
              self.h=height
              self.w=width
              print("Image size in px = ", self.w,"*",self.h)   

class Detect(Fileoperation):
    def __init__(self,file_op):
      self.image = file_op.image
      self.tail = file_op.tail
      self.h = file_op.h
      self.w = file_op.w
      face_locations = face_recognition.face_locations(self.image)
      print("Found {} face(s) in this image.".format(len(face_locations)))
      fh = open("face.json", "a+")
      num_faces=len(face_locations)
      fh = open("face.json", "a+")
      num_faces=len(face_locations)
      fh.write(json.dumps({"image_id":self.tail, "num_faces": num_faces }))
      id=0
      for face_location in face_locations:
          id=id+1
          face_id=str(id)+"_"+self.tail
          top, right, bottom, left = face_location
          tp=top/self.h*100 
          lf=left/self.w*100
          bm=bottom/self.h*100
          ri=right/self.w*100
          print("A face is located at location Top: {}%, Left: {}%, Bottom: {}%, Right: {}%".format(tp, lf, bm, ri))
          fh = open("face.json", "a+")
          fh.write(json.dumps({
          "face_id":face_id,
          "top%": tp,
          "left%": lf,
          "bottom%":bm,
          "right%":ri
          }))
          fh.close()
fileObject1=Fileoperation()
detectObject2=Detect(fileObject1)