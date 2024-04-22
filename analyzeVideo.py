import inference
import cv2 as cv
import os
from calculsMath import ang
import math


def analyzeVideo(filePath, erreur):
        try:

                model = inference.get_model(model_id="ele3000/3")

                dove = False
                water = False

                color = {'Starter': (255, 0, 0), 'Block': (0, 255, 0), 'Area': (0, 0, 255)}

                current_main = [0, 0]
                next_main = [0, 0]
                pied = 0
                current_hanche = [0, 0]
                next_hanche = [0, 0]
                block = [0, 0]
                avantav = [0, 0]
                avantar = [0, 0]
                arriereav = [0, 0]
                arrierear = [0, 0]

                frame_dep = 0
                distance = 0

                video = cv.VideoCapture(filePath)
                success = True
                first_frame = True

                #ajouter essai en first frame pour voir si video a droite ou a gauche

                while success and not water:
                        success, image = video.read()
                        if success:

                                
                # run inference on our chosen image, image can be a url, a numpy array, a PIL image, etc.
                                results = model.infer(image)

                                for object in results[0].predictions:
                                        if object.class_name == 'Starter':
                                                for keypoint in object.keypoints:
                                                        cv.circle(image, (int(keypoint.x), int(keypoint.y)), 
                                        radius=2,color=color['Starter'], thickness=-1)
                                                        if not dove:
                                                                if keypoint.class_name == 'piedav':
                                                                        pied = int(keypoint.x)
                                                        else:
                                                                if keypoint.class_name == 'mainar':
                                                                        next_main = [int(keypoint.x), int(keypoint.y)]
                                                                elif keypoint.class_name == 'mainav':
                                                                        next_main = [int(keypoint.x), int(keypoint.y)]
                                                                elif keypoint.class_name == 'hanches':
                                                                        next_hanche = [int(keypoint.x), int(keypoint.y)]
                                        elif object.class_name == 'Block':
                                                for keypoint in object.keypoints:
                                                        cv.circle(image, (int(keypoint.x), int(keypoint.y)), 
                                        radius=2,color=color['Block'], thickness=-1)
                                                        if not dove:
                                                                if keypoint.class_name == 'avant':
                                                                        block = [int(keypoint.x), int(keypoint.y)]
                                        else:
                                                for keypoint in object.keypoints:
                                                        cv.circle(image, (int(keypoint.x), int(keypoint.y)), 
                                        radius=2,color=color['Area'], thickness=-1)
                                                        if keypoint.class_name == 'avantav':
                                                                avantav = [int(keypoint.x), int(keypoint.y)]
                                                        elif keypoint.class_name == 'avantar':
                                                                avantar = [int(keypoint.x), int(keypoint.y)]
                                                        elif keypoint.class_name == 'arriereav':
                                                                arriereav = [int(keypoint.x), int(keypoint.y)]
                                                        else:
                                                                arrierear = [int(keypoint.x), int(keypoint.y)]

                                if not dove:
                                        frame_dep += 1
                                        if pied >= (block[0]+10):
                                                dove = True
                                                react = frame_dep/30
                                                imagereact = image
                                                imagereact = cv.putText(imagereact, f'Reaction Time: {round(react, 3)}s', (0, 40), cv.FONT_HERSHEY_SIMPLEX,  
                                1, color['Block'], 1, cv.LINE_AA)
                                                imagereact = cv.putText(imagereact, f'Starter', (180, 120), cv.FONT_HERSHEY_SIMPLEX,  
                                1, color['Starter'], 1, cv.LINE_AA)
                                                imagereact = cv.putText(imagereact, f'Block', (block[0]-100, block[0]+40), cv.FONT_HERSHEY_SIMPLEX,  
                                1, color['Block'], 1, cv.LINE_AA)
                                                imagereact = cv.putText(imagereact, f'Area', (avantav[0], avantav[1]+40), cv.FONT_HERSHEY_SIMPLEX,  
                                1, color['Area'], 1, cv.LINE_AA)
                                                
                                else:
                                        
                                        if next_main[1] >= (((avantav[1]+avantar[1])/2 + (arriereav[1]+arrierear[1])/2)/2 - 5):
                                                water = True
                                                x1moy = (arrierear[0]+arriereav[0])/2
                                                x2moy = (avantar[0]+avantav[0])/2
                                                y1moy = (arrierear[1]+arriereav[1])/2
                                                y2moy = (avantar[1]+avantav[1])/2
                                                distance = (math.sqrt((current_main[0]-x1moy)**2+(y1moy-current_main[1])**2)/math.sqrt((x2moy-x1moy)**2+(y1moy-y2moy)**2))*5
                                                p1 = (int(x1moy), int(y1moy))
                                                p2 = (int(x2moy), int(y2moy))
                                                #imagedist = cv.line(imagecur, (2*p1[0], 2*p1[1]), (2*p2[0], 2*p2[1]), color['Area'], thickness=1)
                                                imagedist = cv.putText(imagecur, f'Distance: {round(distance, 2)}m', (0, 80), cv.FONT_HERSHEY_SIMPLEX,  
                                2, color['Block'], 2, cv.LINE_AA)
                                                imagedist = cv.line(imagedist, (2*p1[0], 2*(p1[1]+10)),(2*p1[0], 2*(p1[1]-10)), color['Starter'], thickness=1)
                                                imagedist = cv.line(imagedist, (2*current_main[0], 2*int(y1moy+(distance/5)*(y2moy-y1moy))+10),(2*current_main[0], 2*int(y1moy+(distance/5)*(y2moy-y1moy))-10), color['Starter'], thickness=1)
                                                imagedist = cv.line(imagedist, (2*p1[0], 2*p1[1]), (2*int(x1moy+(distance/5)*(x2moy-x1moy)), 2*int(y1moy+(distance/5)*(y2moy-y1moy))), color['Starter'], thickness=1)

                                                
                                                imagedist = cv.line(imagedist, (2*current_hanche[0], 2*current_hanche[1]), (2*current_main[0], 2*current_main[1]), color['Starter'], thickness=1)
                                                angle = ang([p1, p2], [current_hanche, current_main])
                                                imagedist = cv.putText(imagedist, f'Angle: {round(angle, 2)}deg', (600, 80), cv.FONT_HERSHEY_SIMPLEX,  
                                2, color['Block'], 2, cv.LINE_AA)
                                                imagedist = cv.putText(imagedist, f'Starter', (2*280, 2*150), cv.FONT_HERSHEY_SIMPLEX,  
                                2, color['Starter'], 2, cv.LINE_AA)
                                                imagedist = cv.putText(imagedist, f'Block', (2*(block[0]-100), 2*(block[0]+40)), cv.FONT_HERSHEY_SIMPLEX,  
                                2, color['Block'], 2, cv.LINE_AA)
                                                imagedist = cv.putText(imagedist, f'Area', (2*avantav[0], 2*(avantav[1]+40)), cv.FONT_HERSHEY_SIMPLEX,  
                                2, color['Area'], 2, cv.LINE_AA)

                                image = cv.resize(image, (1280, 960), interpolation= cv.INTER_LINEAR)
                                cv.imshow('frame', image)
                                current_hanche = next_hanche
                                current_main = next_main
                                imagecur = image
                                if cv.waitKey(25) & 0xFF == ord('q'):
                                        break


                        else:
                                break
                imagereact = cv.resize(imagereact, (1280, 960), interpolation= cv.INTER_LINEAR)
                imagedist = cv.resize(imagedist, (1280, 960), interpolation= cv.INTER_LINEAR)
                cv.imwrite(os.path.splitext(f"{filePath}")[0]+'react.jpg', imagereact)
                cv.imwrite(os.path.splitext(f"{filePath}")[0]+'dist.jpg', imagedist)
                cv.destroyAllWindows()
        except:
                cv.destroyAllWindows()
                erreur = 1
        return erreur

 

