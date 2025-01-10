import cv2

cams = []

def create_camera(camera_id):
    """
    Initialize a webcam with the given camera_id (0 for default camera).
    """
    cap = cv2.VideoCapture(camera_id)
    if not cap.isOpened():
        raise Exception(f"Cannot open camera {camera_id}")
    cams.append(cap)

def get_image_size(camera_id):
    """
    Get the resolution of the specified camera.
    """
    cap = cams[camera_id]
    return int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

def get_video(camera_id):
    """
    Capture a frame from the specified camera.
    """
    cap = cams[camera_id]
    ret, frame = cap.read()
    if not ret:
        raise Exception("Cannot read frame from camera")
    return frame

def close_cameras():
    """
    Release all webcams.
    """
    for cam in cams:
        cam.release()

if __name__ == "__main__":
    create_camera(0)
    while True:
        img = get_video(0)
        cv2.imshow("camera", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    close_cameras()
    cv2.destroyAllWindows()
