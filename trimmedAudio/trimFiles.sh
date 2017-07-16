FILES=../podcastAudio/*/*.mp3
for f in $FILES
do
  baseFileName=`basename "$f"`
  echo sox \"$f\" \"trimmed_$baseFileName\" trim 10:00 10
done
