pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract advCollectible is ERC721 {

    uint256 public tokenCounter;

    constructor() public ERC721("IceCream", "MF")
    {
        tokenCounter = 0;
    }

    // "userProvidedSeed" must be avoided because not needed, needed in prevoius project because of the random
    function createCollectible(string memory tokenURI) public returns (uint256) {
        uint256 newItemId = tokenCounter;
        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        tokenCounter = tokenCounter + 1;
        return newItemId;
    }




    function setTokenURI(uint256 tokenId, string memory _tokenURI) public  {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: transfer caller is not owner nor approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }


}