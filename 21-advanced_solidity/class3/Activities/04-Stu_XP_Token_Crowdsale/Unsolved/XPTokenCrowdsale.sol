/*
XP-Token Crowdsale
*/

// @TODO: Add the pragma statement

// @TODO: Add the import statement for the `XPTokenMintable.sol` file
// @TODO: Add the import statements for the OpenZeppelin `Crowdsale` contract.
// @TODO: Add the import statements for the OpenZeppelin `MintedCrowdsale` contract.


contract XP_TokenCrowdsale is Crowdsale, MintedCrowdsale {

    // @TODO: Create a `constructor` function that includes three attributes: `rate`, `wallet` and `token`.

    // @TODO: Create the public `Crowdsale` constructor that takes in the same three attributes: `rate`, `wallet`, and `token`.

    // @TODO
}


contract XP_TokenCrowdsaleDeployer {

    // @TODO: Add public addresses to keep track of the token_address and arcade_sale_address

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet // this address will receive all Ether raised by the sale
    )
        public
    {
        // @TODO: create the XP_Token and its address
        // Your code here!

        // @TODO: create the XP_TokenCrowdsale and its address
        // Your code here!

        // @TODO: make the XP_TokenCrowdsale contract a minter, then have the XP_TokenCrowdsaleDeployer renounce its minter role
        // Your code here!
    }
}
