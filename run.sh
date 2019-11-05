sed -i s/"max_movie_time 0"/"max_movie_time 30"/ /etc/motion/motion.conf

nohup motion > output.log &

wget $CONFIG_URL

python3 main.py
