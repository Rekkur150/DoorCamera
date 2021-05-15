from cv2 import VideoWriter #For VideoWriter
from datetime import datetime #For naming file

class Recorder:
    recordingFileLocation = ""
    maxStorageSpaceInMB = 1000

    currentVideoCapture = None

    def __init__(self, recordingFileLocation, maxStorageSpaceInMB):
        self.storageLocation = location
        self.maxDataSizeInMB = maxSize
    
    def Record(self):
        if currentVideoCapture is None:
            currentVideoCapture = cv2.VideoWriter(recordingFileLocation + datetime.now().strftime("%d-%m-%Y.%H:%M:%S"), -1, 20.0, (640,480))
        else:
            print("Error: Recording Already Started, Please Finish Recording before starting a new recording")

    def AddFrameToRecord(self, frame):
        if currentVideoCapture is not None:
            currentVideoCapture.write(frame)
        else:
            print("Error: Please start recording before adding frames")

    def FinishRecording(self):
        currentVideoCapture.release()
        currentVideoCapture = None

