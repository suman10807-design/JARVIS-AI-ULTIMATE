
import os
import webbrowser
import subprocess


class JarvisController:

    def open_website(self, url):
        if not url.startswith(("https://", "http://")):
            return "Invalid website address."

        webbrowser.open(url)
        return f"Opening {url}"

    def open_application(self, application):

        allowed_apps = {
            "notepad": ["notepad.exe"],
            "calculator": ["calc.exe"],
            "paint": ["mspaint.exe"],
            "file explorer": ["explorer.exe"]
        }

        app = application.lower().strip()

        if app not in allowed_apps:
            return "This application is not in the approved list."

        try:
            subprocess.Popen(allowed_apps[app])
            return f"Opening {app}"

        except OSError as error:
            return f"Could not open application: {error}"


if __name__ == "__main__":
    jarvis = JarvisController()

    print(jarvis.open_application("notepad"))
