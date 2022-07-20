# Docker dash sample app

<h3>To run the docker-dash-sample-app container, simply run below command. The image has been pushed to docker hub repository</h3>
<pre>docker run -it -p 8050:8050 vishalkashyap95/docker-dash-sample-app:v1<br># After running above command, open browser and enter "127.0.0.1:8050" in URL</pre> 


<h2>Details</h2>
<ul>
<li><b>app.py</b> contains code to create a dash app.<br>
<li><b>Dockerfile</b> contains the configuration of base image, copying the code into image and command to call the app.py<br>
</ul>

