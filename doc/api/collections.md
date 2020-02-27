# Collections

## Datastructure

```
+ - - - - - - - - +                   + - - - - - - - - +                  + - - - - - - - - +
|                 | 0.. *       0.. * |                 | 1          0.. * |                 |
|	Collection    | - - - - - - - - - |      Item       | - - - - - - - - -|      Image      |
|                 |                   |                 |                  |                 |
+ - - - - - - - - +                   + - - - - - - - - +                  + - - - - - - - - +
```



## Collection

A **Collection** manages associated **Items** an provides accumulated rights-managment.



### Collection Object

```json
{
    "_id": [String], // Collection id
    "proto": "collection", 
    "owner": [Username], // Owner of the Collection, full rights
    "items": [], //List of items-ids 
    "meta": { //Metadata
        "attribution": [String], //Institution
        "logo": [String], //Url to an image-file
        "label": [String],
        "description", [String]
    }
}
```

### Basic Functions

#### Get Collection

> [GET] api/1.0/collections

#### Get Collection

>[GET] api/1.0/collections/`colletion_id`

#### Add Collection

>[POST] api/1.0/collections

#### Update Collection

>[PUT] api/1.0/collections/`collection_id`

## Item

An **Item** is the  representations of an image-sequence, for example a scanned book or diary. It is basis for dynamic creation of IIIF-manifest-json-files.

The **Item** objects contains a sequence of refereneces to **Image**-objects. 

### Item Object

```json
{
    "_id": [String], // Item id
    "proto": "item", 
    "owner": [String], // Username of the owner of the Item, full rights
    "read": [], // List of Usernames with read permission
    "annotate": [], // List of Usernames with permission to annotate the item
    "edit": [], // List of Usernames with permission to edit
    			//the structure of the document, to add, remove and crop images etc.
    "images": {}, // key-value list of page-number and refence to Image-Object
    "meta": { //Metadata
        "attribution": [String], //Institution
        "logo": [String], //Url to an image-file
        "label": [String],
        "description", [String]
    },
    "thumbnail", [String] // reference of image object used as thumbnail
}
```

----

### Basic Functions

#### Get Item

> [GET] api/1.0/item/`item_id`

#### Add Item

> [GET] api/1.0/item/`collection_id`

#### Remove Item

> [DELETE] api/1.0/item/`collection_id`/`item_id`

#### Update Item

> [PUT] api/1.0/item/`item_id`

----

### Rights-Managment

#### Update Owner

>TODO

#### Add Contributor

> TODO

#### Remove Contributor

> TODO

----

## Image

### The image Object

```json
{
    "_id": [String], // Image id
    "file-name": [String],
    "file-extension": [String],
    "path": [String], //full path to th image file in the data directory
    "proto": "image", 
    "owner": [String], // Username of the owner of the image, full rights
    "meta": { //Metadata
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
}
```



### Basic Functions

#### Get Image

> [GET] api/1.0/images/`image_id`

#### Add Image

> [POST] api/1.0/images

#### Remove Image

>TODO

#### Update Image

> TODO

#### Update Crop



> TODO