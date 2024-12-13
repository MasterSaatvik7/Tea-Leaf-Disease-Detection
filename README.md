Here is the professional version of your project README:

---

# Tea-Leaf-Disease-Detection

This repository contains a Convolutional Neural Network (CNN) model for detecting tea leaf diseases. The model was developed in Python 3.10.12 and was initially implemented on Google Colaboratory. To avoid dimension errors, it is recommended to use Python 3.10.12 or higher.

The model is built with **TensorFlow 2.14.0**, which is compatible with the version available in Google Colaboratory.

## How to Run the Web Application

1. Ensure that the following files and directories are in the same location:
   - `static/` directory
   - `templates/` directory
   - `app.py`
   - `CNN_Tea_Leaf_Disease_Detection.pkl` file

2. Open a terminal in the directory containing the files and execute the following command:

   ```bash
   python3.10 app.py
   ```

This will start the web application, which utilizes the trained CNN model for tea leaf disease detection.

## Kaggle Dataset Used for Training

The model is trained on the dataset available on Kaggle:  
[Identifying Disease in Tea Leafs](https://www.kaggle.com/datasets/shashwatwork/identifying-disease-in-tea-leafs)

## How to Import Kaggle Dataset in Google Colab

1. Sign in to your Kaggle account.
2. Navigate to **Profile** -> **Account**.
3. Under the **API** section, click on **Create New Token** to generate a new API key.

Once you have the API key:

1. Open Google Colab and upload the `kaggle.json` file (API token).
2. Use the following commands to import the Kaggle dataset into Google Colab:

   ```bash
   !pip install -q kaggle  # Install the Kaggle API
   !mkdir ~/.kaggle  # Create a directory for the Kaggle API token
   !cp kaggle.json ~/.kaggle  # Copy the API token into the directory
   !kaggle datasets download -d shashwatwork/identifying-disease-in-tea-leafs  # Download the dataset
   ```

### To Use Any Other Kaggle Dataset

1. Go to the respective dataset on Kaggle.
2. Click on the menu (three vertical dots) and select **Copy API Command**.
3. Use the following command to download the dataset:

   ```bash
   !kaggle datasets download -d <dataset-path>
   ```

4. After downloading, unzip the dataset using the following command:

   ```bash
   !unzip /content/<dataset-name>.zip
   ```

---
