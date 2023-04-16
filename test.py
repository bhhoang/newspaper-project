
from selectolax.parser import HTMLParser
html  = '<?xml version="1.0"?>'\
'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">'\
'<html><head><meta name="qrichtext" content="1"/><style type="text/css">'\
'p, li { white-space: pre-wrap; }'\
'</style></head><body style=" font-family:\'Times\'; font-size:12pt; font-weight:400; font-style:normal;"><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="https://static.wikia.nocookie.net/oshi_no_ko/images/b/b0/AiHoshino.png/revision/latest?cb=20210820021211" alt="Ai Hoshino | Oshi no Ko Wiki | Fandom"/></p></body></html> '

test = "<p>Europe is a continent full of history, culture and natural beauty. Here are some of the best places to visit in Europe:</p><ul><li><img src='https://unsplash.com/photos/4m1VwvOY5XU' alt='Paris, France'></li><li><img src='https://unsplash.com/photos/7JX0-bfiuxQ' alt='Venice, Italy'></li><li><img src='https://unsplash.com/photos/8vJgUPTZJ9M' alt='Athens, Greece'></li><li><img src='https://static.wikia.nocookie.net/oshi_no_ko/images/b/b0/AiHoshino.png/revision/latest?cb=20210820021211' alt='Ai Hoshino | Oshi no Ko Wiki | Fandom'></li></ul>"
tree = HTMLParser(test)
for out in tree.css('img'):
    print(out.attributes['src'])