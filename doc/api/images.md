# Images

 ## Image Object

```
{
    "_id": [String], // Image id
    "file-extension": [String],
    "path": [String], //full path to th image file in the data directory
    "proto": "image", 
    "owner": [String], // Username of the owner of the image, full rights
    "meta": { //IIIF-Metadata
        "width": [Integer]
        "height": [Integer]
    	"crop": {
            "crop-width": [Integer]
            "crop-height": [Integer]
            "crop-x": [Integer],
            "crop-y": [Integer],
            "rotation": [Float]
		}
    },
	"metadata": [//Annotated Metdata
        ]
}
```

## Get Image

> [GET] api/1.0/images/`image_id`

### Returns

An image object

### Status Codes

- **200** 
- **409** *Could not get image*
- **401** *Access denied*

### Access

- basic protection

## Add Image

> [POST] api/1.0/images

### Required fields

```
{
    "file-name": [String],
    "file-extension": [String],
    "path": [String],
    "width": [int]
    "height": [int]
}
```

### Returns 

An image object

### Status Codes

- **200** 
- **409** *Could not add image*
- **422** *Missing field*
- **401** *Access denied*

### Access

- basic protection

## Remove Image

> TODO

## Update Image

> TODO

## Update Crop

> TODO

## Upload Image

> [POST] api/1.0/images/`collection_id`/`item_id`

### Required

An image file

### Status Codes

- **201** *File successfully uploaded*
- **401** *Access denied*

### Access

- basic protection

## Update Annotations

> [POST] api/1.0/images/`image_id`/annotations

Storing the annotation object from localstorage in the database.

### Required fields

```
{
    "annotations": {}
}
```

### Returns 

An image object

### Status Codes

- **200** 
- **409** *Could update annotations for image*
- **422** *Missing field*
- **401** *Access denied*

### Access

- basic protection