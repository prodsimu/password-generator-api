# Password Generator API

A simple **Password Generator API** built with **Python** and **Flask**.  
It generates random passwords with customizable **length**, **symbols**, and **uppercase letters**.


## Features

- Generate strong random passwords
- Customize length, symbols, and uppercase usage via query parameters
- Built with **Flask** and **OOP principles**
- Easy to run locally with `venv`
- Ready for extension and deployment


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

Run the Flask server:

```
python app.py
```

By default, the API will run on:

```
http://127.0.0.1:5000
```

## API Endpoint

### Base URL

```
/generate_password
```

### Parameters

| Name          | Type | Default | Description                     |
| ------------- | ---- | ------- | ------------------------------- |
| length        | int  | 12      | Length of the password          |
| use_symbols   | bool | true    | Configures the use of symbols   |
| use_uppercase | bool | true    | Configures the use of uppercase |


## Examples

### Default request

```
http://127.0.0.1:5000/generate_password
```
```
{
  "password": "*wM%D#?uwC$?"
}
```

### With custom length

```
http://127.0.0.1:5000/generate_password?length=16
```
```
{
  "password": "!A?a-&tH&j*#AhH&"
}
```

### Without symbols

```
http://127.0.0.1:5000/generate_password?use_symbols=false
```
```
{
  "password": "oUHDMcqBIqeD"
}
```

### Without uppercase

```
http://127.0.0.1:5000/generate_password?use_uppercase=false
```
```
{
  "password": "*wM%D#?uwC$?"
}
```

### With length, without symbols and uppercase

```
http://127.0.0.1:5000/generate_password?length=16&use_symbols=false&use_uppercase=false
```
```
{
  "password": "ploxfmkzvfvufvxm"
}
```
