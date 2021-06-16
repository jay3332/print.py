import subprocess;


class PRINTER(object, metaclass=type):
  lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
  lpr.stdin.write(your_data_here)
