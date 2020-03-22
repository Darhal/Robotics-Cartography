
# Import everthing we need:
# Import bins, Ultasonicsensor, touchsensor, ColorSensor
from ev3dev.auto import INPUT_1, INPUT_2, INPUT_3, INPUT_4, \
    OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, \
    UltrasonicSensor, TouchSensor, ColorSensor

from RobotMotor import * # Import Robot Motor class to handle the motors
from USensor import * # Import UltraSound sensor class
from SensorMotor import * # Import Sensor Motor class (the class responsible for rotating the middle motor)
from Image import * # Import the image class that uses pygame

"""
@class: Robot
@brief: Robot class is the main class that is going to intilize everything needed for the robot to start
    exploring his surrounding 
"""
class Robot:
    """
        @function: constructor
        @brief: Intilize the robot class and make it prepared to explore
    """
    def __init__(self):
        """
            Intilize RobotMotor, SensorMotor, UltrasoundSensor, the TouchSensor and all the other necessary components
            for the robot then set its position to (0, 0)
        """
        self.moteur = RobotMotor(5.5, 14.0, OUTPUT_A, OUTPUT_D) # Intilize both motors
        self.sensor = USensor() # Intilize Ultrasound sensor
        self.ts = TouchSensor() # Intilize TouchSensor
        self.sensor_motor = SensorMotor() # Initlize SensorMotor that is will be responsible to rotate the ultra sound sensor
        self.is_running = False # Is running boolean
        self.cool_down_time = 1.0 # the cooldown time for the program to sleep at each iteration
        self.posx = 0 # Set position X to 0
        self.posy = 0 # Set position Y to 0
        self.img = Image("explore.png", 1028, 1028) # Create the result image thats gonna be filled during exploring
        self.sensor_dir = 1 # Sensor state either (0:left, 1:middle, 2:right), iniltized to look front
        self.obstacles = [] # Array of arrays containing obstacles


    """
        @function: start
        @brief: when called the robot will start exploring his surrounding to draw the map
    """
    def start(self):
        self.moteur.go_forwards() # Start the motor and advance forward
        # print("* Going forward")
        dist = self.sensor.get_distance() # Get intial distance
        # print("TouchSensor: "+str(self.ts.value()))

        while not self.ts.value(): # While the press button isn't pressed
            self.loop(dist) # Run the loop function that will handle all the logic
            dist = self.sensor.get_distance() # Update distance at each iteration

        self.shutdown()


    """
        @function: loop
        @brief: handle all the logic at each iteration according the current state
    """
    def loop(self, dist):
        self.posy += 1 # Advance in the y direction
        
        # print("Distance of USensor: %0.2f"%dist) # Print distance for debugging
        if (dist < 30.0): # if distance is less than 30 cm away
            self.handleObstacle() # call the handle obstacle function
        else:
            self.img.point((self.posx, self.posy), (0, 255, 0)) # mark this point as visited in the picture by putting green pixel

        # Update and rotate the sensor direction:
        self.rotateSensor()

        # Print current position for debugging purposes
        # print("* My Position is : (%.2f, %.2f)" % (self.posx, self.posy))
        sleep(self.cool_down_time) # Wait for the cooldown to expire to do another iteration

    """
        @function: rotateSensor
        @brief: handle sensor rotation to cover the 180 degrees field of view in the front
    """
    def rotateSensor(self):
        if (self.sensor_dir == 0): #  if the sensor dir is left
            self.sensor_motor.stop() # stop the motor
            sleep(0.1) # sleep for a little bit
            self.sensor_motor.turn_right(None, 20) # turn it to the right to face the front
            # print("* Turning sensor to the middle") # debug output
        elif (self.sensor_dir == 1): # if the sensor dir is in the middle
            self.sensor_motor.stop() # stop the motor
            sleep(0.1) # sleep for little bit
            self.sensor_motor.turn_right(None, 20) # turn the motor to the right
            # print("* Turning sensor to the right") # Debug message
        elif (self.sensor_dir == 2): # if the sensor dir is the left
            self.sensor_motor.stop() # stop the motor
            sleep(0.1) # sleep for little bit
            self.sensor_motor.turn_left(None) # rotate the motor to the left
            # print("* Turning sensor to the left") # debug message
        
        # Increment and do modulo 3 to no go out of our 3 states (left, middle, right)
        self.sensor_dir =  (self.sensor_dir + 1) % 3 

    """
        @function: handleObstacle
        @brief: handle the logic when the robots sees an obstacle
    """
    def handleObstacle(self):
        if (self.sensor_dir == 0): # if the sensor is to the left
            # print("* Handling obstacle to the left")  # debug message
            self.addObstacle((self.posx, self.posy - 1)) # add obstacle to the table with the right coordinates
        elif (self.sensor_dir == 1):
            # print("* Handling obstacle to the middle")  # debug message to the table
            self.addObstacle((self.posx+1, self.posy)) # add obstacle to the table with the right coordinates
        elif (self.sensor_dir == 2):
            # print("* Handling obstacle to the right")  # debug message to the table
            self.addObstacle((self.posx, self.posy+1)) # add obstacle to the table with the right coordinates
    
    """
        @function: addObstacle
        @brief: add obstacles coordinate
    """
    def addObstacle(self, pos):
        if((self.posx, self.posy - 1) not in self.obstacles): # if the coordinates are not already in onstacles then
            self.obstacles.append((self.posx, self.posy - 1)) # add to obstacles
        else:
            # print("deja enregistré") # print debug messages
            pass

    """
        @function: stop
        @brief: stop all motors
    """
    def stop(self):
        self.moteur.stop() # stop motor
        self.sensor_motor.stop() # stop sensor motor

    """
        @function: shutdown
        @brief: shutdown robot
    """
    def shutdown(self):
        # print("* Shutting down") # debug output
        self.is_running = False # put is running state is false
        self.stop() # stop all motors
        self.img.save() # save the result image