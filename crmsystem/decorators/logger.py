from datetime import datetime


class Logger(object):
    def __init__(self, pre=True, post=True, showTime=True, opMessage=""):
        super().__init__()
        self.pre = pre
        self.post = post
        self.showTime = showTime
        self.opMessage = opMessage

    def __call__(self, function):
        def wrap_call(*args, **kargs):
            if self.pre:
                message = "{} - [BEGIN] {}".format(
                    datetime.now(), self.opMessage)
                print(message)

            results = function(*args, **kargs)

            if(self.post):
                message = "{} - [END] {}".format(
                    datetime.now(), self.opMessage)
                print(message)

            return results

        return wrap_call
