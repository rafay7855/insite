FROM python:3.9

WORKDIR /usr/src/insite

# Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY insite.py .
COPY app app
COPY tests tests 

# Environment Variables
ENV FLASK_APP insite.py
ENV FLASK_CONFIG dev

CMD [ "flask", "run" ] 