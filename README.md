# Django Channels Tutorial

## Want to learn how to build this?

Check out the [tutorial](https://testdriven.io/blog/django-channels/).

## Want to use this project?

1. Fork/Clone

2. Create and activate a virtual environment:

   ```sh
   $ python3 -m venv venv && source venv/bin/activate
   ```

3. Install the requirements:

   ```sh
   (venv)$ pip install -r requirements.txt
   ```

4. Start a Redis server for backing storage:

   ```sh
   (venv)$ docker run -p 6379:6379 -d redis:5
   ```

5. Run the server with memory profiler:

   ```sh
   (venv)$ mprof run uvicorn core.asgi:application --port 8000 --lifespan off --host 0.0.0.0 --workers 1
   ```

6. Navigate to [http://localhost:8000/chat/](http://localhost:8000/chat/). Reload the page many times or send messages..
