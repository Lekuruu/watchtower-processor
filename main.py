
import app.session as session
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - <%(name)s> %(levelname)s: %(message)s"
)

def main():
    for event, args, kwargs in session.events.listen():
        event(*args, **kwargs)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
