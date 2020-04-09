# Collections

> modules/api/collections.py

## Data structure

```
+ - - - - - - - - +                   + - - - - - - - - +                  + - - - - - - - - +
|                 | 0.. *       0.. * |                 | 1          0.. * |                 |
|	Collection    | - - - - - - - - - |      Item       | - - - - - - - - -|      Image      |
|                 |                   |                 |                  |                 |
+ - - - - - - - - +                   + - - - - - - - - +                  + - - - - - - - - +
```



## Collection object

A **Collection** manages associated **items** an provides accumulated rights-managment.

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

## Get collections

> [GET] api/1.0/collections

### Returns

A list of collection objects

### Status Codes

- **200**
- **409** *Could not get collections*
- **401** *Access denied*

### Access

- basic protection

## Get collection

>[GET] api/1.0/collections/`colletion_id`

### Returns

A collection objects

### Status Codes

- **200**
- **409** *Could not get collection*
- **401** *Access denied*

### Access

- basic protection

## Add collection

>[POST] api/1.0/collections

### Required fields

```json
{
    "label": [String],
    "description": [String],
    "attribution": [String],
    "logo": [String], // url to a logo image
}
```

### Returns 

A collection object

### Status Codes

- **200** 
- **409** *Could not add collection*
- **422** *Missing field*
- **401** *Access denied*

### Access

- basic protection

## Update collection

>[PUT] api/1.0/collections/`collection_id`

### Required fields

```json
{
    "label": [String],
    "description": [String],
    "attribution": [String],
    "logo": [String], // url to a logo image
}
```

### Returns 

A collection object

### Status Codes

- **200** 
- **409** *Could not update collection*
- **422** *Missing field*
- **401** *Access denied*

### Access

- basic protection

## Remove collection

> [Delete] api/1.0/collections/`collection_id`

### Status Codes

- **200** *Removed collection*
- **409** *Could not remove collection*
- **401** *Access denied*

### Access

- basic protection