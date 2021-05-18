import OCR
import spacy
from face_detect import  capture_face

nlp = spacy.load('en_core_web_lg')
reader = OCR.Reader(['en']) # need to run only once to load model into memory
result = reader.readtext('id.jpeg')
capture_face("id.jpeg")
data=[]
# entity recognition
for items in result:
  data.append(items[1])

data= " ".join(data)
print(data)
doc = nlp(data)
print([(X.text, X.label_) for X in doc.ents])
