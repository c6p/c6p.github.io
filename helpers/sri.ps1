hugo --minify
(rg -oIN '<script.*?(sha\d{3}-.{43}=)\"' -r '''$1''' public | sort -unique) -join ' ' | out-file -encoding ASCII -noNewline data/hash/script.txt 
# (rg -oIN '<link.*?(sha\d{3}-.{43}=)\"' -r '''$1''' public | sort -unique) -join ' ' | out-file -encoding ASCII -noNewline data/hash/style.txt