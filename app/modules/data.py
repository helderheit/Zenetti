# -*- coding: utf-8 -*-
"""methods serving the IIIF api"""
import os

from flask import Blueprint, send_from_directory, send_file, request, jsonify
from flask_iiif.api import IIIFImageAPIWrapper
from werkzeug.utils import secure_filename
from modules.database import images, collections

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route("/data/<collection>/<item>/<uuid>/<region>/<size>/<rotation>/<quality>", methods=["GET"])
def get_image(collection, item, uuid, region, size, rotation, quality):
    quality = quality.replace(".jpg", "")
    quality = quality.replace(".tif", "")
    quality = quality.replace(".png", "")
    image = IIIFImageAPIWrapper.from_file("webapp/data/" + collection + "/" + item + "/" + uuid + ".tif")
    image.apply_api(
        region=region,
        size=size,
        rotation=rotation,
        quality=quality
    )

    return send_file(image.serve(), mimetype='image/jpeg')


@data_blueprint.route("/data/<collection>/<item>/<uuid>/info.json")
def get_image_info(collection, item, uuid):
    image = images.get_image(uuid)


    data = {
        "@context": "http://iiif.io/api/image/2/context.json",
        "@id": "http://localhost:4000/data/"+collection + "/"+item+"/"+uuid,
        "protocol": "http://iiif.io/api/image",
        "width": image["meta"]["width"],
        "height": image["meta"]["height"],
        "sizes": [
            {"width": 206, "height": 152},
            {"width": 309, "height": 238}
        ],
        "tiles": [
            {"width": 256, "height": 256, "scaleFactors": [1, 2, 4, 8, 16, 32]}
        ],
        "profile": [
            "http://iiif.io/api/image/2/level1.json",
            {"formats": ["jpg"],
             "qualities": ["native", "color", "gray", "bitonal"],
             "supports": ["regionByPct", "regionSquare", "sizeByForcedWh", "sizeByWh", "sizeAboveFull", "rotationBy90s",
                          "mirroring"],
             "maxWidth": 1000,
             "maxHeight": 1000
             }
        ]
    }
    return jsonify(data), 200

@data_blueprint.route("/data/<collection_id>.json")
def get_manifest(collection_id):
    collection = collections.get_collection(collection_id)
    manifest = {
      "@context": "http://iiif.io/api/presentation/2/context.json",
      "@id": "http://localhost:4000/manifests/album_01.json",
      "@type": "sc:Manifest",
      "attribution": collection["meta"]["attribution"],
      "metadata": [
        {
          "label": "Title",
          "value": "Album 1"
        },
        {
          "label": "Author(s)",
          "value": "Paul Zenetti"
        },
        {
          "label": "Publication date",
          "value": "20th century"
        },
        {
          "label": "Attribution",
          "value": "Haus der Bayerischen Geschichte and University of Regensburg"
        },
        {
          "label": "",
          "value": "<a href='https://www.uni-regensburg.de'>View website</a>"
        }],
      "label": "Albums of Paul Zenetti",
      "logo": "https://www.uni-regensburg.de/res/pics/logo.png",
      "service": {
        "@context": "http://iiif.io/api/search/1/context.json",
        "@id": "http://exist.scta.info/exist/apps/scta/iiif/pg-lon/search",
        "profile": "http://iiif.io/api/search/1/search",
        "label": "Search within this manifest"
        },
      "rendering": {
        "@id": "http://localhost:4000/",
        "format": "text/html",
        "label": "Full record view"
      },
      "sequences": [
        {"@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000092.json",
          "@type":"sc:Sequence",
          "label":"Default",
          "canvases":[
                {"@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000092.json",
                  "@type":"sc:Canvas",
                  "label":"Coming soon: Paul Zenetti",
                  "width":5392,
                  "height":8158,
                  "images":[{"@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000092.json",
                              "@type":"oa:Annotation",
                              "motivation":"sc:painting",
                              "on":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000092.json",
                              "resource":{"@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000092",
                                          "@type":"dctypes:Image",
                                          "format":"image/jpeg",
                                          "width":5392,
                                          "height":8158,
                                          "service":{"@context":"http://iiif.io/api/image/2/context.json",
                                                      "profile":"http://iiif.io/api/image/2/level1.json",
                                                      "@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000092"}}}]}
          ,{"@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000093.json",
                  "@type":"sc:Canvas",
                  "label":"Coming soon: Paul Zenetti",
                  "width":5392,
                  "height":8158,
                  "images":[{"@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000093.json",
                              "@type":"oa:Annotation",
                              "motivation":"sc:painting",
                              "on":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000093.json",
                              "resource":{"@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000093",
                                          "@type":"dctypes:Image",
                                          "format":"image/jpeg",
                                          "width":5392,
                                          "height":8158,
                                          "service":{"@context":"http://iiif.io/api/image/2/context.json",
                                                      "profile":"http://iiif.io/api/image/2/level1.json",
                                                      "@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000093"}}}]}
          ,{"@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000094.json",
                  "@type":"sc:Canvas",
                  "label":"Coming soon: Paul Zenetti",
                  "width":5392,
                  "height":8158,
                  "images":[{"@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000094.json",
                              "@type":"oa:Annotation",
                              "motivation":"sc:painting",
                              "on":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000094.json",
                              "resource":{"@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000094",
                                          "@type":"dctypes:Image",
                                          "format":"image/jpeg",
                                          "width":5392,
                                          "height":8158,
                                          "service":{"@context":"http://iiif.io/api/image/2/context.json",
                                                      "profile":"http://iiif.io/api/image/2/level1.json",
                                                      "@id":"http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000094"}}}]}

          ]}
      ],
      "thumbnail": {"@id": "http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000092/full/,200/0/default",
                    "service": {"@context": "http://iiif.io/api/image/2/context.json",
                                "@id": "http://localhost:4000/data/Zenetti_Tagebuecher/Album_01/ubr2008000092",
                                "profile": "http://iiif.io/api/image/2/level2.json"}},
      "within": "http://localhost:4000/"
    }

    return jsonify(manifest), 200