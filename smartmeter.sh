#!/bin/bash

sudo python3 datacollect.py &
sudo python3 uploaddata.py &
sudo python3 display.py &
sudo python3 instantdata.py &
