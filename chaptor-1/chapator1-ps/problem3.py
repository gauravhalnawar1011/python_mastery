
#  to activate an vitual enviremnt in  python add the comand 
# source venv/bin/activate
import pyttsx3        
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"
engine.say("hello bhamba how are u")
engine.runAndWait()

