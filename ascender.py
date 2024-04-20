from asccore.contracts.foundation.application import Application as ApplicationContract
from asccore.contracts.kernel import Kernel as KernelContract
from asccore.main import app
from app.console.kernel import Kernel

def cli():
    app.singleton(ApplicationContract, lambda: app)
    app.singleton(KernelContract, Kernel)
    kernel = app.make(KernelContract)
    kernel.handle()

def serve():
    from asccore.contracts.foundation.application import Application as ApplicationContract
    from asccore.contracts.kernel import Kernel as KernelContract
    from asccore.main import app
    from app.http.kernel import Kernel

    app.singleton(ApplicationContract, lambda: app)
    app.singleton(KernelContract, Kernel)
    kernel = app.make(KernelContract)
    kernel.handle()

    return kernel.send()