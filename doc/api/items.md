# Items

## Item object

An **Item** is the  representations of an image-sequence, for example a scanned book or diary. It is basis for dynamic creation of IIIF-manifest-json-files.

The **Item** objects contains a sequence of references to **image**-objects. 

### Item Object

```
{
    "_id": [String], // Item id
    "proto": "item", 
    "owner": [String], // Username of the owner of the Item, full rights
    "read": [], // List of Usernames with read permission
    "annotate": [], // List of Usernames with permission to annotate the item
    "edit": [], // List of Usernames with permission to edit
    			//the structure of the document, to add, remove and crop images etc.
    "images": [], // refences to Image-Objects
    "meta": { //IIIF-Metadata
        "attribution": [String], //Institution
        "logo": [String], //Url to an image-file
        "label": [String],
        "description", [String]
    },
    "metadata": [ //Annotated Metdata for the item
        {
         "label": [String],
         "value": [String]
        }
    ],
    "thumbnail", [String] // reference of image object used as thumbnail
}
```

## Get Item

> [GET] api/1.0/items/`item_id`

### Returns

An item object

### Status Codes

- **200** 
- **409** *Could not get item*
- **401** *Access denied*

### Access

- basic protection

## Add Item

> [GET] api/1.0/items/`collection_id`

### Required fields

```
{
    "label": [String],
    "description": [String],
    "attribution": [String],
    "logo": [String], // url to a logo image
}
```

### Returns 

A item object

### Status Codes

- **200** 
- **409** *Could not add item*
- **422** *Missing field*
- **401** *Access denied*

### Access

- basic protection

## Remove Item

> [DELETE] api/1.0/items/`collection_id`/`item_id`

## Update Item

> [PUT] api/1.0/items/`item_id`

### Required fields

```
{
    "label": [String],
    "description": [String],
    "attribution": [String],
    "logo": [String], // url to a logo image
}
```

### Returns 

A item object

### Status Codes

- **200** 
- **409** *Could not update item*
- **422** *Missing field*
- **401** *Access denied*

### Access

- basic protection

## Get Annotations

> [GET] api/1.0/`collection_id`/`item_id`/annotations.json"

### Returns

A key value list of annotations. This list is loaded into local storage to display the Annotations in Mirador.

### Status Codes

- **200** 
- **401** *Access denied*

### Access

- basic protection

## Rights-Managment

#### Update Owner

>TODO

#### Add Contributor

> TODO

#### Remove Contributor

> TODO

