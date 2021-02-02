# A Web Application for Label Detection using Google Cloud Vision - Checky

Created a Flask  Web Application that allows users to upload an image, and our Artificial Intelligence extracts labels from that image.

This project was created as a submission to the #Challenge 1 of Citi Tech Hackathon 2021. 



# Technologies used:

- HTML
- CSS
- Flask
- Python
- Pytesseract OCR
- Keras OCR
- Google Cloud Vision API
- Google Colab

# How to Run:

Firstly, get your free credits at Google Cloud Console here: https://console.cloud.google.com/  and generate a service account key.

```shell
cd Citibank_Hackathon-main
```
then put your Service Account token file in this folder. Change the name from service.json to the filename of your token.

```shell
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="service.json"
```

Run the following statements:

```shell
export export FLASK_APP=vision.py
```
```shell
flask run
```

