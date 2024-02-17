from core.contracts.foundation.application import Application as ApplicationContract
from app.http.kernel import Kernel
from core.contracts.kernel import Kernel as KernelContract
from core.main import app

app.singleton(ApplicationContract, lambda: app)
app.singleton(KernelContract, Kernel)
kernel = app.make(KernelContract)
kernel.handle()

serve = kernel.send()
