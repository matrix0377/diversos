import speedtest
import os

os.system('cls')
# test = speedtest.Speedtest()

# down_speed = test.download()
# up_speed = test.upload()

# print(f"Download speed: ", {down_speed})
# print(f"Upload Speed: ", {up_speed})

import speedtest

servers = []
# If you want to test against a specific server
# servers = [1234]

threads = None
# If you want to use a single threaded test
# threads = 1

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download(threads=threads)
s.upload(threads=threads)
s.results.share()

results_dict = s.results.dict()

