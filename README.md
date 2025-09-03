# Password Generator API

A simple Password Generator API built with __**Python**__ and __**Flask**__.
It generates random passwords containing both letters and symbols, with customizable length.

## Features

- Generate strong random passwords.
- Customize password length via query parameter.
- Built with __**Flask**__ and __**OOP**__ principles.
- Easy to run locally with venv.
- Ready for extension and deployment.

## Installation

### 1. Clone the repository

```
git clone https://github.com/prodsimu/password-generator-api.git

cd password-generator-api
```

### 2. Create a virtual environment

```
python -m venv .venv

source .venv/bin/activate   # Linux/macOS
# .\.venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

## Usage

### 1. Run the Flask server:

```
python app.py
```

By default, the API will run on:

```
http://127.0.0.1:5000
```

### 2. API Endpoint

Parameters:

| Name   | Type | Default | Description            |
| ------ | ---- | ------- | ---------------------- |
| length | int  | 12      | Length of the password |

Request example:
```
http://127.0.0.1:5000/generate_password?length=16
```

Response example:

``` json
{
  "password": "aB@dE!qR9kM"
}
```