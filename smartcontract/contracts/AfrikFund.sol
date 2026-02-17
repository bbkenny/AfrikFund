// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract AfrikFund is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Campaign {
        uint256 id;
        address beneficiary;
        uint256 goal;
        uint256 deadline;
        uint256 totalRaised;
        string metadataHash; // IPFS hash
        bool active;
    }

    mapping(uint256 => Campaign) public campaigns;
    uint256 public campaignCount;

    event CampaignCreated(uint256 indexed id, address indexed beneficiary, uint256 goal);

    constructor() Ownable(msg.sender) {}

    function createCampaign(
        address _beneficiary,
        uint256 _goal,
        uint256 _duration,
        string memory _metadataHash
    ) external {
        require(_goal > 0, "Goal must be > 0");
        require(_duration > 0, "Duration must be > 0");

        campaignCount++;
        campaigns[campaignCount] = Campaign({
            id: campaignCount,
            beneficiary: _beneficiary,
            goal: _goal,
            deadline: block.timestamp + _duration,
            totalRaised: 0,
            metadataHash: _metadataHash,
            active: true
        });

        emit CampaignCreated(campaignCount, _beneficiary, _goal);
    }
}
