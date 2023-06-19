import cv2

cap = cv2.VideoCapture(2)

width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer= cv2.VideoWriter('opencv.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 20, (width,height))

while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()

  writer.write(frame)

  # 顯示圖片
  cv2.imshow('frame', frame)

  # 若按下 q 鍵則離開迴圈
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放攝影機
cap.release()
writer.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()