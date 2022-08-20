# MilestoneFullStack
## Introduction
This business case will show how our project will deal with the current business concerns, 
the possible advantage of the project, and recommendations and justification of the project. 
The following case will also talk through the project performance, goals, assumptions, limitations and alternative options. 
Because of the increasing expense of evaluating car loss by humans, our car insurance company has to develop an AI application 
that is available to recognise and detect the car damages automatically in a web application.  
Due to the panadamic, the human force is demanding and not all of our staff can work in the office to check the damaged cars of the clients. 
In order to solve this program, we are trying to develop an AI web application where the client can take a picture of their damaged car and our AI will detect and categorize the type of damage.  
Also, the insurance companies take a long time to process claims, they take time to process even a small damage to the car by human judgment. 
As traveling may not be convenient for all clients, just getting information from the description of the damaged car may not be accurate to estimate the claim. 
In order to solve this problem, the AI can process a faster and a more accurate claim.


## Run the application on docker
* The docker image yolov5 doesn't work on apple M1 arm64 laptop.
1) Download 4 models from [Model1_Damage_or_not](https://drive.google.com/file/d/1iKPMKf4eJMhx6b4sKxtQ13uoakAsJZAd/view?usp=sharing), [Model2_Severity](https://drive.google.com/file/d/1eryXt8SGz9zTerZBTinBFZ9_LnUiNmpE/view?usp=sharing), [Model3_Locations](https://drive.google.com/file/d/1KxYQMYQYmQ5Cmb4grM-LqzVz42DrUF7j/view?usp=sharing), [YOLOv5](https://drive.google.com/file/d/1fTkUxzRcOpmucb8FfRmYdUj2ljL9m0BF/view?usp=sharing)
2) docker build -t app .
3) docker images // Verify the new image
4) docker run -dp 8000:5000 --name main app
5) docker ps -all // Verify the new container
6) Access localhost:8000 to upload your car damage picture.

## Local Installation
Python: 3.7.13

### Create a virtual env
python -m venv py3713

pip install -r requirements.txt

### Run the application locally in Pycharm
Run app.py

Select an image and click submit button

You can see a sample result. Currently, it is a static image 'static/result.png'

## Run the application on Docker
* docker images //Show all the images locally
* docker ps -all // Show all the containers locally
* docker rm <container_id> // Remove a container
* docker rmi <image_id> // Remove a docker image
* docker build -t milestone . // Build an image named 'milestone'
* docker run -dp 8000:5000 --name main milestone // Run a docker container named main with image 'milestone'

[Final Report](https://docs.google.com/document/d/1Q5h7Kew6YeRh523bozr4TQtEeyzb4vuW5Gu1mA0WUC8/edit?usp=sharing)