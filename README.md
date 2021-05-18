# ID Card data capture automation using machine learning

<h2>Two phase of processing:</h2><br>

Text region of interest Detection and extraction<br>
Face region of interest detection and extraction<br>

<h2>Text Detection and extraction</h2>
<a href=https://arxiv.org/pdf/1904.01941v1.pdf>Character Region Awareness for Text Detection a 2019 based paper </a>that is able to localize the text in a image and is able to also map the region of intrests to its associated texts.<br>
Reason for choosing this architecture is because there is alot of experiments and other resources that have been performed and available that shows a proven benchmark precision of 97% on ICDAR 2013 data set.<br>
Currently for this project iam using the pretrained model which was trained on synthetic text data set.<br>
Future we can experiment by modifying the layers and running training on more data to make it more accurate.<br>

<h2>Face Detection and extraction</h2>
I will be using pre-trained Haar Cascade model from OpenCV and Python to detect and extract faces from the ID image.<br>


<h2>TO run:</h2>
Run 
```main.py --image [image_path]```
