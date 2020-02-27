# Data

## Delivering Image Data

This workflow offers an non destructive way to crop into a bookpage contained in an image and to adjust the rotation of the scan.

```
+ - - - - - - +         + - - - - - - - - +         + - - - - - - - - +         #######################
|             |         |                 |         |                 | < - - - #     HTTP-request    #
|  RAW IMAGE  | - - - > | CROP + ROTATE   | - - - > | IIIF - workflow |         #    (region, size,   #
|             |         |                 |         |                 | - - - > #  rotation, quality) #
+ - - - - - - +         + - - - - - - - - +         + - - - - - - - - +         #######################
                                ^
                                |
+ - - - - - - - - +             | Page information
|                 |             |
|  Image Object   | - - - - - - +
|                 |
+ - - - - - - - - +
```

## IIIF Methods

### Get image

> [GET] api/1.0/`collection`/`item_id`/`uuid`/`region`/`size`/`rotatin`/`quality`

Returns an image or a region of an image with applied IIIF workflow.

#### Notes:

Use `region` = **full** to get the whole image

### Get image info

> [GET] api/1.0/`collection`/`item_id`/`uuid`/info.json

Returns information for an image in IIIF-style.

### Get manifest

> [GET] api/1.0/`collection`/ `item_id`/manifest.json

Returns a IIIF manifest.