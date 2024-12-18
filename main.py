from testhttp_modules import testhttp_modules

from testhttp_modules.trigger_new_entries import NewEntriesTrigger
from testhttp_modules.action_request import Request


if __name__ == "__main__":
    module = testhttp_modules()
    module.register(NewEntriesTrigger, "NewEntriesTrigger")
    module.register(Request, "Request")
    module.run()
