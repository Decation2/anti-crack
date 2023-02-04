import sys
import ctypes

def is_vm():
    with open("/proc/cpuinfo", "r") as f:
        cpuinfo = f.read()
    return "vmware" in cpuinfo or "qemu" in cpuinfo

def is_debugger_present():
    return ctypes.windll.kernel32.IsDebuggerPresent() != 0

if is_vm() or is_debugger_present():
    print("Debugging tool detected! Exiting...")
    sys.exit(0)
else:
    print("Program running normally.")