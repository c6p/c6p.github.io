---
title: NotAra
date: 2014-08-27T16:14:00+03:00
categories: [project/NotAra]
---

PDF annotaions is a review tool. They are useless for research notes and organizing them is pain. Also now web pages are a better resource for research or learning in general and bookmarks are incompetent to organize. There is already many applications providing a solution for this issue, albeit not completely. Some too complex, some requires a cloud subscription (though this is a plus for syncronization, even when privacy is disregarded there is the issue of file or database size limits), others do not have certain requirements, rest can only show and annotate only PDF or HTML.
<!--more-->

With [NotAra](https://github.com/c6parmak/NotAra) it will be possible to annoate (and import existing annotations) all supported documents with same interface and all notes will be kept categorically, while whole library can be searched against without giving up simplicity.

![NotAra text selection](attachments/notara-textselection.png)

For now PDF rendering and basic text selection is implemented. Very early stage of development. UI is going to be done with QtQuick 2 (Qt5). I hope it will ease implenting annotations and an android port won't require much modification. Although I have a little bit experience with Qt4, QtQuick was alien to me. Understanding C++ QML interaction took too much time, yet still I am not sure I understand it enough: Passing Poppler rendered pages and processing QML selections in C++ and sharing them back to QML.

Text quality (even with antialising enabled) is far beneath other Poppler based PDF readers. I am going to look at this after implementation of basic features.

