import cv2

# 视频文件路径
video_path = r"C:\Users\29294\Downloads\ch1-2023-03-03 17-59-43-MP4.mp4"

# 创建VideoCapture对象
cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

frame_count = 0
# 逐帧读取视频
while True:
    # 读取下一帧
    ret, frame = cap.read()

    # 如果正确读取帧，ret为True
    if not ret:
        print("Reached end of video or cannot retrieve frame.")
        break

    # 每读取10帧，保存当前帧
    if frame_count % 10 == 0:
        # 保存帧为图片
        frame_filename = f'frame_{frame_count // 10}.jpg'
        cv2.imwrite(frame_filename, frame)
        print(f'Saved {frame_filename}')

    frame_count += 1

# 释放VideoCapture对象
cap.release()
print("Finished processing video.")
