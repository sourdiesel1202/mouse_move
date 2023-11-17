import macmouse, time

while True:
    macmouse.move(macmouse.get_position()[0]+10,macmouse.get_position()[1]-10)
    time.sleep(45)
