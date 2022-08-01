from core2d import Vector2


class TrainerSettings:


    WORLD_SIZE = 500

    OBJECT_VEL = 30 # number represents pixels per second | more then 30 senseless, because PC is not faster

    MAX_DRONE_SPEED = 10  # Maximum speed of a drone
    DRONE_SIZE = 10       # number represents pixels ( Diameter)
    DRONE_DIST = 15       # DISTANCE BETWEEN CENTER OF 2 DRONES
    MAX_RAYCAST_LEN = 100 # Maximum Length of Drone Raycast Detector

    RAYCASTS_DRONE = [
        Vector2(1, 0),
        Vector2(-1, 0),
        Vector2(0, 1),
        Vector2(0, -1),
        Vector2(1, 1),
        Vector2(-1, 1),
        Vector2(1, -1),
        Vector2(-1, -1)
    ]


    time_Waiting = 1/60
    time_scale = 5.0



