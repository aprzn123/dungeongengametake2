import configparser

class JsonDict(dict):
    def __getattr__(self, attr):
        return self[attr]

class Config:
    def __init__(self, filename):
        self.cfgp = configparser.ConfigParser()

        self.filename = filename

        self.update_data()

    def disp_data(self):
        return data["DISPLAY"]

    def reload_data(self):
        cfgp.read(self.filename)

        self.data = JsonDict({
            "DISPLAY": {
                "WindowWidth": cfgp["DISPLAY"].getint("WindowWidth"),
                "WindowHeight": cfgp["DISPLAY"].getint("WindowHeight"),
                "Fullscreen": cfgp["DISPLAY"].getboolean("Fullscreen"),
                "TileWidth": cfgp["DISPLAY"].getint("TileWidth")
            }
        })

config_cfg = Config("config.cfg")
