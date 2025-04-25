FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install -e ./src/recrut_ai

EXPOSE 8501

CMD ["streamlit", "run", "src/recrut_ai/app.py", "--server.address=0.0.0.0"]