# # load the results into the supervision Detections api
# detections = sv.Detections.from_inference(results[0].dict(by_alias=True, exclude_none=True))

# # create supervision annotators

# bounding_box_annotator = sv.BoundingBoxAnnotator()
# label_annotator = sv.LabelAnnotator()

# # annotate the image with our inference results
# annotated_image = bounding_box_annotator.annotate(
#     scene=image, detections=detections)
# annotated_image = label_annotator.annotate(
#     scene=annotated_image, detections=detections)

# # display the image
# sv.plot_image(annotated_image)



# # folder_dir = "C:/Git/ELE3000/ELE3000-1/test/images"
# model = YOLO("C:/Git/ELE3000/runs/pose/train22/weights/best.pt")
# # for images in os.listdir(folder_dir):
    

# image_path = f"C:/ELE3000/Video/2/testdive.mp4"
# video = cv.VideoCapture(image_path)
# success = True
# first = True

# while success:
#     success, image = video.read()

#     results = model(image)

#     # Iterate through detected objects  and draw bounding boxes
#     i = 0
#     for result in results:
#         keypoint = result.keypoints.xy.tolist()
#         if first:
#             if keypoint.length() > 4:
#                 type['Starter'] = i
#             elif keypoint.length() == 4:
#                 type['Area'] = i
#             else:
#                 type['Block'] = i
#         i+=1

#     first = False

                    
#print(result.names)
        # if i == 0:
        #     color = (255, 0, 0)
        # elif i == 1:
        #     color = (0, 255, 0)
        # else:
        #     color = (0, 0, 255)
        # i+=1
# for coord in keypoint:
#             if coord[0] != 0:
#                 cv.circle(image, (int(coord[0]), int(coord[1])), 
#                             radius=2,color=color, thickness=-1)

# # Display the image with bounding boxes
# cv.imshow("Object Detection", image)
# cv.waitKey(0)
# cv.imwrite(f"C:/Git/ELE3000/testKeypoints/{images}", image)

