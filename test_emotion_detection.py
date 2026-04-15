import unittest

from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_dominant_emotions(self):
        test_map = {
            'I am glad this happened': 'joy',
            'I am really mad about this': 'anger',
            'I feel disgusted just hearing about this': 'disgust',
            'I am so sad about this': 'sadness',
            'I am really afraid that this will happen': 'fear'
        }
        for text, emotion in test_map.items():
            #print(f'working on text {text}')
            result = emotion_detector(text)
            dominant_emotion = result['dominant_emotion']
            self.assertEqual(dominant_emotion, emotion)


if __name__ == '__main__':
    unittest.main()
