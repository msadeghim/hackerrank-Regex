pat = rf'(?<!\w){word}(?!\w)'
pat = rf'((?<=\W)|^){word}((?=\W)|$)'
 
cls = '[_0-9a-zA-Z]'
pat = rf'(?<!{cls}){word}(?!{cls})'
