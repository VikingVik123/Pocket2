from BinaryOptionsTools import pocketoption

#ssid = (r'42["auth",{"session":"448be3b75e1e6d7969b7fd792682d23e", "isDemo":1,"uid":79658638,"platform":2}]')
#ssid = (r'42["auth",{"session":"vtftn12e6f5f5008moitsd6skl","isDemo":1,"uid":79658638,"platform":2}]')
#ssid = r'42["auth",{"session":"a:4:{s:10:\"session_id\";s:32:\"968fbe28a99f8fcbc5bb10ba3e9bf173\";s:10:\"ip_address\";s:12:\"98.97.79.202\";s:10:\"user_agent\";s:111:\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36\";s:13:\"last_activity\";i:1733449881;}448be3b75e1e6d7969b7fd792682d23e","isDemo":1,"uid":79658638,"platform":2}]'
ssid = r'42["auth",{"session":"dihpme6fh6s30mhe5nd47snu1l","isDemo":1,"uid":79658638,"platform":2}]'
demo = True
#ssid = input("Enter your ssid: ")
api = pocketoption(ssid, demo)

#data = api.GetCandles("EURUSD_otc", 5)
#print(data)
print(f"GET BALANCE: {api.GetBalance()}")
api.Call(1, "EURUSD_otc", 90, False)

