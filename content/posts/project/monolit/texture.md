---
title: Texture
date: 2014-08-06T21:47:00+03:00
categories: [project/Monolit]
---

I have created the UV coordinates and textured with the image below. Coordinates sent are shaped as an hexagon, though test texture is oversimplified.

![](attachments/tile.png "Texture image")
<!--more-->

Hexagon tiles are textured randomly.

{{< gfycat "SnivelingCaringAmericanwigeon" >}}

To be honest I wrote this part on monday, then have spent last two days *debugging*. First I thought problem is shader, wrote a new one. Or somehow coordinates are not sent to the graphics card and searched h3dutCreateGeometryRes function for errors. But as said error quite possibly is within your code, since these libraries are heavily tested. At last I have convinced myself coordinates are wrong and printed. It was ok. And finally I realized I am checking coordinates within the calculation function, and I am sending a *now invalid pointer to a local variable*. *First use Occam's Razor*.
