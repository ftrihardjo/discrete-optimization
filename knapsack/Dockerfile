FROM python
# Set the working directory in the container
WORKDIR /usr/src/app
# Copy the current directory contents into the container
COPY . .
# Install ortools
RUN pip install ortools
# Command to run the application
CMD ["python", "./main.py"]