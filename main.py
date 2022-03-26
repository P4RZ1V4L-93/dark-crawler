from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

profile = FirefoxProfile(r'C:\Users\rohit\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()

options = Options()
options.binary_location = r'C:\Users\rohit\Desktop\Tor Browser\Browser\firefox.exe'

driver = webdriver.Firefox(firefox_profile=profile, executable_path= r'C:\Users\rohit\Desktop\Python_Projects\Crawler\geckodriver.exe', options=options)

driver.get("http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/")