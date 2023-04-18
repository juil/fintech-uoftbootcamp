/*
XP-Token Crowdsale
*/

pragma solidity ^0.5.0;

import "./XPTokenMintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract XP_TokenCrowdsale is Crowdsale, MintedCrowdsale {
    constructor(
        uint256 rate,
        address payable wallet,
        XP_Token token
    )
      Crowdsale(rate, wallet, token)
      public
    {
        // constructor can stay empty
    }
}

contract XP_TokenCrowdsaleDeployer {
    address public xp_token_address;
    address public xp_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
    public
    {
        XP_Token token = new XP_Token(name, symbol, 0);
        xp_token_address = address(token);

        XP_TokenCrowdsale xp_crowdsale =
            new XP_TokenCrowdsale(1, wallet, token);
        xp_crowdsale_address = address(xp_crowdsale);

        token.addMinter(xp_crowdsale_address);
        token.renounceMinter();
    }
}
