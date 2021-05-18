import OCR
import spacy
from face_detect import capture_face


class id_automation:
    def __init__(self, image_path):
        self.image_path = image_path
        self.language_model = 'en_core_web_lg'
        self.langauage = 'en'
        self.nlp = spacy.load(self.language_model)
        self.reader = OCR.Reader([self.langauage])
        self.parsed_data = None
        self.face = None

    def process_text(self):
        """
        This method calls the OCR module and finds the region of interest and convert it into words or sentences.
        The recognized words or sentence is again parsed using spacy to find named entities to extract required data.
        Returns required information.
        """
        result = self.reader.readtext(self.image_path)
        data = []
        # entity recognition
        for items in result:
            data.append(items[1])
        data = " ".join(data)
        print(data)
        doc = self.nlp(data)
        parsed_data = [(X.text, X.label_) for X in doc.ents]
        assert parsed_data is None, "OCR couldnt read any text"
        return parsed_data

    def process_face(self):
        """
        This method calls the face detection model
        returns the cropped face from the image
        """
        result = capture_face(self.image_path)
        assert result is None, "Face detection could not find any faces"
        return result

    def process(self):
        self.parsed_data = self.process_text()
        self.face = self.process_face()

    def result(self):
        return (self.parsed_data, self.face)


if __name__ == "__main__":
    automate = id_automation("id.jpeg")
    automate.process()
    data, face = automate.result()
