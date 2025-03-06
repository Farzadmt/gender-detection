import cv2
import json
import os
from flask import Flask, request, jsonify
from deepface import DeepFace

app = Flask(__name__)

# مسیر ذخیره عکس‌ها
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/detect-gender', methods=['POST'])
def detect_gender():
    if 'image' not in request.files:
        return jsonify({"status": "error", "message": "No image provided"}), 400

    image_file = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, "captured_face.jpg")
    image_file.save(image_path)

    response = {}

    try:
        result = DeepFace.analyze(image_path, actions=['gender'])
        gender = result[0]['dominant_gender']

        response = {
            "status": "success",
            "gender": gender,
            "raw_data": result
        }
    except Exception as e:
        response = {
            "status": "error",
            "message": str(e)
        }

    # تبدیل خروجی به JSON و ارسال آن
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
