---
title: Demistifying Content Securiy Policy
date: 2021-05-09
datetime: 2021-05-09 20:42:49 
categories: [configuration]
tags: [security, web]
---

After I have built the site, the next step was checking performance and security. The **log**, besides being my learning notebook, is also a test-bed for my experiments.
![[Mozilla Observatory](https://observatory.mozilla.org/analyze/c6p.netlify.app) security grades](attachments/2021-05-10-15-24-07.png)
<!--more-->
## What is CSP?
An HTTP header for fine-grained control over where resources are loaded from. By employing content-security-policy, we can eliminate [almost all](https://csp.withgoogle.com/docs/faq.html#caveats) *XSS* (Cross Site Scripting) attacks. [Read](https://csp.withgoogle.com/docs/why-csp.html) further for why XSS is a problem.

## May 6 — GitHub Pages
[GitHub pages](https://pages.github.com/) does not let us specify HTTP headers. One way is to include `<meta http-equiv="Content-Security-Policy" content="...">` as first child of `<head>`. Yet, netlify lets us set our response headers beyond other goodies, so I skipped ahead.  Out of the box the grade is a **D**.
## May 8 — Netlify (A false hope)
Setting up a site on [netlify](https://www.netlify.com/) from GitHub is trivial. Point to your repository, enter your build command and publish directory. Done.

Our response headers are in `_headers` file at the root of publish directory. Mozilla suggests starting with `default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self'` for CSP.

* `base-uri` - restrict URLs for `<base>`
* Fetch directives:
  * `default-src` - default policy for allowed fallback sources
  * `img-src` - for images
  * `font-src` - for fonts
  * `script-src` - for scripts, i.e. JavaScript
  * `style-src` - for styles, i.e. CSS
  * `connect-src` - e.g. XMLHttpRequest, WebSocket
  * `object-src` - for plugins, e.g. Flash, Silverlight

{{< hint info >}}
* `'none'` - nothing
{{< /hint >}}
{{< hint warning >}}
* `'self'` - same site
* `https://example.com/external.js` - specific external resource
{{< /hint >}}
{{< hint danger >}}
* `https:` - only HTTPS
* `'unsafe-hashes'` - only code in event handler attributes, e.g. onclick
* `'unsafe-inline'` - only inline blocks
* `'unsafe-eval'` - `eval, 
{{< /hint >}}

I began with something like what Mozilla suggests, extended to allow CDNs for third party scripts. All `<script>`s required to have a hash or a nonce. A *nonce* is a cryptographically secure random token **per request** for a script block. It is impossible for a static site to return them. So we should include `sha256` *hash*es on `integrity` attributes (SRI — Sub-resource integrity) to ensure they are not tampered. Simple with Hugo templates.  
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

{{< hint info >}}
Hugo can highlight code blocks (no highlight.js), can preprocess SCSS (via hugo-extended, no node.js), can minify resources and generate hashes during build. But it can't yet generate diagrams (mermaid.js) nor typeset math (KaTeX, MathJax). Also, a client side search (FlexSearch in my case) requires JavaScript. Thus, we still need some third party libraries. 
{{< /hint >}}

<!--
### Bonus point
Though irrelevant to CSP, important for security, for your external links...
There are some discussions for `rel` attribute for `<base>` tag for page wide rules.
```html
<a target="_blank" rel="nofollow noopener noreferrer">
```
-->

## May 9 — Two steps back 
I had to add `unsafe-inline`s and domains of CDNs to restore full functionality, although errors about `eval`s were false flags. **B+**.

## May 10 — Onward!
I learned `strict-dynamic` and parsed *integrity* hashes of all inline and external scripts. It worked in Chrome. Sadly caused many problems on [Firefox](https://bugzilla.mozilla.org/show_bug.cgi?id=1409200 "Bugzilla"). Following hours of debugging and reading bug reports, I grasped, though it is supported for years, it is unusable. Since [CSP-3](https://www.w3.org/TR/CSP3/) being a working draft, *hash*es for external scripts are unsupported. Still **B+**.
{{< hint info >}}
  * `'strict-dynamic'` - let trusted code blocks to load additional scripts
{{< /hint >}}

### A Bittersweet Victory
It seems [CSP-2](https://www.w3.org/TR/CSP2/) (current W3C Recommendation) only supports *hash*es for inline scripts, requiring more fine-grained regexps.  

I created a git pre-commit hook to update hashes whenever I commit my site, in *PowerShell* being on Windows. Search is using *ripgrep*, `-oIN` meaning only print matches without filename or line numbers, and `-r` to modify result by adding single quotes around it. Unique results filtered and joined on a single line, and written to a file. 

Where first regexp for all integrity strings, second one filters only inline scripts, and third one generating 
```posh
hugo --minify
(rg -oIN '<script.*?(sha\d{3}-.{43}=)\"' -r '''$1''' public | sort -unique) -join ' ' | out-file -encoding ASCII -noNewline data/script_hash.txt 
(rg -oIN '<script.*?(sha\d{3}-.{43}=)\".*?>[^\n<>]+?</script>' -r '''$1''' public | sort -unique) -join ' ' | out-file -encoding ASCII -noNewline data/inline_script_hash.txt 
(rg -oIN '<script.*?src=\"?(http.*?\.js)[ \">]' -r '$1' public | sort -unique) -join ' ' | out-file -encoding ASCII -noNewline data/external_script_source.txt
```

Hugo layout template `index.headers` is used to generate `_headers`. Here is only the relevant part for `script-src`.
```html {.wrap}
script-src {{readFile "data/inline_script_hash.txt"}} 'self' {{readFile "data/external_script_source.txt"}};
```
And the result **A+**.
```html {.wrap}
script-src 'sha256-aECzxYUJ57J5H6YymaVqtppSpIqD2Z9YAIAZfd/2xMY=' 'sha256-MktN23nRzohmT1JNxPQ0B9CzVW6psOCbvJ20j9YxAxA=' 'sha256-OBZ1TAxtlr9xf3a+8VMnoX0v39PPCWCsN6DfNkKio/I=' 'self' https://cdn.jsdelivr.net/npm/mathjax@3.1.4/es5/tex-mml-chtml.js https://cdn.jsdelivr.net/npm/mermaid@8.9.3/dist/mermaid.min.js;
```

Whole content security policy line:
```html
Content-Security-Policy: default-src 'none'; base-uri 'self'; manifest-src 'self'; connect-src 'self'; font-src 'self' https://cdn.jsdelivr.net; img-src 'self' data:; script-src 'sha256-aECzxYUJ57J5H6YymaVqtppSpIqD2Z9YAIAZfd/2xMY=' 'sha256-MktN23nRzohmT1JNxPQ0B9CzVW6psOCbvJ20j9YxAxA=' 'sha256-OBZ1TAxtlr9xf3a+8VMnoX0v39PPCWCsN6DfNkKio/I=' 'self' https://cdn.jsdelivr.net/npm/mathjax@3.1.4/es5/tex-mml-chtml.js https://cdn.jsdelivr.net/npm/mermaid@8.9.3/dist/mermaid.min.js; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; object-src 'none'
```
### Further Reading
* [Google Developer Documentation](https://developers.google.com/web/fundamentals/security/csp)
* [CSP Quick Reference Guide](https://content-security-policy.com/)
* [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)