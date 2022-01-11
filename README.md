## DSSI 2021 summer project <br>

**project 1: start galaxy classification task**<br>

for this task we were given 50,000 images of star or galaxy crop images from astronomy data, each object has 8 channels data which are g band, r band, i band, z band, and their point spread function in each band. <br>

the filter data are standard Sloan digital Sky Survey (SDSS) photometric filters, the g band and r band are considered visual spectrum, where i band and z band are in the near infrared spectrum.<br>
<img src="https://github.com/ethanahlquist/DSSI_Asteroid_Object_Detection/blob/main/img/SDSS.jpg" width="400">


g band example: <br>
![](https://github.com/ethanahlquist/DSSI_Asteroid_Object_Detection/blob/main/img/g.png)<br>
psf-g band example: <br>
![](https://github.com/ethanahlquist/DSSI_Asteroid_Object_Detection/blob/main/img/psfg.png)<br>

We tried couple CNN architectures, the best performing model we had great accuracy and great AUC score.<br>
<img src="https://github.com/ethanahlquist/DSSI_Asteroid_Object_Detection/blob/main/img/cnn_elyssa_model.PNG" width="500"><br>
<img src="https://github.com/ethanahlquist/DSSI_Asteroid_Object_Detection/blob/main/img/confusion_matrix.png" width="300"><br>



**project 2: detect asteroids from difference images**<br>

this project we are given astronomy difference images<br>

astronomy difference image is made from two exposure subtracting each other, the telescope track certain object in the sky, while most star are orbiting the same speed, asteroid or satellite will orbit in different speed compare to the stars, so by subtracting two frames, we can see what is moving in different velocity and thus determin if this is an asteroid or satellite or even comet.  Pluto was discovered this way as well  

the asteroids in those images are artifically injected with galsim. there are each 20 asteroids per images. <br>


traditional CNN : 

Fast-R

YOLO: 


<img src="https://github.com/ethanahlquist/DSSI_Asteroid_Object_Detection/blob/main/Joe/result/result17.png" width="500"><br>

