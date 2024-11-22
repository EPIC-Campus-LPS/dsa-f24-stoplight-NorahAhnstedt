# Lab 8 - Stoplight
## Part I - Tinkercad

- Visit https://www.tinkercad.com/
- Click Circuits > Create New Circuit
- Create a circuit to light up 3 light bulbs - *Remember each 3V coin battery is equivalent to a GPIO pin on your Raspberry Pi*
- Take a screenshot of your circuit

- [x] Take a screenshot of your circuit and upload it to this repository 
## Part II - Python3

- Redo part I with real components; however, for your power source, use GPIO pins on your Raspberry Pi. _Turn off your Pi when connecting cables to the GPIO ports._
- Create a Python script `led_stoplight.py`  to recreate the following pattern out with your LEDs - Green for 5 seconds, then Yellow for 1 second,  Red for 4 seconds, then it repeats. _Do not use the stoplight sensor, use three individual LEDs._  
- You will need to import the `GPIO` and `time` libraries for this assignment.
- Add comments to your Python script to explain how it works.
- Take a short video of your stoplight working and a clear top-down photo of your wiring

- [x] Upload `led_stoplight.py`, the video, and the photo to this repository then continue to Part II

## Part III - RBG LED  

![Pasted image 20240918085928](https://github.com/user-attachments/assets/afc83c00-95dd-4bed-a120-0daec07b2c7f)

- In a new script`rgb_stoplight.py`, repeat the previous two parts, this time using one 4 prong RGB LED, instead of 3 separate lights. This light should follow the same pattern switching from green, to yellow, to red.
- Add comments to your Python script to explain how it works.
- Take a clear top-down photo of your wiring

- [x] Upload `rgb_stoplight.py` and your photo then continue to Part IV
## Part IV - Starting with a Button

- In a new script `button_stoplight.py`, add a button or touch module to your project to start your RGB stoplight. When the button is pressed the light should light up in the green, yellow, red pattern.
- For your button module, `S` should be connected to a GPIO pin, `V` to 5V, and `G` to ground.
- In order to use a button, set the `S` pin to an input with `GPIO.setup(pin_number, GPIO.IN)`. It the button is pressed, `GPIO.input(pin_number)` will be equal to 0. If it is unpressed, `GPIO.input(pin_number)` will be equal to 1.
- Take a short video of your button starting the stoplight and the pattern appearing correctly

- [x] Upload `button_stoplight.py`  and the video to this repository then continue to Part V - Wrap Up
## Part V - Wrap Up

- Make sure all the deliverables above are  uploaded to the repository
- Answer the following questions:

1. What is a Python library and how do you include one in your script?

2. What does it mean for elements of a circuits to be in series vs. in parallel?

3. Can you create a circuit of 3 light bulbs in series? Why or why not?
- [x]

## Rubric 

_Course Content_

- 6 points - All required items are present.    
- 5 points - Task was completed, but supplementary materials are weak or missing.
  - Code is complete, but poorly communicates necessary information
- 4 points - Task was attempted, but is missing major components.    
  - Missing comments, videos/photos, or reflection questions  
- 3 points - Did not attempt or student should reattempt.  
  - Inappropriate use of AI tools.
  
_Workforce Readiness_  
  
- 4 points - Exemplified  WFR standards  
  - Language is professional.  
  - Work is clear and easy to read.
  - Used deductive reasoning guide solution.
  - Reflection on own work was thoughtful and honest.  
- 3 points - Practiced WFR standards  
  - Language is readable but not professional.  
  - Work is understandable but not completely clear.  
  - Reflection on own work was weak.  
  - Citations were not complete.
  - Format is somewhat distracting from content
- 2 points - Developing WFR standards
  - Work is unprofessional. Significant spelling or grammar errors.
  - Format is actively distracting from content
  - Did not attempt or student should reattempt.
