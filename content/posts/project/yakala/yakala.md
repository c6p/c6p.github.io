---
title: "Yakala — capture everything"
date: 2021-05-16T10:31:03+03:00
categories: [project/Yakala]
---
Years ago I had difficulty in taking notes and capturing information, and couldn't find anything to fit my needs. I tried to create a cross-platform application to fill the gap: [**NotAra**](/categories/project/notara). I faced technological problems, life intervened, and the project just got stuck. Today, I am not even sure, whether I pushed all local changes to GitHub. 

Anyways, in the meantime, apps to fill the niche has emerged. As you can tell from NotAra screenshots, [Polar](https://getpolarized.io/) is what I had in mind to capture information. But the name NotAra means "Note Search", so the process did not stop with capturing data, but using that information to easily create cross-linked notes[^1]. Note-taking I envisioned is similar to [Obsidan](https://obsidian.md/) today.
<!--more-->
[^1]: [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten)

 During the passing years, many projects have popped up. Trying them out made me realize something. *Capturing* information and *writing* are two different processes that requires different states of mind. The essence of [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) did not transfer well to the world of GUI, so we ended up with unmaintained cemetery of monoliths, while the same Unix tools just as alive as they were 50 years ago.
## Current software ecosystem
> Put small good perfect things around you, you higher men! Their golden ripeness heals the heart. What is perfect teaches hope. [^2]
[^2]: Thus Spake Zarathustra, Friedrich Nietzsche - [google books](https://books.google.com.tr/books?id=xuR59sqNLPAC&pg=PA227).

* [Org Mode](https://orgmode.org/) for Emacs: The mode that started everything. Emacs, emerging from GNU project with a distinct contrast to its roots as a monolith that does everything[^4], has the greatest note-taking tool ever made: Org Mode. It has many features, and being a part of Emacs, all are very extensible. Capture information, take notes, keep To-Dos, manage your calendar, cross-reference research, publish blogs/articles/books. It can even double as an executable research notebook, replacing [jupyter](https://jupyter.org/). [^3]   

  All that is great when you are in Emacs ecosystem, know Emacs commands and Elisp to heart. Also, as all the tools that does everything, it does most of them poorlier than the competition. Though it has the best agenda view in the entire universe, you can pull what you want to see regardless of whereabouts in from all `.org` files. Files are just text, you can sync them to Dropbox, git etc. Even if the new clients somewhat eased the editing on mobile, they are still clumsy. And the capture mode with all the extensions is not as easy or seamless as I want. Of course all, after you learn to use Emacs, and that is a big one.
[^4]: To be honest, not in contrast to the philosophy, but GNU Emacs is its own OS with its own Lego blocks.
[^3]: There was a quote that I cannot remember where I saw, inspired by the famous one from George Santayana: "Those who cannot remember the past are condemned to repeat it, badly." The text was about rewriting good old programs in [Electron](https://www.electronjs.org/) — harder to use, slower, requiring more memory. The last added bit, *badly*, creates all the difference. 
* [OneNote](https://www.onenote.com): It is like [Basket Note Pads](https://basket-notepads.github.io) which is around for a long time. Both let you put rich content on an infinite canvas, Basket Note Pads are even more featureful in [KDE](https://kde.org/), though as I remember it lacked the key features of OneNote, easy remote sync and mobile support. These tools are not to my taste, merging information capture and note-taking into one. It works for keeping things together for a self-contained idea, but when things get entangling it falls short. Besides, they lack referencing to parts of a document. I sometimes use this exempt of better options, when I need to quickly jot down notes and then study everything together as I am preparing for an exam, or sketching designs.
* [Google Keep](https://keep.google.com): It does well what it does, OCR is useful, but it does not capture or reference any fine data from documents as above. Hard to force a structure upon data. It can be a cloud backend for Yakala in the future, where it stores resources and the database kept in Google Drive.
* [Evernote](https://evernote.com/): Being older and more feature rich, besides rich text editing and better extensions for information capture, it is actually quite similar to google keep in its core. Shares mostly the same deficiencies and mostly useless without premium.
* [DEVONthink](https://www.devontechnologies.com/apps/devonthink): Mac, iOS only. I couldn't try it. But, skimming features, screenshots, and videos; I think it implements many ways to capture and edit documents within a single suite. Whether it checks all the boxes, I honestly don't know. Its standalone capture helper '*Sorter*' seems similar to planned Yakala. Has OCR, supports PDFs, EPUBs, HTMLs, RTFs. One advertised feature is smart rules to carry out actions which I did also plan. While reading reviews now, I understand its transactional backup feature is also very similar to how sync will work in Yakala that I am going to detail below.

You may argue, most of them are not information capturing tools but actually for notes. However, the process of info-capture is half-baked as extensions into these tools and one may claim jotting down some notes is really a capture of ideas, except the case of organized thoughtful writing. Ignoring Org Mode, all in the end, are keeping information that really begs to be used anywhere else. That is why you have a pile of things never looked upon again. That we set out to solve.

### Academic Writing and Citation Manager
* [Papers](https://www.papersapp.com/): Only for PDFs. Annotation and cross-referencing. It has a very pretty web editor though, I can get *inspired* for NotAra.
* [Zotero](https://www.zotero.org/): It does one thing and does it very well. Keeps a library of tagged sources, it can download web snapshots. Supports many text editors. Has very rich library of plugins. In the future, I can make *integrations* to Yakala and NotAra. Alternative [Mendeley](https://www.mendeley.com) is just Zotero with annotations support and social features.


### Annotation Tools
You capture information from documents by annotating certain parts.
* [Polar](https://getpolarized.io/): As I have stated before, it is very similar to what I *envisioned* when I started NotAra (at v0.1). Open source. It supports PDFs, EPUBs, can download HTMLs to annotate them. Cross-platform, though mobiles not yet supported. Ok, there is a catch, a big one. New version does not work offline, and free accounts naturally has limited quota. Annotated data cannot easily be used anywhere else, which is the whole point of capturing.
* [hypothes.is](https://hypothes.is): I'm *using* it to annotate webpages, it can only do highlights. Annotating PDFs in the browser is possible. A problem with this approach is when the source document is not accessible anymore, you are only left with your notes. Mentioning it, notes can be written in markdown. Annotation data can be accessed via an API.
* [Memex](https://getmemex.com/): Hypothes.is with additional features. Mobile support, excellent search, youtube annotations, integrations to note-taking apps. Automated sync is a premium feature. Memex is a great competitor. Though in the end, what it does capture is only highlights and notes over them.
* [Keypoints](https://keypoints.app/): I couldn't try it, Mac only. Only PDF annotation. It has markdown note editor where you can reference your annotations.

I skipped tools that are chiefly for organized[^5] note-taking such as RemNote, Roam Research, Obsidian, Foam, TiddlyWiki, OmniOutliner, ; or tools mainly for academic writing or referencing like Zotero, Mendeley, Papers, Bookends or document creation software such as Word. They will be discussed in the context of NotAra.
[^5]: Organized not necessarily structured.

## Requirements
should:
* be used offline
* sync across devices seamlessly
  * even when multiple devices were offline for a very long time
* capture any form of data
* capture existing annotations
* reference inner elements of documents such as HTML or PDF
* let attaching metadata, like tags or references to other resources
* able to export information
* able to query information
  * and provide that in many forms, be it FUSE or GraphQL
* able to provide academic references to editors

## Envisioned usage
* **Capture** phase:  
  * Audio, Video, Image etc.  
    Depending on the settings or the shortcut used, will either be directly saved into `inbox` or ideally will launch an *editor* to cut/crop base content, and in next step an *annotation* tool. Annotations and cut (or original if desired) base content will be kept and served separately. 
  * HTML, PDF etc.  
    User will just select an area. Information will be captured via Browser Extensions or a similar tool on mobile. Base content (as single page for HTML), and annotations will again be saved separately. Unlike competitor, it won't be an image, but styled DOM elements for HTML and areas. *Polar* (and incomplete NotAra tries to) do this.
* **Organize** phase:  
  Metadata may be attached during capture via tags, references, or short notes. Or it may be done at inbox.
* **Rule Creation** phase:
  User have captured a YouTube or IMDB link, where should it go? Inbox. Way no. It can be added to a watch-list offline or to our account at their respective sites. Title, image, PDF or user-set metadata matches a filter. It goes brr. User can also view what automated actions have been carried out and their success.
* **Query** phase:  
  Database may quickly be searched to pick and insert a specific capture, via a popup launched by a shortcut. Or from CLI, web interface or inside your choice of document editor. Yakala will act as a data provider in last case.
* **Sync** or **Backup** phase:  
  Not really a phase, it will be a one time linking of devices. Backup/restore to/from a database, will be a single command away without any hassle.

## Design and Architecture
Well, it is still huge. How I am going to realize it.

### Version 0.1 or Minimum Viable Product
Yakala will be written in Rust, and encompass a single portable executable. Central point will be the *server*, which can be compiled with a *GUI* ([Tauri](https://tauri.studio/en/)) for desktop use.

Browser *extensions* to capture structured web data will communicate with the server via *WebSockets*. Every other clipping tool saves an image, we will directly reference the DOM element.

Also, Yakala will boast its own web view to render PDFs, EPUBs, images, videos and other documents, thanks to Tauri. 7 years ago I didn't want to go this way, and chose Qt with its native controls, but since then web have come a long way. When Tauri supports mobile devices we can also target them.

All capture-ready resources will be annotated in a UI similar to Polar. Clipboard data may also be quickly captured.

Database will be SQLite due to its ubiquity. Copies of captured binary documents will be kept in the file system. Linked annotations will be kept in database, with a UUID identifying also the current database. All rows will be immutable, and also contain their own hash (base64 encoded SHA256). Changes will be kept as rows of patches with [pijul](https://pijul.org/) algorithm. In this way I plan to implement synchronization of version controlled annotation. Since source documents are not to be touched, they will be synced directly. The problem of always growing database will be mitigated by keeping only the control hashes of deleted changes/annotations.

Every copy of database created will have its own identifier. So a sync between devices will actually be a sync of databases. I presume it is also how DEVONthink implements transactional backups. Caching information on exchanged rows in a table will speed up synchronization. So a sync can both be done with a single Yakala instance and multiple databases; and also between multiple Yakala instances in the network.