import logging
import os

# logging tutorial; https://docs.python.org/3/howto/logging.html
logging.basicConfig(
    level=logging.DEBUG,
    format=" %(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y%m%d_%H%M%S",
    handlers=[
        logging.StreamHandler(),  # display log in console
        logging.FileHandler(os.path.join("logs", "debug.log")),  # write log to file
    ],
)

# adjust log report info level
logging.disable(logging.NOTSET)  # NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL

logging.info("program: started")


def hello(name):
    """returns a greeting"""
    logging.debug(f"running: hello()")
    logging.debug(f"argumnt: {name}")

    return f"hello {name}!"


hello("pony")
hello("goat")

logging.info("program: completed")
