def security(door_open,window_open,motion_dected,alarm_deactivated):
    a = ((door_open and not(alarm_deactivated)) == True)
    b = ((window_open and not(alarm_deactivated)) == True)
    c = ((motion_dected and not(alarm_deactivated)) == True)
    return a or b or c

door_open = input() == "True"
window_open = input() == "True"
motion_dected = input() == "True"
alarm_deactivated = input() == "True"

print(security(door_open,window_open,motion_dected,alarm_deactivated))