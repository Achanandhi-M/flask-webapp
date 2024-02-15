```markdown
# Flask Electricity Billing API

## Introduction
This Flask application provides an API for electricity billing. Users can log in and calculate their electricity bills based on meter readings.

## Installation
1. Install Flask and Flask-Session:
   ```bash
   pip install Flask Flask-Session
   ```

## Usage
1. Clone the repository.
2. Navigate to the project directory.

### Running the Application
```bash
python app.py
```

## API Endpoints

### 1. `/` (Login Endpoint)
- **Method:** POST
- **Input:**
  - JSON:
    ```json
    {
        "name": {{user}}
        "pass": {{pass}}
    }
    ```
- **Output:**
  - Success:
    ```json
    {
        "message": "Success",
        "user": "John"
    }
    ```
  - Error:
    ```json
    {
        "message": "User Not Found :("
    }
    ```

### 2. `/bill` (Bill Endpoint)
- **Method:** POST
- **Input:**
  - JSON:
    ```json
    {
        "Previous": 50,
        "Present": 100
    }
    ```
- **Output:**
  - Success:
    ```json
    {
        "message": "Success",
        "user": "John",
        "total_units_consumed": 50,
        "total_amount_rupees": 500
    }
    ```
  - Error:
    ```json
    {
        "message": "Error"
    }
    ```

## Testing with Postman
1. Open Postman.
2. Create a new request for each endpoint.
3. Set the request method to POST.
4. Enter the appropriate endpoint URL (e.g., `http://localhost:5000/`).
5. Add the required JSON parameters in the request body.
6. Click on the "Send" button to test the API
