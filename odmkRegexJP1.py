#-*- coding: utf-8 -*-

"""
odmkRegexJP1

Test script using Python Regular Expressions, 're' library.

Using Python to process Japanese text

"""

import re
import string
import sys
import pprint
import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text

#from nltk.corpus import knbc ??wtf


#//////////////////////////////////////////////////////////////////////////////
# begin: set encoding
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

sys.getdefaultencoding()
reload(sys)     #Important!! can't set encoding without reloading...
sys.setdefaultencoding('utf-8')
sys.getdefaultencoding()


#//////////////////////////////////////////////////////////////////////////////
# end: set encoding
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#//////////////////////////////////////////////////////////////////////////////
# begin: define functions
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#special print func for Jp text
def pp(obj):
    pp = pprint.PrettyPrinter(indent=4, width=160)
    str = pp.pformat(obj)
    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),16)), str)


#//////////////////////////////////////////////////////////////////////////////
# end: define functions
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



print '\n\n\n'
print '*---------------------------------------------------------------------*'
print "%s で %s" % (u"パイソン", u"自然言語処理")

print '*---------------------------------------------------------------------*'

data = {u"スクリプト言語":
        {u"Perl": u"パール", u"Python": u"パイソン", u"Ruby": u"ルビー"},
    u"関数型言語":
        {u"Erlang": u"アーラング", u"Haskell": u"ハスケル", u"Lisp": u"リスプ"}
    }

print data
print '\n'
print '*---------------------------------------------------------------------*'
print pp(data)


print '\n'
print '*---------------------------------------------------------------------*'
jk = '深入 Python'
print ('J/E Mixed String = '+str(jk))



#define Japanese punctuation tokens
jp_sent_tokenizer = nltk.RegexpTokenizer(u'[＾ 「」　！　？　。　]*[！　？　。]')

#define J-unicode characters
jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[＾ぁ-んァ-ンー￥u4e00-\u9FFF]+)')


ginga = PlaintextCorpusReader("C:\\nltk_data", r'gingatetsudono_yoru.txt', 
                              encoding='utf-8', para_block_reader=read_line_block, 
                              sent_tokenizer=jp_sent_tokenizer, 
                              word_tokenizer=jp_chartype_tokenizer)




#jk_utf8_enc = jk.encode('utf8')
#jk_utf8_dec = jk_utf8_enc.decode('utf8')


#print ('J/E Mixed UTF8 Encode = '+str(jk_utf8_enc))
#print ('J/E Mixed UTF8 Decode = '+str(jk_utf8_dec))

# #doesn't work with WINXP console coded (default=cp932)
# print ('Hiragana ALL chr:')
# for i in range(0x3040, 0x30a0): print(chr(i), end='')

#print ('Katakana ALL chr:')
#for i in range(0x30a0, 0x3100):
#    print chr(i)

# CJK Chinese Japanese Korean
# print ('CJK Unified Ideographs 例:')
# for i in range(0x4e00, 0x4f00): print(chr(i), end='')


#k = re.compile(chr(0x3042))
#res = k.search('あ')
#
#print ('Match あ using a RE: chr(0x3042)')
#print ('Matched Result String = '+str(res.group()))






#basic regex processing
# ** metacharacters **
# . ^ $ * ? {} [] \ | ()



