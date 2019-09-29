# StratosGWSMK1



StratosGWSMK1

Control one BRUSHLESS motor + raspicam streaming

STEPS

01-start the server on the raspberry

02-start the client on the desktop

03-open a new terminal in raspberry and launch this comand : raspivid -t 0 -b 2000000 -fps 30 -w 640 -h 480 -o - -rot 180 | nc -p 1904 -u 192.168.1.62 5000

ENJOY

STRATOS 2019
