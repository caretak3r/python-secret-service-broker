from app import config, api

if __name__ == "__main__":
    api.run(host= config.HOST,
            port= config.PORT,
            debug= config.DEBUG)