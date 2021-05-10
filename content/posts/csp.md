---
title: Demistifying Content Securiy Policy
date: 2021-05-09
datetime: 2021-05-09 20:42:49 
categories: [configuration]
tags: [security, web]
---

After I have built the site, the next step was checking performance and security. The **log**, besides being my learning notebook, is also a test-bed for my experiments.
![[Mozilla Observatory](https://observatory.mozilla.org/analyze/c6p.netlify.app) security grades](attachments/2021-05-09-20-54-11.png)
<!--more-->
## What is CSP?
An HTTP header for fine-grained control over where resources are loaded from. By employing content-security-policy, we can eliminate almost all *XSS* (Cross Site Scripting) attacks.

### Why XSS is a problem?
 arbitrary 

## May 6 — GitHub Pages
GitHub pages does not let us specify HTTP headers, and out of the box the grade is a **D**. One way is to include `<meta http-equiv="Content-Security-Policy" content="...">` as first child of `<head>`. Yet, netlify lets us set our response headers beyond other goodies, so I skipped ahead.

## May 8 — Netlify (A false hope)
Setting up a site on netlify from GitHub is trivial. Point to your repository, enter your build command and publish directory. Done.

Our response headers are in `_headers` file at the root of publish directory. Mozilla suggest starting with `default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self'` for CSP.

* `default-src` - default policy for allowed fallback sources
  * `img-src` - for images
  * `font-src` - for fonts
  * `script-src` - for scripts, i.e. JavaScript
  * `style-src` - for styles, i.e. CSS
  * `connect-src` - e.g. XMLHttpRequest, WebSocket
  * `object-src` - for plugins, e.g. Flash, Silverlight

{{< hint info >}}
* `'none'` - nothing
* `'self'` - same site
{{< /hint >}}
{{< hint warning >}}
  * `https:` - only HTTPS
  * `'strict-dynamic'` - let trusted code blocks to load additional scripts
{{< /hint >}}
{{< hint danger >}}
* `'unsafe-hashes'` - only code in event handler attributes, e.g. onClick
* `'unsafe-inline'` - all inline code blocks
* `'unsafe-eval'` - eval
{{< /hint >}}

I began with something similar to what Mozilla suggests, extended to allow CDNs for third party scripts. All `<script>`s required to have a hash or a nonce. A *nonce* is a cryptographically secure random token **per request** for a script block. It is impossible for a static site to return them. So we should include `sha256` *hash*es on `integrity` attributes (SRI — Sub-resource integrity) to ensure they are not tampered. Simple with Hugo templates.  
```html
<!-- For inline script blocks -->
{{ with (resources.Get "inline.js" | minify | fingerprint) }}
<script integrity="{{ .Data.Integrity }}">{{ .Content | safeJS }}</script>
{{ end }}
<!-- For external scripts -->
{{ $script := resources.Get "external.js" | minify | fingerprint }}
<script src="{{ $script.RelPermalink }}" integrity="{{ $script.Data.Integrity }}"></script>
```
Result is an **A+**. Yet, there is a problem. Error log shows that MathJax contains inline scripts and `eval`s. So we are not yet done.

Hugo can highlight code blocks (no highlight.js), can preprocess SCSS -via hugo-extended- (no node.js), can minify resources and generate hashes during build. But it can't yet generate diagrams (mermaid.js) nor typeset math (KaTeX, MathJax). Also, a client side search requires JavaScript. Thus, we still need some third party libraries. 

### Bonus point
Though irrelevant to CSP, important for security, for your external links...
There are some discussions for `rel` attribute for `<base>` tag for page wide rules.
```html
<a target="_blank" rel="nofollow noopener noreferrer">
``` 

## May 9 — Two steps back 
I had to add `unsafe-inline`s to restore full functionality, although errors about `eval`s were false flags. **B+**.

## May 9 - Victory