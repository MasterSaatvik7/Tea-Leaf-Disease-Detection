# Tea-Leaf-Disease-Detection

This CNN model for Tea Leaf Disease Detection works in **Python 3.10.12**(since the model was developed in google colaboratory).

If any lower version of Python is used dimension erros will occur.

The Tensorflow version used is **tensorflow 2.14.0**(available in google colaboratory).

**How to Run the website code:**

Keep all the static directory, templates directory, app.py & CNN_Tea_Leaf_Disease_Detection.pkl file in same directory.

Open the directory in terminal and type the following command

  **python3.10 app.py**

**Kaggle Dataset used for training: https://www.kaggle.com/datasets/shashwatwork/identifying-disease-in-tea-leafs**

**How to import Kaggle Dataset in Google Colab:**

sign in to your kaggle account -> go to **"profile"** -> click on **"Account"** -> Under the heading **API** click on **"Create New Token**

open Google Colab and upload your API token(json file) and type the following commands to import the Kaggle Data using the API

!pip install -q kaggle  #installs kaggle into google colab

!mkdir ~/.kaggle  #making a kaggle directory

!cp kaggle.json ~/.kaggle  #copying our API token into the kaggle directory

!kaggle datasets download -d shashwatwork/identifying-disease-in-tea-leafs  #copy this command to pull kaggle data into colab

To use any othe dataset: Go to respective Datset in kaggle -> click on menu option( the 3 vertical dots) -> click on **"Copy API Command**

!unzip /content/identifying-disease-in-tea-leafs.zip  #unzip the kaggle data downloaded
