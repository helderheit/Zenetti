from flask import jsonify
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
