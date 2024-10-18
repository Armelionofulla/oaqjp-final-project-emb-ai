from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        #Test Joy
        result_joy = emotion_detector("I am glad this happened")
        self.assertEqual(result_joy['dominant_emotion'], 'joy')
        #Test Anger
        result_anger = emotion_detector("I am really mad about this")
        self.assertEqual(result_anger['dominant_emotion'], 'anger')
        #Test Disgust
        result_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_disgust['dominant_emotion'], 'disgust')
        #Test Fear
        result_fear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_fear['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()