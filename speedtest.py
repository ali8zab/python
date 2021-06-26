import speedtest
s = speedtest.Speedtest()

print("Welcome to Ali's speed test program :)")
print("Test Download Speed...")

download_result = s.download()/1024/1024
print(f'Your download speed is {download_result:2f}mbit/s')

print('Test Upload Speed...')
upload_result = s.upload()/1024/1024

print(f"Your Upload speed is {upload_result:2f}mbit/s")


print("Test Ping Test...")
ping_result = s.results.ping
print(f"Your ping speed is {ping_result}ms")