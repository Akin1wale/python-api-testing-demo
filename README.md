# Python API Testing Demo

A simple, zero-dependency Python script that performs HTTP GET and POST requests against a public API and uses `assert` statements to verify responses. This project demonstrates how to write and run basic API tests using Python's `requests` library.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Running the Tests](#running-the-tests)
8. [Extending the Tests](#extending-the-tests)
9. [Contributing](#contributing)
10. [License](#license)

---

## Project Overview

This mini‑project (`api_tests.py`) illustrates how to:

* Send HTTP GET and POST requests using the [`requests`](https://docs.python-requests.org/) library
* Validate responses via Python `assert` statements
* Organize tests in functions and execute them as a script

The demo uses the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) fake REST API for testing, so you don’t need to set up any servers.

---

## Features

* **GET Test**: Verifies that a sample resource (`/posts/1`) returns HTTP status code **200**
* **POST Test**: Sends a new post and checks for HTTP status code **201**
* **Multiple GETs**: Loops through IDs 1–5, asserting status 200 and JSON schema
* **Clear Output**: Prints status codes and test progress to the console

---

## Tech Stack

* **Language:** Python 3.x
* **Library:** [`requests`](https://pypi.org/project/requests/)

---

## Prerequisites

* Python **3.6** or higher installed and available on your `PATH`
* Basic familiarity with command‑line usage and virtual environments

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/python-api-testing-demo.git
   cd python-api-testing-demo
   ```

2. **Set up a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   # OR on Windows
   .\venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install requests
   ```

---

## Usage

Open the `api_tests.py` file to review the test functions:

```python
import requests

# Test that GET /posts/1 returns 200 OK
...

# Test that POST /posts returns 201 Created
...

# Loop test for GET /posts/1–5
...
```

You can customize:

* Endpoints (`url` variables)
* Payloads (`json` bodies)
* Assertions (status codes, JSON keys)

---

## Running the Tests

With your virtual environment activated, run:

```bash
python api_tests.py
```

You should see output similar to:

```
Running API tests...

GET https://jsonplaceholder.typicode.com/posts/1 → 200
POST https://jsonplaceholder.typicode.com/posts → 201
✓ GET post 1 passed
✓ GET post 2 passed
✓ GET post 3 passed
✓ GET post 4 passed
✓ GET post 5 passed

🎉 All tests passed!
```

If an `assert` fails, the script will stop and display an error message indicating which check failed.

---

## Extending the Tests

Here are a few ideas to level up:

* Integrate **`pytest`** for richer test discovery and reporting
* Validate additional JSON fields or response headers
* Add **error-handling** (`try/except`) around requests
* Store endpoints and test data in a **config file** (`.json` or `.yaml`)
* Set up a **GitHub Actions** workflow to run tests automatically on each push

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests:

1. Fork the repo
2. Create a new branch (`git checkout -b feature/my-test`)
3. Commit your changes (`git commit -m "Add new test"`)
4. Push to the branch (`git push origin feature/my-test`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
