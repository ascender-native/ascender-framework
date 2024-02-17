from core.contracts.foundation.application import Application as ApplicationContract
from app.console.kernel import Kernel
from core.contracts.kernel import Kernel as KernelContract
from core.main import app
 
def cli():
    app.singleton(ApplicationContract, lambda: app)
    app.singleton(KernelContract, Kernel)
    kernel: Kernel = app.make(KernelContract)
    kernel.handle()