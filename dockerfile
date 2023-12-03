FROM miranor/alx_sandbox

# Update the system and install necessary packages
RUN apt-get update && \
   apt-get install -y pkg-config libmysqlclient-dev mysql-server && \
   apt-get clean && \
   rm -rf /var/lib/apt/lists/*

# Install Python packages with specific versions
RUN pip3 install Flask==2.1 Flask-SQLAlchemy==3.0 SQLAlchemy==1.4.* mysqlclient 

# Install Flask-CORS
RUN pip3 install flask_cors

# Install Flask-Security-Too
RUN pip3 install Flask-Security-Too

# Pin Werkzeug to version 1.0.1 to avoid the import issue
RUN pip3 install Werkzeug==2.3.7

# Pin Jinja2 to version 3.0.3 to avoid the import issue
RUN pip3 install Jinja2==3.0.3

# Install Pillow Package
Run pip install Pillow
