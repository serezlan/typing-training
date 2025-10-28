import speechd


class Voxin:
    def __init__(self, client_name="chatty"):
        self._client = speechd.Client(client_name)
        self._client.set_synthesis_voice("nathan-embedded-high")
        self._client.set_rate(60)

    def speak(self, text):
        self._client.speak(text)

    def close(self):
        self._client.close()

    def set_voice(self, voice):
        match voice:
            case "nathan":
                synth_voice = "nathan-embedded-high"
            case "zoe":
                synth_voice = "zoe-embedded-high"
            case _:
                synth_voice = "nathan-embedded-high"

        self._client.set_synthesis_voice(synth_voice)