#print '\n\n\n'
#print '*---------------------------------------------------------------------*'
#ztxt = '%All 418 cats are Grey, #93Cats, $93_Cats, ?93_Cats'
#print 'original text string:\n'
#print '"'+ztxt+'"'+'\n\n'
#
#print '*---------------------------------------------------------------------*'
#
##basic string match
#print '::basic regex::\n'
#mtc1 = re.match(r'%All 418 cats are Grey, #93Cats, \$93_Cats, \?93_Cats',ztxt)
#print 'Exact text match = '+str(mtc1.group())   #mtc1.group(0) = same
#
##Single char search: [A-Za-z] matches any 1 digit from 0-9
#mtc1 = re.search(r'[A-Za-z]',ztxt)
#print 'Single char search [A-Za-z] = '+str(mtc1.group())
#
##Specific char search: [c] matches c
#mtc1 = re.search(r'[c]',ztxt)
#print 'Specific char search [c] = '+str(mtc1.group())
#
##basic string search
#mtc1 = re.search(r'418 cats',ztxt)
#print 'Basic string search = '+str(mtc1.group())+'\n\n'
#
#print '*---------------------------------------------------------------------*'
#
#
#print '::more regex::\n'
#
##bracket OR - [_3]Cats
#mtc1 = re.search(r'[_3]Cats',ztxt)
#print 'bracket OR example [_3]Cats = '+str(mtc1.group())
#
##Ignore Case -> use re.IGNORECASE, or re.I
#mtc1 = re.search(r'grey',ztxt,re.I)
#print 'String search w IGNORECASE = '+str(mtc1.group())
#
##Specific char search plus 1 or more (anything) that follows: [c] matches c
#mtc1 = re.search(r'[c].+',ztxt)
#print 'char search plus 1 or more [c].+ = '+str(mtc1.group())
#
##Specific char search plus at least 0, at most 12 chars (anything, until end of line)
#mtc1 = re.search(r'[c].{0,12}',ztxt)
#print 'char search plus 0 to 12 chars [c].{0,12} = '+str(mtc1.group())
#
##Specific char search plus two char: [c] matches c
#mtc1 = re.search(r'[c].{2}',ztxt)
#print 'char search plus two char [c].{2} = '+str(mtc1.group())
#
##A char plus one or more characters: [A-Za-z]{2,}
#mtc1 = re.search(r'[A-Za-z]{1,}',ztxt)
#print 'A char plus one or more char [A-Za-z]{1,} = '+str(mtc1.group())+'\n\n'
#
##Single digit search: [0-9] matches any 1 digit from 0-9
#mtc1 = re.search(r'[0-9]',ztxt)
#print 'Single digit search [0-9]= '+str(mtc1.group())
#
##Multiple digit search: [0-9]+ matches any digits
#mtc1 = re.search(r'[0-9]+',ztxt)
#print 'Multi digit search = '+str(mtc1.group())
#
##Multiple digit search: \d+ matches any digits
#mtc1 = re.search(r'\d+',ztxt)
#print 'Multi digit search ALT= '+str(mtc1.group())
#
##Exactly 2 digit search: [0-9]+ matches any digits
#mtc1 = re.search(r'[0-9]{2}',ztxt)
#print 'Exactly 2 digit search = '+str(mtc1.group())
#
##Exactly 2 digit search: [0-9]+ matches any digits
#mtc1 = re.search(r'\d{2}',ztxt)
#print 'Exactly 2 digit search ALT= '+str(mtc1.group())
#
##Exactly 2 digit search: \d+ matches any digits
#mtc1 = re.search(r'\d{2}',ztxt)
#print 'Exactly 2 digit search ALT= '+str(mtc1.group())+'\n\n'
#
#print '*---------------------------------------------------------------------*'
#
##Not Matching
#print '::more regex::\n'
#
##Non-digit search: [^0-9]+ matches any non-digits
#mtc1 = re.search(r'[^0-9]+',ztxt)
#print 'Non-digit search= '+str(mtc1.group())
#
##Match without using ?
#mtc1 = re.search(r'93_Cats',ztxt)
#print 'Non-? search= '+str(mtc1.group())
#
##Match using ? = zero or one occurance
#mtc1 = re.search(r'93_?Cats',ztxt)
#print 'Use ? search= '+str(mtc1.group())
#
##Match using | (OR) - returns first match found!
#mtc1 = re.search(r'(93_Cats)|(93Cats)',ztxt)
#print 'Search using | (OR)= '+str(mtc1.group())
#
##Match using \w = word characters :: [A-Za-z0-9]
#mtc1 = re.search(r'\w',ztxt)
#print 'Use \w same as [A-Za-z0-9_]= '+str(mtc1.group())
#
##Match using \W = non-word characters :: [^A-Za-z0-9]
#mtc1 = re.search(r'\W',ztxt)
#print 'Use \W same as [^A-Za-z0-9_]= '+str(mtc1.group())+'\n\n'
#
#print '*---------------------------------------------------------------------*'
#
##special characters, etc
#print '::Special Character searches::\n'
#
##Specific special character search
#mtc1 = re.search(r'\$',ztxt)
#print 'Special char search \$ = '+str(mtc1.group())
#
##Specific special character search using 'character class'
#mtc1 = re.search(r'[$]',ztxt)
#print 'Char class - char search [$] = '+str(mtc1.group())+'\n\n'
#
#print '*---------------------------------------------------------------------*'
#
##Grouping
#print '::Grouping string searches::\n'
#
#mtc1 = re.search(r'(\d*) (cats) are (.{4})',ztxt)
#print 'Multi Group; regex = (\d*) (cats) are (.{4})'
#print 'result mtc1.group() = '+str(mtc1.group())
#print 'result mtc1.group(0) = '+str(mtc1.group(0))
#print 'result mtc1.group(1) = '+str(mtc1.group(1))
#print 'result mtc1.group(2) = '+str(mtc1.group(2))
#print 'result mtc1.group(3) = '+str(mtc1.group(3))+'\n'
#
#
#mtc1 = re.search(r'(\w{3}) \d* (cats) (\w{3}) (.{4})',ztxt)
#print 'Multi Group; regex = (\w{3}) \d* (cats) (\w{3}) (.{4})'
#print 'result mtc1.group() = '+str(mtc1.group()) 
#print str(mtc1.group(1))+' '+str(mtc1.group(2))+' '+str(mtc1.group(3))+' '+str(mtc1.group(4))+'\n\n'
#
#print '*---------------------------------------------------------------------*'
#
##Compiling
#
#print '::Compiling Examples::\n'
#p = re.compile('[a-zA-Z]+')
#print 'Compiled Pattern = [a-zA-Z]+'
#print 'Compiled Pattern object = '+str(p)+'\n'
#
#res = p.search('::: matchedKword :::')
#print 'Input String = ::: matchedKword :::'
#print 'Matched object = '+str(res)
#print 'Matched Pattern = '+str(p.pattern)
#print 'Matched Result = '+str(res.group())+'\n'
#
#
#p = re.compile(r'bluecats', re.I)
#print 'Compiled Pattern = bluecats'
#mtc1 = p.search(ztxt)
#if mtc1:
#    print 'Match found: '+str(mtc1.group())+'\n'
#else:
#    print 'No Match\n'
#
#p = re.compile(r'(\w{3}) \d* (cats) (\w{3}) (.{4})')
#print 'Compiled Pattern = (\w{3}) \d* (cats) (\w{3}) (.{4})'
#mtc1 = p.search(ztxt)
#if mtc1:
#    print 'Match found: '+str(mtc1.group())+'\n'
#else:
#    print 'No Match\n'
#    
#print 'Using findall (Output is a List!!)'   
#p = re.compile('[a-zA-Z]+')
#print 'Compiled Pattern = [a-zA-Z]+'
#mtc1 = p.findall(ztxt)
#print 'findall Results List:'
#print mtc1  
#    
#p = re.compile('\d+')
#print '\nCompiled Pattern = \d+'
#mtc1 = p.findall(ztxt)
#print 'findall Results List:'
#print mtc1
#
#print '*---------------------------------------------------------------------*'
