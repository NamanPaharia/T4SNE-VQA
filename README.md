# T4SNE-VQA

## Visual Question Answering
A Leap Further From Image Captioning

We present a application which will allow its user to extract details of their environment by engaging in a conversation with the smartphone. This application integrates Visual Question Answering with OCR and Speech-to-Text modules to enable its user to interact with their surroundings.

## Process
Application will give its user an option to click a photo then record a question using phone( e.g. which currency note if this, is there a zebra crossing, how many dogs are in this picture, etc) which will then be transferred to a server(users personal laptop or cloud based services) and the response deduced using this image and question will be send back to the mobile phone and then to the user using a text-to-speech module.

![1](https://user-images.githubusercontent.com/45457551/115137638-de232e80-a044-11eb-9aa0-6f40896e7210.PNG)




## Model Architechture

We use a classical model (deeper LSTM Q + norm I) which uses a two layer LSTM to encode the questions and the last hidden layer of VGGNet to encode the images. Both question and image features are transformed to a common space and fused via element-wise multiplication, which is then passed through a fully connected layer followed by a softmax layer to obtain a distribution over answers. The training dataset contains over 760K questions with around 10M answers.


![image](https://user-images.githubusercontent.com/45457551/115137685-23dff700-a045-11eb-9f17-f34a3417c797.png)



## Requirements

For installing requirements run - 
```

pip install -r requirements.txt
pipwin install PyAudio

```
Download all folders from drive link given below and place them in the main directory, download VQA_MODEL_WEIGHTS.hdf5 and place in models/VQA  
drive link: https://drive.google.com/drive/folders/1P90Z_VXlViUfncVayeWcZ0kX7igrHOHn?usp=sharing

## Usage
To call your own model pass the argument -model and name of the file. For e.g

> python train -model DeeperLSTM

To run the demo

> python demo.py -module <select a module out of vqa, ocr, speech_to_text> -enable_text_to_speech  <set True to get speech output> -image_file_name <path_to_file> -question "Question to be asked"

e.g 

> python demo.py -module vqa -image_file_name test.jpg -question "Is there a man in the picture?"

## Use cases

| Image                                              | Question                   | Top Answers (left to right) |
|----------------------------------------------------|----------------------------|-----------------------------|   
| ![3](https://user-images.githubusercontent.com/45457551/115138422-ae2a5a00-a049-11eb-95b7-a1d6dfb748d1.PNG) | Is there a zebra crossing?      | yes          |
| ![4](https://user-images.githubusercontent.com/45457551/115138466-f9446d00-a049-11eb-9858-93f831dff402.PNG) | What is the value of currency note?     | 100     |
| ![5](https://user-images.githubusercontent.com/45457551/115138478-0a8d7980-a04a-11eb-9375-40b35e965ca8.PNG) | What kind of bottle is this? | wine                     |
| ![6](https://user-images.githubusercontent.com/45457551/115138485-12e5b480-a04a-11eb-8af6-b86c03d0e38f.PNG) |How many dogs are there?     | three           |
