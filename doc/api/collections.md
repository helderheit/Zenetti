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
    "id": [String], // Collection id
    "proto": "collection", 
    "owner": [Username], // Owner of the Collection, full rights
    "images": {}, // key-value list of page-number and refence to Image-Object
    "meta": { //Metadata
        "attribution": [String], //Institution
        "logo": [String], //Url to an image-file
        "label": [String],
        "description", [String]
    }
}
```

### Basic Functions

## Item

An **Item** is the  representations of an image-sequence, for example a scanned book or diary. It is basis for dynamic creation of IIIF-manifest-json-files.

The **Item** objects contains a sequence of refereneces to **Image**-objects. 

### Item Object

```json
{
    "id": [String], // Item id
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

> #### TODO



#### Add Item

> TODO



#### Remove Item

> TODO

#### Update Metadata

> TODO

----

### Rights-Managment

#### Update Owner

>TODO



#### Add Contributor

> TODO



#### Remove Contributor

> TODO

----

### Images

#### Add Image

> TODO



#### Remove Image

>TODO



#### Update Order

> TODO

----

### IIIF Functions

#### Get Manifest

> TODO