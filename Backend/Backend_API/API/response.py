# class for Response Structure for api 
# example: 
# {
#   "success": true,
#   "message": "User logged in successfully",
#   "payload": { }
# }
# 
class Response():
    def __init__(self, success, message, payload=None):
        self.success = success
        self.message = message
        self.payload = payload
    
    def setStatus(self, value):
        self.success = value

    def setMessage(self, value):
        self.message = value

    def setPayload(self, value):
        self.payload = value

    def to_json(self):
      return {"success": self.success, "message": self.message, "payload": self.payload}