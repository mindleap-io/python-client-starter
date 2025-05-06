---
title: Contribution
---

Contribution
============

Development Environment
-----------------------
1. Install the required tools:
- Install python
- Install pip, setuptools and wheel
- Install pipenv

2. Install a virtual environment:

    ```shell
    > pipenv shell
    ```

3. Install the required development packages:

    ```shell
    > pipenv install --dev
    ```

4. Build the project:

    ```shell
    > pipenv run pip install -e .
    ```

5. Set up your local environment:
- Create a file named `.env` in the project root.
- Fill in the **Mindleap Starter** host url (adjust the port, if necessary)

    ```shell
    MINDLEAP_STARTER_HOST_URL=http://localhost:8090
    ```

6. Run the tests, for example:

    ```shell
    > pipenv run pytest tests/test_1_graph_model_service.py
    ```
