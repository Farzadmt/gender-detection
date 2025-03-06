import cv2
import json
from deepface import DeepFace

# باز کردن دوربین
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # نمایش تصویر در یک پنجره
    cv2.imshow("Press 's' to capture", frame)

    # فشردن 's' برای گرفتن عکس
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        image_path = "captured_face.jpg"
        cv2.imwrite(image_path, frame)
        break

# بستن دوربین و پنجره
cap.release()
cv2.destroyAllWindows()

# تحلیل تصویر برای تشخیص جنسیت
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

# تبدیل خروجی به JSON و نمایش آن
json_output = json.dumps(response, ensure_ascii=False, indent=4)
print(json_output)
