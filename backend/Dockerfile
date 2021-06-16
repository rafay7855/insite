FROM python:3.8.5

WORKDIR /usr/src/insite

# Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt

# copy the content of the local src directory to the working directory
COPY insite.py config.py .
COPY app app
COPY tests tests 

# Environment Variables
ENV FLASK_APP insite.py
ENV FLASK_CONFIG test

CMD ["flask", "test" ]
