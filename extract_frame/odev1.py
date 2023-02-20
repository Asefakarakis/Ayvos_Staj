import os
import cv2

videos_folder = "path_to_videos_folder"
frame_save_frequency = 1

for video_name in os.listdir(videos_folder):
    if video_name.endswith(".mp4"):
        video_path = os.path.join(videos_folder, video_name)
        cap = cv2.VideoCapture(video_path)
        save_folder_name = f"{video_name[:-4]}_frames"
        frame_count = 0
        print(f"Saving frames from {video_name}...")
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                if frame_count % frame_save_frequency == 0:
                    if not os.path.exists(save_folder_name):
                        os.makedirs(save_folder_name)
                    frame_name = f"{video_name[:-4]}_{frame_count}.jpg"
                    cv2.imwrite(os.path.join(save_folder_name, frame_name), frame)
                frame_count += 1
            else:
                break
        cap.release()
        frame_save_frequency += 1