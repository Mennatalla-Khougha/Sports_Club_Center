# Use the base image
FROM miranor/alx_sandbox

# Update the system and install necessary packages
RUN apt-get update && \
   apt-get install -y pkg-config libmysqlclient-dev mysql-server && \
   apt-get clean && \
   rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install SQLAlchemy==1.4.* mysqlclient

# Install Flask and Flask-CORS
RUN pip3 install flask flask_cors
