class RecordStarter:
    cascadeClassifiers = []
        
    def LoadCascadeClassifier(this, cascadeClassifierPath):
        cascadeClassifiers.append(cv2.CascadeClassifier(cascadeClassifierPath))

    def Detect(this, grayScaleFrame)
        detections = []

        for cascadeClassifier in cascadeClassifiers:
            detect = cascadeClassifier.detectMultiScale(grayScaleFrame, scaleFactor=1.1, minNeighbors=5, minSize(60,60), flags=cv2.CASCADE_SCALE_IMAGE)
            detections.append(detect)

        return detections


