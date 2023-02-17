# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3
ENV SPI_PATH /app/SPI-Py
WORKDIR /app

# Copy SPI-Py driver to rfid_card_reader
COPY SPI-Py ./SPI-Py
COPY main.py ./
COPY hal ./hal

# Install the relevant modules required 
RUN pip3 install --no-cache-dir smbus
RUN pip3 install --no-cache-dir rpi.gpio
# Install SPI driver 
WORKDIR $SPI_PATH
RUN python3 setup.py install

# Trigger Python script
WORKDIR /app
CMD ["python3", "./main.py"]
