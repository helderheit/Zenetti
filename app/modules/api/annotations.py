from flask import jsonify
import numpy as np
import time
import cv2
import os
from pathlib import Path

from modules.api import api

from modules.database import items
from modules.database import images


@api.api_blueprint.route("/<item_id>/annotations_plain.json")
def get_plain_annotations(item_id):
    annotations_json = {}
    item = items.get_item(item_id)
    page_id = 0
    for image_id in item["images"]:
        image = images.get_image(image_id)
        if "annotations" in image:
            annotations_json[page_id] = {}
            annotation_id = 0
            objects = []
            for obj in image["annotations"]:
                objects.append({"value": obj["resource"][0]["chars"], "location": obj["on"][0]["selector"]["default"]["value"]})
                annotation_id += 1
            annotations_json[page_id] = objects
        page_id += 1

    return jsonify(annotations_json), 200


@api.api_blueprint.route("/<collection_id>/<item_id>/detected_objects.json")
def apply_object_detection(collection_id, item_id):
    path_to_data = "../app/webapp/data/" + str(collection_id) + "/" + str(item_id) + "/"
    path_to_yolo = "../app/webapp/yolo-coco"
    detected_objects = {}

    def detection_algorithm(input_image, input_yolo=path_to_yolo, input_confidence=0.5, input_treshold=0.3):
        tif_file = Path(input_image + ".tif")
        png_file = Path(input_image + ".png")
        jpg_file = Path(input_image + ".jpg")
        if tif_file.exists():
            input_image = input_image + ".tif"
        elif png_file.exists():
            input_image = input_image + ".png"
        elif jpg_file.exists():
            input_image = input_image + ".jpg"
        print("inp img = ", input_image)

        labelsPath = os.path.sep.join([input_yolo, "coco.names"])
        LABELS = open(labelsPath).read().strip().split("\n")

        weightsPath = os.path.sep.join([input_yolo, "yolov3.weights"])
        configPath = os.path.sep.join([input_yolo, "yolov3.cfg"])
        print("[INFO] loading YOLO from disk...")
        net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

        image = cv2.imread(input_image)
        (H, W) = image.shape[:2]
        ln = net.getLayerNames()
        ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                     swapRB=True, crop=False)
        net.setInput(blob)
        start = time.time()
        layerOutputs = net.forward(ln)
        end = time.time()
        print("[INFO] YOLO took {:.6f} seconds".format(end - start))

        boxes = []
        confidences = []
        classIDs = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
                if confidence > input_confidence:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        idxs = cv2.dnn.NMSBoxes(boxes, confidences, input_confidence,
                                input_treshold)

        output = {}

        if len(idxs) > 0:
            for i in idxs.flatten():
                x = boxes[i][0]
                y = boxes[i][1]
                w = boxes[i][2]
                h = boxes[i][3]
                label = "xywh=" + str(x) + "," + str(y) + "," + str(w) + "," + str(h)
                output[label] = str(LABELS[classIDs[i]])

        return output

    item = items.get_item(item_id)
    page_id = 0
    for image_id in item["images"]:
        input_path = path_to_data + str(image_id)
        print(input_path)
        detected_in_curr_image = detection_algorithm(input_path)
        detected_objects[page_id] = detected_in_curr_image
        page_id += 1

    return jsonify(detected_objects), 200
