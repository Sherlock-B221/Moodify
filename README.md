# Moodify:-

Emotion recognition and playing of custom build playlists of songs to lift up your mood.
# Table of Content :
1.[Description](#p1)

2.[Installations](#p2)

3.[Dataset](#p3)

4.[Usage](#p4)

5.[Credits](#p5)

6.[Future Plans](#p6)

<a id="p1"></a> 
# Description:

We are morons driven by our mood to make decisions whether to work or not regardless of it's necessity. So we built moodify to modify your mood as per the current occasion. Your facial expression is a consequence of your mood and therefore we shall detect your emotion and the play songs that shall rejuvinate your mood so that you could maximize your productivity.

<a id="p2"></a> 
# Installations:
-tensorflow

-keras

-imutils

-cv2

-numpy

<a id="p4"></a> 
# Dataset:
I have used [this](https://www.kaggle.com/c/3364/download-all) dataset

Download it and put the csv in fer2013/fer2013/

(-fer2013 emotion classification test accuracy: 66%)

<a id="p3"></a> 
# Usage:
Run the trainer to train your dataset by executing the command:- 
"python train_emotion_classifier.py"
in your command prompt/terminal.

After installing the above directories and reaching to the downloaded folder you would be able to run Moodify by just entering 
"python Moodify.py"
in your command prompt/terminal.

The program will create a window to display the scene capture by webcamera and a window representing the probabilities of 
detected emotions. By pressing 'q' you would be able to cature your specific mood at the given time which will automatically play
the playlist of songs relative to your mood.

# Credits
1) www.kaggle.com for dataset.
2) [Raghav Vashisht](https://github.com/dramikei) and Milind Pathak for Linux support

# Future Plans
1) Improving Accuracy
2) Converison to app
3) Auto Detecting Cameras
4) Smart homes

# Issues & Suggestions
If any issues and suggestions to me, you can create an [issue](https://github.com/Sahajpal/Moodify/issues).
Give me some stars if you like my work.
