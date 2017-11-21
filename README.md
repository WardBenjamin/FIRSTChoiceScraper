# FIRST Choice Spreadsheet Generator

Scrapes the FIRST Choice website (https://firstchoicebyandymark.com), and adds that data to a spreadsheet to help with priority lists.

The spreadsheet (as a CSV) contains SKU, name, url, Price (in terms of credits), and max quantity (if applicable).

### Methodology (pseudo-code):

```
get every product-item

for each product, get the a inside product-title
for each a, get href and text
end
end

for each product, get the actual-price span text and the maxqty if applicable
```

##

## Authors

This software was created and is maintained by [Benjamin Ward](https://github.com/WardBenjamin). It is licensed under the MIT license.

