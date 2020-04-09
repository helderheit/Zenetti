## Image

### 

### The image Object

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

### 

### Basic Functions

#### 

#### Get Image

> [GET] api/1.0/images/`image_id`

#### 

#### Add Image

> [POST] api/1.0/images

#### 

#### Remove Image

> TODO

#### 

#### Update Image

> TODO

#### 

#### Update Crop

> TODO