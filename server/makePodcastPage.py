#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests # Available from: http://docs.python-requests.org/en/master

def make_podcast_page(call_id):
    returnString = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
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
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">New business</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Passive Income </button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Advertising </button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Startup</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Marketing</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Taxes</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Hiring</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Management</button></div>
        <br>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Finding investors</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Leasing</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Distributing</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Production</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Insurance</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Safety</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Hiring</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">Contracts</button></div>
        <div class="inline-button"><button type="button" class="btn btn-secondary btn-sm">HIPAA</button></div>
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
