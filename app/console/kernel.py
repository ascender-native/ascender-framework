from core.foundation.console.console_kernel import ConsoleKernel
import os

class Kernel(ConsoleKernel):
    def commands(self) -> None:
        self.load('app.console.commands.*')