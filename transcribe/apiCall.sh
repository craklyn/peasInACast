EOFFILES=/Users/LeoLe/Downloads/peasInACast/podcastAudio/EOFire*/*.mp3

SPIPFILES=/Users/LeoLe/Downloads/peasInACast/podcastAudio/Smart*/*.mp3

for f in $EOFFILES
do
	curl -X POST --form "file=@$f" --form 'apikey=ab00903b-664d-4efa-9966-4c258c562145' https://api.havenondemand.com/1/api/async/recognizespeech/v1
	sleep 30
done

for s in $SPIPFILES
do
        curl -X POST --form "file=@$s" --form 'apikey=ab00903b-664d-4efa-9966-4c258c562145' https://api.havenondemand.com/1/api/async/recognizespeech/v1
        sleep 30
done 

curl -X GET https://api.havenondemand.com/1/job/status/w-eu_8bb2767c-0e10-4db3-a97f-f67e9c8edd20?apikey=ab00903b-664d-4efa-9966-4c258c562145
