from core2d import Vector2

class TrainerSettings:


    WORLD_SIZE = 500
    WORLD_DIAG = WORLD_SIZE*1.41421356237

    MINIMUM_OBJECTIVE_DIST = 150

    OBJ_SPEED = 15

    DRONENUM = 1


    MAX_DRONE_SPEED = 20  # Maximum speed of a drone
    DRONE_SIZE = 10       # number represents pixels ( Diameter)
    DRONE_DIST = 30       # DISTANCE BETWEEN CENTER OF 2 DRONES
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


    update_time = 1/30
    time_scale = 4.0
    exec_time = 25.0



