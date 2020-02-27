import uuid

from modules.api import api
from modules.database import database


def get_image(image_id):
    try:
        data = database.server[database.DATA_DB_NAME][image_id]
        if "proto" in data:
            if data["proto"] == "image":
                del data["rev"]
                return data
        print("Could not get image " + image_id + ": Document type not image")
        return None

    except Exception as e:
        print("Could not get image " + image_id + ": " + str(e))
        return None


def add_image(file_name, file_extension, path, width, height):
    try:
        image_id = str(uuid.uuid4())
        database.server[database.DATA_DB_NAME][image_id] = {"_id": image_id,
                                                            "proto": "image",
                                                            "file-name": file_name,
                                                            "file-extension": file_extension,
                                                            "path": path,
                                                            "owner": "",
                                                            "meta": {
                                                                "width": width,
                                                                "height": height,
                                                                "crop": {}
                                                            }
                                                            }
        print("Added image to database")
        return get_image(image_id)

    except Exception as e:
        print("Could not add image" + str(e))
    return None
