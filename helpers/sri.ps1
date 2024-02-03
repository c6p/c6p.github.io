hugo --minify
(rg -oIN '<script.*?(sha\d{3}-.{43}=)\".*?>[^\n<>]+?</script>' -r '''$1''' public | sort -unique && # sw.js 
"sha256-XPQOTL5eFJ25siodk2WHVt/XrYkMsTAhKXSn/xGmbpI=") -join ' ' | out-file -encoding ASCII -noNewline data/inline_script_hash.txt 
(rg -oIN '<script.*?src=\"?(http.*?\.js)[ \">]' -r '$1' public | sort -unique) -join ' ' | out-file -encoding ASCII -noNewline data/external_script_source.txt