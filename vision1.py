import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision_v1 import types
from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from PIL import Image
import re
from flask_ngrok import run_with_ngrok
from flask_cors import CORS, cross_origin

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service.json"
app = Flask(__name__)
run_with_ngrok(app)
cors = CORS(app, resources={"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['UPLOAD_FOLDER'] = 'static/img'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename)
            text = {}
            text = crop_image(app.config['UPLOAD_FOLDER'], filename)
            return text

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


def crop_image(FOLDER_NAME, FILE_NAME):
    im = Image.open(os.path.join(FOLDER_NAME, FILE_NAME))
    width, height = im.size
    entire_list = []
    # For date

    if (1800 < width < 2400):
        left = 1100
        top = 130
        right = 1800
        bottom = 300
        date = im.crop((left, top, right, bottom))
        date = date.save("date.jpg")
        main_date_text = computer_vision("date.jpg")
        main_date_text = re.sub('[A-Za-z]', '', main_date_text)
        main_date_text = re.sub(' ', '', main_date_text)

    if (width > 8000):
        left = 6000
        top = 780
        right = 10000
        bottom = 1600
        date = im.crop((left, top, right, bottom))
        date = date.save("date.jpg")
        main_date_text = computer_vision("date.jpg")
        main_date_text = re.sub('[A-Za-z]', '', main_date_text)
        main_date_text = re.sub(' ', '', main_date_text)

    if (width > 3000 and width < 6000):
        left = 3000
        top = 400
        right = 5000
        bottom = 800
        date = im.crop((left, top, right, bottom))
        date = date.save("date.jpg")
        main_date_text = computer_vision("date.jpg")
        main_date_text = re.sub('[A-Za-z]', '', main_date_text)
        main_date_text = re.sub(' ', '', main_date_text)

    if (width < 1800):
        left = 700
        top = 100
        right = 1200
        bottom = 200
        date = im.crop((left, top, right, bottom))
        date = date.save("date.jpg")
        main_date_text = computer_vision("date.jpg")
        main_date_text = re.sub('[A-Za-z]', '', main_date_text)
        main_date_text = re.sub(' ', '', main_date_text)

    # for amount_in_words
    # done
    if (width < 1800):
        left = 100
        top = 240
        right = 800
        bottom = 350
        amount_in_words = im.crop((left, top, right, bottom))
        amount_in_words = amount_in_words.save("amount_in_words.jpg")
        main_amount_text = computer_vision("amount_in_words.jpg")

    # done
    if (1800 < width < 2500):
        left = 50
        top = 370
        right = 1400
        bottom = 550
        amount_in_words = im.crop((left, top, right, bottom))
        amount_in_words = amount_in_words.save("amount_in_words.jpg")
        main_amount_text = computer_vision("amount_in_words.jpg")

    # done
    if (width > 8000):
        left = 1400
        top = 2200
        right = 7600
        bottom = 3000
        amount_in_words = im.crop((left, top, right, bottom))
        amount_in_words = amount_in_words.save("amount_in_words.jpg")
        main_amount_text = computer_vision("amount_in_words.jpg")

    # done
    if (width > 3000 and width < 6000):
        left = 600
        top = 1100
        right = 3800
        bottom = 1600
        amount_in_words = im.crop((left, top, right, bottom))
        amount_in_words = amount_in_words.save("amount_in_words.jpg")
        main_amount_text = computer_vision("amount_in_words.jpg")

    # for amount in number

    if (1800 < width < 2400):
        left = 1330
        top = 250
        right = 2000
        bottom = 440
        amount_in_number = im.crop((left, top, right, bottom))
        amount_in_number = amount_in_number.save("amount_in_number.jpg")
        main_amount_number_text = computer_vision("amount_in_number.jpg")
        main_amount_number_text = re.sub('[A-Za-z]', '', main_amount_number_text)
        main_amount_number_text = re.sub(' ', '', main_amount_number_text)

    # done
    if (width > 8000):
        left = 8000
        top = 1350
        right = 10000
        bottom = 2150
        amount_in_number = im.crop((left, top, right, bottom))
        amount_in_number = amount_in_number.save("amount_in_number.jpg")
        main_amount_number_text = computer_vision("amount_in_number.jpg")
        main_amount_number_text = re.sub('[A-Za-z]', '', main_amount_number_text)
        main_amount_number_text = re.sub(' ', '', main_amount_number_text)

    # done
    if (width > 3000 and width < 6000):
        left = 1000
        top = 800
        right = 5200
        bottom = 1200
        amount_in_number = im.crop((left, top, right, bottom))
        amount_in_number = amount_in_number.save("amount_in_number.jpg")
        main_amount_number_text = computer_vision("amount_in_number.jpg")
        main_amount_number_text = re.sub('[A-Za-z]', '', main_amount_number_text)
        main_amount_number_text = re.sub(' ', '', main_amount_number_text)

    # done
    if (width < 1800):
        left = 100
        top = 200
        right = 1200
        bottom = 270
        amount_in_number = im.crop((left, top, right, bottom))
        amount_in_number = amount_in_number.save("amount_in_number.jpg")
        main_amount_number_text = computer_vision("amount_in_number.jpg")
        main_amount_number_text = re.sub('[A-Za-z]', '', main_amount_number_text)
        main_amount_number_text = re.sub(' ', '', main_amount_number_text)

    entire_dict = {}
    # entire_list.append(main_date_text)
    entire_dict['date'] = main_date_text
    # print(main_date_text)
    # entire_list.append(main_amount_text)
    entire_dict['Amount in words'] = main_amount_text
    # print(main_amount_text)
    # entire_list.append(main_amount_number_text)
    entire_dict['Amount in number'] = main_amount_number_text
    # print(main_amount_number_text)
    entire_dict['Entire text'] = computer_vision(os.path.join(app.config['UPLOAD_FOLDER'], FILE_NAME))
    # entire_list.append(computer_vision(os.path.join(app.config['UPLOAD_FOLDER'], FILE_NAME)))

    return entire_dict


def computer_vision(FILE_NAME):
    client = vision.ImageAnnotatorClient()
    with io.open((FILE_NAME), 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    count = 0
    count2 = 0
    total_confidence = 0
    response = client.document_text_detection(image=image)
    entire_text = ""

    try:
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                # print('\nBlock confidence: {}\n'.format(block.confidence))

                for paragraph in block.paragraphs:
                    para_text = ""

                    for word in paragraph.words:
                        word_text = ''.join([
                            symbol.text for symbol in word.symbols
                        ])
                        para_text = para_text + " " + word_text
                    total_confidence = total_confidence + paragraph.confidence

                    count2 += 1
                    entire_text = entire_text + para_text

                    # print('Paragraph text: {}\n'.format(para_text))

        response1 = jsonify(entire_text)
        response1.headers.add("Access-Control-Allow-Origin", "*")
        return entire_text
    except (UnicodeEncodeError):
        response1 = jsonify(entire_text)
        response1.headers.add("Access-Control-Allow-Origin", "*")

        return entire_text

    flask.run()


if __name__ == "__main__":
    app.run()