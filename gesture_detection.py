import cv2
import mediapipe as mp
import numpy as np
import pickle
import time

camera=cv2.VideoCapture(0)   
width=640
height=320
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,width)
camera.set(cv2.CAP_PROP_FPS,30)

handsFrame=mp.solutions.hands.Hands(False,2,1,0.5,0.5)
mpDraw=mp.solutions.drawing_utils

time.sleep(3)
keyPoints=[0,4,5,9,13,17,8,12,16,20]
tolerance=7

train=int(input("enter 1 to train or 0 to load trained dataset: "))
if train==1:
    trainCnt=0
    knownGestures=[]
    gestureNames=[]
    numberGestures=int(input("enter number of gestures:"))

    for i in range(0,numberGestures):
        prompt="name of gesture"+str(i+1)+" "
        gestureName=input(prompt)
        gestureNames.append(gestureName)
    fileName=input("enter filename (press enter for default): ")
    if fileName=="":
        fileName='default'
    fileName=fileName+'.pkl'
if train==0:
    fileName=input("enter name of file to load trained dataset (press enter to load default): ")
    if fileName=="":
        fileName='default'
    fileName=fileName+'.pkl'
    with open(fileName,'rb') as f:
        gestureNames=pickle.load(f)
        knownGestures=pickle.load(f)
        


def parseLandmarks(frame):
    myHands=[]
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=handsFrame.process(frameRGB)
    if results.multi_hand_landmarks != None:
        for handLandMarks in results.multi_hand_landmarks:
            my_Singular_Hand=[]
            #mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
            for landmark in handLandMarks.landmark:
                my_Singular_Hand.append((int(landmark.x*frame.shape[1]),int(landmark.y*frame.shape[0])))
            myHands.append(my_Singular_Hand)
    return myHands

def findDistances(handData):
    distMatrix=np.zeros([len(handData),len(handData)],dtype='float')
    palmSize=((handData[0][0]-handData[9][0])**2+(handData[0][1]-handData[9][1])**2)**0.5
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            distMatrix[row][column]=(((handData[row][0]-handData[column][0])**2+(handData[row][1]-handData[column][1])**2)**0.5)/palmSize
    return distMatrix

def findError(gestureMatrix,unknownMatrix,keypoints):
    error=0
    for row in keypoints:
        for column in keypoints:
            error=error+abs(gestureMatrix[row][column]-unknownMatrix[row][column])
    #print(error)
    return error

def findGesture(unknownGesture,knownGestures,keypoints,gestureNames,tolerance):
    errorArray=[]
    for i in range(0,len(gestureNames),1):
        error=findError(knownGestures[i],unknownGesture,keypoints)
        errorArray.append(error)
    errorMin=errorArray[0]
    minIndex=0
    for j in range(0,len(errorArray)):
        if errorArray[j]<errorMin:
            errorMin=errorArray[j]
            minIndex=j
    if errorMin<tolerance:
        gesture=gestureNames[minIndex]
    if errorMin>=tolerance:
        gesture='unknown'

    return gesture


while True:
    ignore, frame=camera.read()
    hands=parseLandmarks(frame)
    if train==1:
        if hands!=[]:
            print("show ur gesture", gestureNames[trainCnt], ": press t when ready to train")
            if cv2.waitKey(1)==ord('t'):
                knownGesture=findDistances(hands[0])
                knownGestures.append(knownGesture)
                trainCnt+=1
                if trainCnt==numberGestures:
                    train=0
                    with open(fileName,'wb') as f:
                        pickle.dump(gestureNames,f)
                        pickle.dump(knownGestures,f)                    
    if train==0:
        if hands!=[]:
            unknownGesture=findDistances(hands[0])
            
            myGesture=findGesture(unknownGesture,knownGestures,keyPoints,gestureNames,tolerance)
            cv2.putText(frame,myGesture,(5,40),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),2)
    for hand in hands:
        for point in keyPoints:
            cv2.circle(frame,hand[point],8,(0,0,0),-1)
            
    cv2.imshow('window',frame)
    if cv2.waitKey(1)==ord('q'):
        break
