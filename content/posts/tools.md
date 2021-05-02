---
title: Developer and Power User Tools List
tags: [ windows, linux, maintenance ]
date: 2021-05-02
datetime: 2021-05-02 18:03:51
categories: [ configuration ]
---
Inspired by [Hanselman Ultimate Tool List](https://www.hanselman.com/tools), check out for even more awesome tools.

## Windows
- [scoop](https://scoop-docs.now.sh/) — **Package manager & installer.** [WinGet](https://github.com/microsoft/winget-cli) is not ready for prime-time and [Chocolatey](https://chocolatey.org/) while has a larger database, it is too slow and harder to automate. `scoop install` a package to install an application. `update`s and `uninstall`s are straightforward too. It has even a Unix which alternative to find out path of an executable `scoop which`.
  - [scoop-completion](https://github.com/Moeologist/scoop-completion) — For CLI completion.
```posh
  scoop bucket add extras
  scoop bucket add nirsoft
  scoop install scoop-completion which autohotkey pyenv sysinternals shellexview shellmenuview rapidee lockhunter spacesniffer everything winmerge dupeguru winaero-tweaker carnac 
```
  Then to update all `scoop update *`. I am generally keeping self updating software like Firefox out of scoop, everything else is managed by scoop.

  You can install Everything from an elevated CLI, otherwise it is may raise a UAC prompt at boot. 
<!--more-->
- [which](http://gnuwin32.sourceforge.net/packages/which.htm) — **Which for Windows.** Shows full path of commands. I am not used to the PowerShell way of doing things, so I reach for a known Unix tool to quickly find out path of an executable.  
- [AutoHotKey](https://www.autohotkey.com/) — **Automation scripting language.** Easy to learn and lightweight. One example is better than a thousand words, so here is an `ahk` file to *scan with MalwareBytes Free*.
```posh
Run, "C:\Program Files\Malwarebytes\Anti-Malware\mbam.exe"
WinWait, Malwarebytes Free
ControlClick, x450 y580, Malwarebytes Free,,,, NA
```
- [pyenv](https://github.com/pyenv/pyenv) — **Python version manager.** Using multiple versions of Python at the same time is incredibly difficult. This tool just makes it possible. To make one version globally active `pyenv global` and only for current directory `pyenv local`.
- [AutoRuns](https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns) — **Startup manager.** When `msconfig` is not enough, easier to use, more powerful. Originally part of the Sysinternals suite acquired by Microsoft. 
- [ShellExView](https://www.nirsoft.net/utils/shexview.html) and [ShellMenuView](https://www.nirsoft.net/utils/shell_menu_view.html) — **Context menu editor.** ShellExView is for shell extensions (i.e. 7-Zip submenu) and ShellMenuView is for static items in right click menus.
- [RapidEE](https://www.rapidee.com/en/about) — **Environment editor.** Even though Windows 10 eased the environmental variables' management, RapidEE still has a place with its automatic invalid path check. 
- [LockHunter](https://lockhunter.com/) — **File unlocker.** In case of those nasty situations where some file or disk is locked, so you can't delete/move or safely unmount. Just use from right-click menu or drop on it.  
- Process Hacker — system monitor
- [SpaceSniffer](http://www.uderzo.it/main_products/space_sniffer/) or [WizTree](https://wiztreefree.com/): **Disk space analyzer.** SpaceSniffer's UI is cleaner, but WizTree is faster to analyze disk. I used to be a user of [WinDirStat](https://windirstat.net/) whose UI is identical to WizTree, however it is slower than both options.
- [Everything](https://www.voidtools.com/) — **Instant Search.** Alternative to Unix locate. Although this tool only locates files by name, it is instant and lightweight, while Windows Search is both resource intensive and slow. Whenever I am on a Windows desktop without Everything I just feel lost.
- [WinMerge](https://winmerge.org/) — **Directory/file diff-merge.** I am using it for recursive comparison and merge of directories. Files are, most of the time in version control, otherwise launching a text editor is simpler.
- [dupeGuru](https://dupeguru.voltaicideas.net/): **Duplicate finder.** Simple and quick. TODO: Make use of music and picture specific features advertised.
- [Winaero Tweaker](https://winaero.com/winaero-tweaker/) — **System customizer.** Widely known. Contains many tweaks for appearance and behavior of your Windows.
- [Carnac](http://code52.org/carnac/) — **Keyboard presentation.** It displays keys pressed on screen. Useful for presentations, tutorials etc.
<!-- restic 
  — crestic -->

### WSL (Windows Subsystem for Linux)
- [genie](https://github.com/arkane-systems/genie) — **Systemd in a bottle.** Systemd has become a core part of some GNU/Linux distributions, and it does not work with WSL. But for WSL2 there is a workaround, just start with `wsl genie -s` to get a systemd enable shell.

## Cross-Platform
- [ripgrep](https://github.com/BurntSushi/ripgrep) — **Regex pattern searcher.** A cross-platform alternative to Unix tool grep, to recursively search files for regex patterns. It is faster than alternatives ag, ack and grep.
- [scrcpy](https://github.com/Genymobile/scrcpy) — **PC Android display.** It is pure magic. Connect, then display and control your android device from the comfort of your PC. `scrcpy -S` to turn off android display on launch.
- [adb](https://developer.android.com/studio/command-line/adb) — **Android controller.** Backup your android, uninstall apps and many more.
- [SMPlayer](https://www.smplayer.info/) — **Video player.** Compared to [VLC](https://www.videolan.org/), [mplayer](http://www.mplayerhq.hu/design7/dload.html) was always the better player though not that popular, and [mpv](https://mpv.io/) fork is even better. Without doubt the best GUI for mpv is SMPlayer. It has OpenSubtitles.org search feature, and mpv will just play anything thrown to it more performant then any other player.
```posh
scoop bucket add jfut https://github.com/jfut/scoop-jfut.gitscoop # for smplayer 
scoop install ripgrep scrcpy adb smplayer
```

## GNU/Linux
- [tin-summer](https://github.com/vmchale/tin-summer) — **Build artifacts cleaner.** Anyone who is programming will end up huge amount of space occupied with build artifacts such as `node-modules`. Cleanup all with just `sn a`. Furthermore, it is a `du` replacement.
<!--- ncdu — disk usage
- guix -->
