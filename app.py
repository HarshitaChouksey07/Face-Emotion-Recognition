from flask import Flask, render_template, request
import cv2
import Emotion_Detection

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/after', methods = ['GET', 'POST'])
def after():
    img = request.files['file1']
    img.save('static/file.jpg')
    img_, text = Emotion_Detection.detect('static/file.jpg')

    try :
        cv2.imwrite("static/output.jpg", img_)
    except:
        cv2.imwrite("static/output.jpg", img)


    return render_template('after.html',data = text)


if __name__ == '__main__':
    app.run(debug=True)