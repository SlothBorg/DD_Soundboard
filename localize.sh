# delete audio dir, just in case
rm -rf audio
# make audio dir
mkdir audio
# download all the audio files, save them to the audio dir
wget --directory-prefix=audio -i Links.txt --random-wait
#run the localize python script, to replace all the urls in the html file
python3 scripts/localize.py