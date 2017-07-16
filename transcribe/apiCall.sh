EOFFILES=/Users/LeoLe/Downloads/peasInACast/podcastAudio/EOFire*/*.mp3

SPIPFILES=/Users/LeoLe/Downloads/peasInACast/podcastAudio/Smart*/*.mp3

FREAKFILES=/Users/LeoLe/Downloads/peasInACast/podcastAudio/Freak*/*.mp3

HOWFILES=/Users/LeoLe/Downloads/peasInACast/podcastAudio/How*/*.mp3

MASTERFILES=/Users/LeoLe/Downloads/peasInACast/podcastAudio/Masters*/*.mp3

ONLINEFILES=/Users/LeoLe/Downloads/peasInACast/podcastAudio/Online*/*.mp3

STUFFFILES=/Users/LeoLe/Downloads/peasInACast/podcastAudio/Stuff*/*.mp3


for e in $EOFFILES
do
	echo "Now handling file $e"
	curl -X POST --form "file=@$e" --form 'apikey=07d4909b-f2a7-40ec-9534-75cd0237e8c4' https://api.havenondemand.com/1/api/async/recognizespeech/v1
	sleep 30
done

for s in $SPIPFILES
do
	echo "Now handling file $s"
        curl -X POST --form "file=@$s" --form 'apikey=07d4909b-f2a7-40ec-9534-75cd0237e8c4' https://api.havenondemand.com/1/api/async/recognizespeech/v1
        sleep 30
done 

for f in $FREAKFILES
do
        echo "Now handling file $f"
        curl -X POST --form "file=@$f" --form 'apikey=07d4909b-f2a7-40ec-9534-75cd0237e8c4' https://api.havenondemand.com/1/api/async/recognizespeech/v1
        sleep 30
done

for h in $HOWFILES
do
        echo "Now handling file $h"
        curl -X POST --form "file=@$h" --form 'apikey=07d4909b-f2a7-40ec-9534-75cd0237e8c4' https://api.havenondemand.com/1/api/async/recognizespeech/v1
        sleep 30
done

for m in $MASTERFILES
do
        echo "Now handling file $m"
        curl -X POST --form "file=@$m" --form 'apikey=07d4909b-f2a7-40ec-9534-75cd0237e8c4' https://api.havenondemand.com/1/api/async/recognizespeech/v1
        sleep 30
done

for o in $ONLINEFILES
do
        echo "Now handling file $o"
        curl -X POST --form "file=@$o" --form 'apikey=07d4909b-f2a7-40ec-9534-75cd0237e8c4' https://api.havenondemand.com/1/api/async/recognizespeech/v1
        sleep 30
done

for t in $STUFFFILES
do
        echo "Now handling file $t"
        curl -X POST --form "file=@$t" --form 'apikey=07d4909b-f2a7-40ec-9534-75cd0237e8c4' https://api.havenondemand.com/1/api/async/recognizespeech/v1
        sleep 30
done


curl -X GET https://api.havenondemand.com/1/job/status/w-eu_8bb2767c-0e10-4db3-a97f-f67e9c8edd20?apikey=07d4909b-f2a7-40ec-9534-75cd0237e8c4
