abi = [{"constant":false,"inputs":[{"name":"_varDesc","type":"bytes"}],"name":"saveVar","outputs":[],"type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_from","type":"address"},{"indexed":false,"name":"variantDesc","type":"bytes"}],"name":"VarLog","type":"event"}];
var contract = web3.eth.contract(abi); 
var publicVarStore = contract.at("0x1c761940f41734b0acf9430082418aa259f2c784");
publicVarStore.saveVar.sendTransaction("%s", {from:eth.accounts[0]});
