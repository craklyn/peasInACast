#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests # Available from: http://docs.python-requests.org/en/master

def make_podcast_page(call_id):
    returnString = """
<!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
<HTML>
   <HEAD>
      <TITLE>
         A Small Hello 
      </TITLE>
   </HEAD>
<BODY>
   <H1>Hi</H1>
   <P>This is very minimal "hello world" HTML document.</P> 
</BODY>
</HTML>
"""
    return returnString
