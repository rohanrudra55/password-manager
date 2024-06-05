#!/usr/bin/python3
import os

# Suppress TensorFlow INFO and WARNING messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from src import menu

if __name__ == "__main__":
    os.system('pg_ctl -D database stop')
    os.system('pg_ctl -D database -l logfile.log start')
    menu.manager_system()
    os.system('clear')
    os.system('pg_ctl -D database stop')

