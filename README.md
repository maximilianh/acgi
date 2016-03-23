Code that posts a string to the ethereum network via a CGI.

ran these commands to get current geth
see https://github.com/ethereum/go-ethereum/wiki/Installation-Instructions-for-Ubuntu
sudo apt-get install geth

   screen -S geth
   if first install do: geth --testnet account new
   geth --unlock 0 --testnet
   password for the unlock command is 'acgi' without quotes
   ctrl-a ctrl-d

do not forget this - otherwise the client can't connect to the GETH instance:

    chmod a+rw /home/ubuntu/.ethereum/testnet/geth.ipc

sendVar.js : template to send the transaction, string is marked with %s

VarStore.sol : solidity contract file

VarStoreDeploy.js : compiled solidity, this has been posted to the ethereum testnet on Wed Mar 23 2016


