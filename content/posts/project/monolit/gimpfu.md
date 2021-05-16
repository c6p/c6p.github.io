---
title: "Gimp to YAML: Texture coordinates"
date: 2014-10-18T22:55:00+03:00
categories: [project/Monolit]
tags: [script, gimp]
---

I wrote a small [PythonFu](https://gist.github.com/c6parmak/e73d82fc28f8f8a129a8) to easily transfer textures using the layer data from multitextures prepared in the Gimp

![Texture coordinates](attachments/gimp-layers.png "Gimp screenshot")
<!--more-->
PythonFu saves visible layers above as a PNG image, then wrotes coordinates of, again, visible layers to YAML as below. I will use this in my UI library which is going to use YAML and ChaiScript. Also I am planning to make whole game configuration with these two.

```yaml
load: Untitled.png
textures:
- coords:
  - [0, 20, 20, 20]
  - [20, 20, 20, 20]
  name: button
  type: imagelist
- coords:
  - [0, 0, 20, 20]
  - [20, 0, 20, 20]
  name: Layer Group
  type: imagelist
- coords: [0, 0, 640, 400]
  name: Background
  type: image
```


