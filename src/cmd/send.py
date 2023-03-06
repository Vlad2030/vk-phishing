import os
import subprocess


def send(command: str, stdout: bool = None) -> None:
    if command:
        if stdout:
            subprocess.run(
                args=command.split(" "),
                stdout=subprocess.PIPE,
            ).stdout.decode("utf-8")

        elif stdout is None:
            return os.system(command=command)

        else:
            return print(f"Wrong stdout argument({stdout})")

    else:
        return print(f"Wrong command argument({command})")
