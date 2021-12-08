
 ![Alt text](Smart_Door.png?raw=true "Title")
# Smart Door to Contribute to Limiting The Spread of the Corona Virus


This is a smart door project to limit the spread of Covid-19 using a python language.


## Downloud code 
 - Download from GitHub https://github.com/nowemir/SmartDoor

## Install dependencies 

- First you have to install Python from https://www.python.org/downloads
  
- To RUN facemask detection code You'll need to
  
     - install openCV
       ````
       $ pip install opencv-python
     - install sklearn
       ````
       $ pip install -U scikit-learn 
    - enable the camera on the raspberry pi using this command
      ````
      $ sudo raspi-config 
      ````
      - then enable the camera from the interface (reboot after enabled the camera )
  
    
- To run the MLX90614 Infrared Thermal Sensor You'll need to
  -  install the package "Adafruit Blinka"
  - install the package "adafruit-circuitpython-mlx90614"
  - enable i2c on the raspberry pi using this command
    ````
    $ sudo raspi-config   
    ````
    - then enable i2C from the interface (reboot after enabling i2C
    

## Run the code 

- First you have to run the dataset(withmask\withoutmask).py to collect faces (with and without face mask)
- Run main.py .. the project will work


   


