FROM python:3.8.10-slim
RUN python -m pip install \
        parse \
        realpython-reader
# Create the working director in this docker image
WORKDIR /app

# Copy current folder data into /app of the container
COPY . /app

# Install the dependencies
RUN pip install --no-cache -r requirements.txt

# Run the command to start our app.py file
CMD ["python","app.py"]
