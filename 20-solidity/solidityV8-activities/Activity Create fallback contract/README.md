**fallback** is a special function that is executed either when:

1. a function that does not exist is called or
2. Ether is sent directly to a contract but receive() does not exist or msg.data is not empty

- fallback has a 2300 gas limit when called by transfer or send.