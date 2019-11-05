#sed -i s/"max_movie_time 0"/"max_movie_time 90"/ /etc/motion/motion.conf

wget $CONFIG_URL

nohup python3 main.py > output.log &

motion
