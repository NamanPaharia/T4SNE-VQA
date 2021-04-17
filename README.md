# T4SNE-Term-Project

This is a simple Demo of Visual Question answering, OCR and Speech To Text modules


## Requirements

For installing requirements run - 
```

pip install -r requirements.txt

```
Download 2 folders from drive link given below and place them in the main directory
drive link: https://drive.google.com/drive/folders/1P90Z_VXlViUfncVayeWcZ0kX7igrHOHn?usp=sharing


## Usage
To call your own model pass the argument -model and name of the file. For e.g

> python train -model DeeperLSTM

> python demo.py -module `<one of vqa, ocr, speech_to_text>` -enable_text_to_speech `<bool>`  -image_file_name `path_to_file` -question "Question to be asked"

e.g 

> python demo.py -module vqa -image_file_name test.jpg -question "Is there a man in the picture?"

Expected Output :
095.2 %  train
00.67 %  subway
00.54 %  mcdonald's
00.38 %  bus
00.33 %  train station
