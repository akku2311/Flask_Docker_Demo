# Small version of Python #
FROM python:alpine3.7
EXPOSE 5010
COPY . /Flask_Docker_Demo
WORKDIR /Flask_Docker_Demo
#!/usr/bin/env python3
RUN chmod +x Flask_Code.py
RUN pip install -r requirements.txt
#ENTRYPOINT ["python3"]
CMD ["python3","./Flask_Code.py"]
