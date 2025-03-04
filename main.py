import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw =  mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS,
                                   mp_draw.DrawingSpec((255,0,0),5,2),
                                   mp_draw.DrawingSpec((0,0,255),2,2)
                                   )



    cv2.imshow("Hand Tracking ", img)
    cv2.waitKey(1)


