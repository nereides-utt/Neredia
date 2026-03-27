from pymavlink import mavutil
import time

# Connexion au port COM16 - à changer selon ta config (regarder dans le gestionnaire de périphériques)
master = mavutil.mavlink_connection('COM16', baud=57600)

# Attendre la connexion
print("Waiting for heartbeat...")
master.wait_heartbeat()
print("Connected to ArduPilot")

# Fonction pour envoyer PWM sur un servo
def set_servo(channel, pwm):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,
        channel,  # numéro du port COM du servo
        pwm,      # valeur PWM (1000-2000)
        0, 0, 0, 0, 0
    )

position_PWM = int(input("Entrez la position PWM (1000-2000) : "))
while position_PWM >0 :
    set_servo(8, position_PWM)  # M8 → direction
    print(f'Position min : {position_PWM}')
    time.sleep(4)
    position_PWM = int(input("Entrez la position PWM (1000-2000) : "))
    