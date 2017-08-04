
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests # Available from: http://docs.python-requests.org/en/master
import subprocess
import copy
import pandas

podcastData = pandas.read_csv('Podfinder-data.csv')


def make_podcast_page(terms):
    podcastList = subprocess.check_output('Rscript ../tfidf/findMostSimilarPodcast.R ' + str(terms), shell=True)
    print "postcastList: " + str(podcastList)

    split_terms = terms.split(',')

    returnString = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Divining Pod</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="shortcut icon" href="http://localhost:9000/favicon.ico">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.6.0/Chart.bundle.min.js" integrity="sha256-VNbX9NjQNRW+Bk02G/RO6WiTKuhncWI4Ey7LkSbE+5s=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.6.0/Chart.min.js" integrity="sha256-SiHXR50l06UwJvHhFY4e5vzwq75vEHH+8fFNpkXePr0=" crossorigin="anonymous"></script>
  <link rel="stylesheet" type="text/css" href="http://localhost:9000/style.css">

<script>
  function playAudio(audio) {

    var player=document.getElementById('player');
    var sourceMp3=document.getElementById('sourceMp3');
    sourceMp3.src=audio;

    if(player.paused) {
      player.load();
      player.play();
    }
    else {player.pause()}
  }
</script>

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
""" + makeButton("Contracts", split_terms) + """
""" + makeButton("HIPAA", split_terms) + """
      </div>
    </div>

  </div>
  <div>
    <div class="row section-header" >
      Recommended episodes
    </div>""" + makePodcastEntries(podcastList, split_terms) + """
  </div>
</div>

<audio id="player">
    <source id="sourceMp3" src="" type="audio/mp3">
    Your browser does not support the audio element.
</audio>

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

def makePodcastEntries(audioFile, split_terms):
  returnVal = ""
  podcast_entry_count = 0

  for rows in audioFile.split('\n'):
    podcast_entry_count += 1
    file = rows.split(',')[0]
    top_terms = rows.split(',')[2].split(' ')
    thePodcast = podcastData.loc[podcastData['fileName'] == file]
    #PodcastName,EpisodeName,PodcastTagline,PublishDate,PlayFile,TrimmedPlayFile,fileName = podcastData.loc[podcastData['fileName'] == file]

    PodcastName = thePodcast['PodcastName'].iloc[0]
    EpisodeName = thePodcast['EpisodeName'].iloc[0]
    PodcastTagline = thePodcast['PodcastTagline'].iloc[0]
    PublishDate = thePodcast['PublishDate'].iloc[0]
    PlayFile = 'http://localhost:9000/' + str(thePodcast['PlayFile'].iloc[0])
    TrimmedPlayFile = 'http://localhost:9000/' + str(thePodcast['TrimmedPlayFile'].iloc[0])
    fileName = thePodcast['fileName'].iloc[0]

    returnVal += """
    <div>
      <div class="row"><h4>""" + PodcastName + ": " + EpisodeName + """</h4></div>
      <div class="row">""" + PodcastTagline + """</div>
      <div class="row">Published: """ + PublishDate + """</div>
      <div class="row">
        <button type="button" class="btn btn-secondary" onclick="playAudio('""" + PlayFile + """')">Play</button>
        <button type="button" class="btn btn-secondary" onclick="playAudio('""" + TrimmedPlayFile + """')">Preview</button>
        <button type="button" class="btn btn-secondary" data-toggle="collapse" data-target="#demo""" + str(podcast_entry_count) + """">Details</button>
        <div id="demo""" + str(podcast_entry_count) + """" class="collapse">
<!--          <div class="container">             -->
<!--            <div class="row section-header">  -->
              Themes found in this podcast
              <div class="container filter-section">
                <div class="row text-center">
                  """ + makeButton(top_terms[0], split_terms) + """
                  """ + makeButton(top_terms[1], split_terms) + """
                  """ + makeButton(top_terms[2], split_terms) + """
                  """ + makeButton(top_terms[3], split_terms) + """
                  """ + makeButton(top_terms[4], split_terms) + """
                </div>
<!--               </div> -->
<!--            </div>    -->
          </div>
          <div>
<!--            """ + str(makeChart(podcast_entry_count)) + """ -->
          </div>
        </div>
      </div>
      <hr>
    </div>
"""

  return returnVal


def makeChart(podcast_entry_count):
  return """
<canvas id="myChart""" + str(podcast_entry_count) + """" width="400" height="400"></canvas>
<script>
var ctx = document.getElementById("myChart""" + str(podcast_entry_count) + """").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});
</script>
"""
