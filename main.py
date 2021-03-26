from api import API_KEY
from etherscan_py import etherscan_py
from etherscan import Etherscan
import matplotlib.pyplot as plt

eth = Etherscan(API_KEY)
client = etherscan_py.Client(API_KEY)

contract = str(input("Contract adress?"))
block = int(input("Block Number?"))

tx = client.get_all_transactions(from_address=contract,status=2,from_block=block)
nonce = []
address= []
for transaction in tx:
    nonce.append(transaction.nonce)
    address.append(transaction.from_address)

nonce , address = zip(*sorted(zip(nonce,address),reverse=True))
Eth_balance = []
for address in address:
    Eth_balance.append(float(eth.get_eth_balance(address))/(10**18))

print(len(nonce),len(Eth_balance))
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(nonce,"k+--",label="Number of transactions")
ax1.semilogy()
ax1.set_ylabel("Number of transactions")
ax2.plot(Eth_balance,"ro",label= "ETH balance")
ax2.semilogy()
ax2.set_ylabel("ETH BALANCE")
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.show()



