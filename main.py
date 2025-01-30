import cv2
import torch

# โหลดโมเดล YOLOv5 ที่ใช้ในการตรวจจับ
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # ใช้โมเดล yolov5s ขนาดเล็กสุด

# เปิดการใช้งาน webcam
cap = cv2.VideoCapture(0)

while True:
    # อ่านภาพจาก webcam
    ret, frame = cap.read()
    if not ret:
        print("ไม่สามารถเปิด webcam")
        break

    # ใช้ YOLOv5 ตรวจจับผลไม้ในภาพ
    results = model(frame)

    # แสดงผลการตรวจจับในภาพ
    results.render()  # การวาดกรอบผลไม้
    cv2.imshow('ผลไม้ที่ตรวจจับ', frame)  # แสดงภาพที่ตรวจจับ

    # ออกจากโปรแกรมเมื่อกดปุ่ม 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิด webcam และหน้าต่างการแสดงผล
cap.release()
cv2.destroyAllWindows()
