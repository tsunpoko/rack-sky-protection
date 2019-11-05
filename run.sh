sed -i s/"max_movie_time 0"/"max_movie_time 30"/ /etc/motion/motion.conf

nohup motion > output.log &

python3 main.py
