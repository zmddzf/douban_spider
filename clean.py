# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:38:24 2018

@author: zmddzf
"""

import re
import jieba
class clean:
    """
    Clean the sentence.
    
    Attribute:
        filter_punctuation: filt the punctuation in the sentence.
        filter_emoji: filt the emoji in the sentence.
        wordcut: cut sentence to each single word.
        
    """
    def __init__(self, sent):
        self.sent = sent
        
    def filter_punctuation(self):
        afterfilt = re.sub("[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%\【】\，\、\。\·\；\：\‘\“\”\']", "", self.sent)
        self.sent = afterfilt
        return afterfilt
        
    def filter_emoji(self):
        restr = ''
        try:
            co = re.compile(u'[\U00010000-\U0010ffff]')
        except re.error:
            co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        self.sent = co.sub(restr, self.sent)
        return co.sub(restr, self.sent)
    
    def wordcut(self):
        wordlist = list(jieba.cut(self.sent))
        outstr = ''
        for wd in wordlist:
            outstr += wd
            outstr += ' '
        self.sent = outstr.strip()
        return outstr.strip()
        
    
        
    