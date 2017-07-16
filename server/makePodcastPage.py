#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests # Available from: http://docs.python-requests.org/en/master
import subprocess
import copy

def make_podcast_page(terms):
    podcastList = subprocess.check_output('Rscript ../tfidf/findMostSimilarPodcast.R ' + str(terms), shell=True)
    print "postcastList: " + str(podcastList)

    split_terms = terms.split(',')

    returnString = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="shortcut icon" href="http://localhost:9000/favicon.ico">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <link rel="stylesheet" type="text/css" href="http://localhost:9000/style.css">
</head>


<body>
<img src="http://localhost:9000/images/IphoneCutOut2.png" id="overlay"/>

<div class="head-image">
    <h1>Business</h1>
</div>

<div class="container">
  <div class="row section-header">
    Narrow down by theme

    <div class="container filter-section">
      <div class="row text-center">
""" + makeButton("Business", split_terms) + """
""" + makeButton("Income", split_terms) + """
""" + makeButton("Passive", split_terms) + """
""" + makeButton("Advertising", split_terms) + """
""" + makeButton("Startup", split_terms) + """
""" + makeButton("Marketing", split_terms) + """
""" + makeButton("Taxes", split_terms) + """
""" + makeButton("Hiring", split_terms) + """
""" + makeButton("Management", split_terms) + """
        <br>
""" + makeButton("Investors", split_terms) + """
""" + makeButton("Leasing", split_terms) + """
""" + makeButton("Distributing", split_terms) + """
""" + makeButton("Production", split_terms) + """
""" + makeButton("Insurance", split_terms) + """
""" + makeButton("Safety", split_terms) + """
""" + makeButton("Hiring", split_terms) + """
""" + makeButton("Contracts", split_terms) + """
""" + makeButton("HIPAA", split_terms) + """
      </div>
    </div>

  </div>
  <div>
    <div class="row section-header" >
      Recommended episodes
    </div>
    <div class="row"><h4>SPI 265: Shane and Jocelyn Sams and Their Awesome Advertising Strategy</h4></div>
    <div class="row">The smart passive income podcast</div>
    <div class="row">45 mins - May 10, 2017</div>
    <div class="row">
      <button type="button" class="btn btn-secondary">Play</button>
      <button type="button" class="btn btn-secondary">Preview</button>
      <button type="button" class="btn btn-secondary">Save</button>
    </div>
    <hr>
    <div class="row"><h4>SPI 272: Starting and Running a Business as a Couple Featuring the Bakers</h4></div>
    <div class="row">The smart passive income podcast</div>
    <div class="row">43 mins - June 28, 2017</div>
    <div class="row">
      <button type="button" class="btn btn-secondary">Play</button>
      <button type="button" class="btn btn-secondary">Preview</button>
      <button type="button" class="btn btn-secondary">Save</button>
    </div>
    <hr>
    <div class="row"><h4>SPI 272: Starting and Running a Business as a Couple Featuring the Bakers</h4></div>
    <div class="row">The smart passive income podcast</div>
    <div class="row">43 mins - June 28, 2017</div>
    <div class="row">
      <button type="button" class="btn btn-secondary">Play</button>
      <button type="button" class="btn btn-secondary">Preview</button>
      <button type="button" class="btn btn-secondary">Save</button>
    </div>
    <hr>
    <div class="row"><h4>SPI 272: Starting and Running a Business as a Couple Featuring the Bakers</h4></div>
    <div class="row">The smart passive income podcast</div>
    <div class="row">43 mins - June 28, 2017</div>
    <div class="row">
      <button type="button" class="btn btn-secondary">Play</button>
      <button type="button" class="btn btn-secondary">Preview</button>
      <button type="button" class="btn btn-secondary">Save</button>
    </div>
    <hr>
    <div class="row"><h4>SPI 272: Starting and Running a Business as a Couple Featuring the Bakers</h4></div>
    <div class="row">The smart passive income podcast</div>
    <div class="row">43 mins - June 28, 2017</div>
    <div class="row">
      <button type="button" class="btn btn-secondary">Play</button>
      <button type="button" class="btn btn-secondary">Preview</button>
      <button type="button" class="btn btn-secondary">Save</button>
    </div>
    <hr>
    <div class="row"><h4>SPI 272: Starting and Running a Business as a Couple Featuring the Bakers</h4></div>
    <div class="row">The smart passive income podcast</div>
    <div class="row">43 mins - June 28, 2017</div>
    <div class="row">
      <button type="button" class="btn btn-secondary">Play</button>
      <button type="button" class="btn btn-secondary">Preview</button>
      <button type="button" class="btn btn-secondary">Save</button>
    </div>
    <hr>
    <div class="row"><h4>SPI 272: Starting and Running a Business as a Couple Featuring the Bakers</h4></div>
    <div class="row">The smart passive income podcast</div>
    <div class="row">43 mins - June 28, 2017</div>
    <div class="row">
      <button type="button" class="btn btn-secondary">Play</button>
      <button type="button" class="btn btn-secondary">Preview</button>
      <button type="button" class="btn btn-secondary">Save</button>
    </div>
    <hr>
    <div class="row"><h4>SPI 272: Starting and Running a Business as a Couple Featuring the Bakers</h4></div>
    <div class="row">The smart passive income podcast</div>
    <div class="row">43 mins - June 28, 2017</div>
    <div class="row">
      <button type="button" class="btn btn-secondary">Play</button>
      <button type="button" class="btn btn-secondary">Preview</button>
      <button type="button" class="btn btn-secondary">Save</button>
    </div>
    <hr>
    <div class="row"><h4>SPI 272: Starting and Running a Business as a Couple Featuring the Bakers</h4></div>
    <div class="row">The smart passive income podcast</div>
    <div class="row">43 mins - June 28, 2017</div>
    <div class="row">
      <button type="button" class="btn btn-secondary">Play</button>
      <button type="button" class="btn btn-secondary">Preview</button>
      <button type="button" class="btn btn-secondary">Save</button>
    </div>
    <hr>
    <div class="row"><h4>SPI 272: Starting and Running a Business as a Couple Featuring the Bakers</h4></div>
    <div class="row">The smart passive income podcast</div>
    <div class="row">43 mins - June 28, 2017</div>
    <div class="row">
      <button type="button" class="btn btn-secondary">Play</button>
      <button type="button" class="btn btn-secondary">Preview</button>
      <button type="button" class="btn btn-secondary">Save</button>
    </div>
  </div>
</div>

</body>
</html>
"""
    return returnString


def makeButton(buttonName, currentTerms):
    newTerms = copy.deepcopy(currentTerms)
    button_active = False

    returnString  = '        <div class="inline-button"><a href="http://localhost:8080/'
    if buttonName in newTerms: 
      newTerms.remove(buttonName)
      button_active = True
    else:
      newTerms.append(buttonName)
    returnString += ",".join(newTerms) 
    returnString += '" class="btn '
    if button_active: 
      returnString += 'btn-primary btn-sm active'
    else:
      returnString += 'btn-secondary btn-sm'
    returnString += '">' + buttonName + '</a></div>'
    return returnString
