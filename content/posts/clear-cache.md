---
title: Get Fresh Pages with Messed Up Caches
date: 2021-05-13T10:27:22+03:00
categories: [config]
tags: []
---
While fixing `Content-Security-Policy` header, I have messed up the caches. I have accidentally pushed a change to keep all pages in the cache indefinitely. Situation: browsers are now serving stale pages.
<!--more-->

[Netlify custom headers](https://docs.netlify.com/routing/headers/) documentation does not mention that wildcards may [swallow everything](https://answers.netlify.com/t/confusing-headers-behaviour/17588/3?u=c6p), and does not give any examples of pattern use, in practice `/*.*` pattern matches same paths with `/*`. But, while digging forum posts [this post](https://answers.netlify.com/t/format-of-custom-headers-glob/13037/5?u=c6p) come up, though a support engineer mentions it is an unsupported feature.
```html
/*
  Cache-Control: public, max-age=360
/*.(jpg|jpeg|gif|png|webp|svg)
  Cache-Control: public, max-age=31536000, immutable
```
One can specify it in this manner, take caution, order matters. First pattern matches everything, second one overwrites settings.

## Cache-Control
The header controls how long a resource will be kept in browser caches, and when should it be refreshed. A balance is important, to not request same data repeatedly for less bandwidth and better performance, while not serving stale data.
| Directive | Effect |
|-:|:-|
|`public`| may be stored by *any* cache |
|`private`| may be stored only by *browser's* cache |
|`no-cache`| may be stored, must revalidate |
|`no-store`| may **not** be stored, with `max-age=0` force re-validate 
|`max-age=<seconds>`| max time resource is fresh |
|`must-revalidate`| must not use stale copy without successful validation on the server |
|`immutable`| will *not change* over time, do not revalidate |

For more directives and detailed info check out [MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control).

We can store static resources like images, JS and CSS files forever[^2]. When we must change these resources, we should employ Cache Busting[^1] strategies.
```html
Cache-Control: public, max-age=31536000, immutable
```
{{< hint warning >}}
**Warning:** Double check resources, they will be kept indefinitely.
{{< /hint >}}

For a static site, HTML endpoints (URLs) will remain same, though content will change. We can use several strategies.
* Do not cache at all:
  ```html
  Cache-Control: no-store, max-age=0
  ```
* Cache only a short time (5 mins):
  ```html
  Cache-Control: public, max-age=300 xx
  ```

## Clear-Site-Data
The header is still a [working draft](https://www.w3.org/TR/clear-site-data). Even though it seems to be supported, it is not working as advertised in Firefox. Setting it on Chrome removes offline data correctly.
```html
Clear-Site-Data: "cache"
```
{{< hint info >}}
Attention to the *double quotes*. Other [directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data#directives) are `"cookies"`, `"cookies"`, `"storage"`, `"executionContexts"`, `"*"`.
{{< /hint >}}

### What now?
Andrews Betts [has several solutions](https://www.fastly.com/blog/clearing-cache-browser). Iframe + POST method from the article should work cross-browser for same-origin resources, to transparently refresh a specific resource stuck in cache.

For now, all the visitors I get are friends, so a self refresh is a possibility. I am going to skip it, but it may come in handy in the future.

[^1]: Modifying URL to replace an existing file that is already cached. 
    * File name versioning (e.g. style.v2.css)
    * File path versioning (e.g. v2/style.css)
    * Query strings (e.g. style.css?ver=2)
[^2]: [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt) HTTP/1.1 servers SHOULD NOT send Expires dates more than one year in the future.