class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("Creating new Instance")
            cls._instance = super().__new__(cls)
        else:
            print("Returning Existing instance")
        return cls._instance
    def