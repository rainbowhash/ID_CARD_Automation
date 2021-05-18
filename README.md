# ID Card data capture automation

<h2>Two phase of processing:</h2><br>

Text Detection and extraction<br>
Face detection and extraction<br>

<h2>Text Detection and extraction</h2>
->Character Region Awareness for Text Detection a 2019 based paper that is able to localize the text in a image and is able to also map the region of intrests to its associated texts.<br>

->Reason for choosing this architecture is because there is alot of experiments and other resources that have been performed and available that shows a proven benchmark precision of 97% on ICDAR 2013 data set.<br>

->Currently for this project iam using the pretrained model which was trained on synthetic text data set.<br>

->Future we can experiment by modifying the layers and running training on more data to make it more accurate.<br>

<h2>Face Detection and extraction</h2>
I will be using pre-trained Haar Cascade model from OpenCV and Python to detect and extract faces from the ID image.<br>

