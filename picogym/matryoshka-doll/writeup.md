# Matryoshka Dolls

Once we download the photo, we can view it and quickly tell that there isn't much to see. Taking the hint of the challenge's name, we might try to see if this file is hiding any other files. Running `binwalk` gives the following output.

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378955, uncompressed size: 383936, name: base_images/2_c.jpg
651613        0x9F15D         End of Zip archive, footer length: 22
```

Here, we can see that there is clearly a zip file hidden at the end of the image. `binwalk -e dolls.jpg` will extract said zip file. Like the name of the challenge suggests, there is another image with another zip file inside within this extracted file. Following this pattern we eventually find the key.
