# AfrikFund — Smart Contracts

Solidity smart contracts for AfrikFund (DiasporaDAO) - a decentralized platform empowering African diaspora communities to transparently fund real-world projects back home. Built on Base L2 for low fees.

## Overview

AfrikFund enables African diaspora communities to:

- **Create Fundraising Campaigns**: Set goals, deadlines, and beneficiaries for projects (schools, clinics, infrastructure)
- **Transparent Donations**: Donate via ETH/USDC with real-time fund tracking
- **Proof-of-Impact Withdrawals**: IPFS-based proof submission (photos/receipts) for fund disbursement
- **DAO Governance**: Multi-sig approval system for withdrawals
- **Impact Tracking**: Donor dashboards with impact reports

## Tech Stack

- **Language:** Solidity ^0.8.19
- **Framework:** Hardhat
- **Libraries:** OpenZeppelin (Ownable, Pausable, ReentrancyGuard)
- **Testing:** Hardhat Test Suite
- **Network:** Base L2 (Testnet/Mainnet)
- **Chain ID:** 84532 (Testnet) / 8453 (Mainnet)

## Quick Start

```bash
# Install dependencies
npm install

# Compile contracts
npx hardhat compile

# Run tests
npx hardhat test

# Deploy to Base Sepolia Testnet
npx hardhat run scripts/deploy.js --network baseSepolia
```

## Project Structure

```
smartcontract/
├── contracts/
│   ├── CampaignFactory.sol       # Factory for campaign creation
│   ├── Campaign.sol              # Individual campaign contract
│   ├── interfaces/
│   │   ├── ICampaign.sol         # Campaign interface
│   │   └── IERC20.sol            # ERC-20 interface
│   └── libraries/
│       └── CampaignMath.sol      # Math utilities
├── scripts/
│   ├── deploy.js                 # Deployment script
│   ├── verify.js                 # Contract verification script
│   └── initialize.js             # Contract initialization
├── test/
│   ├── CampaignFactory.test.js   # Factory tests
│   ├── Campaign.test.js          # Campaign tests
│   └── integration.test.js       # Integration tests
├── hardhat.config.ts             # Hardhat configuration
└── package.json                  # Dependencies
```

## Contract Architecture

### CampaignFactory.sol

**Purpose:** Central factory managing campaign creation and registration.

**Key Functions:**
- `createCampaign(string memory name, uint256 goal, uint256 deadline, address beneficiary)` - Create new campaign
- `getCampaigns(address creator)` - Get all campaigns by creator
- `getAllCampaigns()` - Get all active campaigns
- `pauseCampaign(address campaign)` - Admin: Pause campaign

**Events:**
- `CampaignCreated(address indexed creator, address indexed campaign, uint256 timestamp)`

### Campaign.sol

**Purpose:** Individual campaign contract handling donations and withdrawals.

**Key Functions:**
- `donate(uint256 amount)` - Donate ETH/USDC to campaign
- `submitProof(string memory ipfsHash)` - Submit IPFS proof for withdrawal
- `approveWithdrawal(uint256 amount, string memory proofHash)` - Multi-sig approval
- `withdraw(uint256 amount)` - Withdraw funds to beneficiary
- `getDonations(address donor)` - Get donation history
- `getTotalRaised()` - Get total funds raised
- `pause()` / `unpause()` - Emergency controls

**Events:**
- `Donation(address indexed donor, uint256 amount, uint256 timestamp)`
- `ProofSubmitted(address indexed campaign, string ipfsHash, uint256 timestamp)`
- `Withdrawal(address indexed beneficiary, uint256 amount, uint256 timestamp)`

## Security Best Practices

- **OpenZeppelin Contracts**: Use audited contracts (`Ownable`, `Pausable`, `ReentrancyGuard`)
- **Multi-sig**: Implement multi-sig for withdrawals
- **Timelocks**: Add timelock delays for sensitive operations
- **Emergency Pause**: Pausable functionality for emergency stops
- **Professional Audit**: Get audit from firms like PeckShield or Certik before mainnet

## Transparency Features

- **IPFS Storage**: Store proofs (photos, receipts) on IPFS/Arweave
- **Event Emission**: Emit events for all fund movements
- **The Graph Integration**: Index on-chain data for querying
- **Chainlink Oracles**: Use for fiat rate conversions (USD to NGN)

## Environment Variables

Create a `.env` file:

```env
PRIVATE_KEY=your_private_key
BASE_RPC_URL=https://sepolia.base.org
ETHERSCAN_API_KEY=your_etherscan_api_key
IPFS_API_KEY=your_ipfs_api_key
IPFS_API_SECRET=your_ipfs_api_secret
```

**Note:** Never commit your private key or `.env` file to version control!

## Network Configuration

### Base Sepolia Testnet

- **Chain ID:** 84532
- **RPC URL:** `https://sepolia.base.org`
- **Explorer:** [Base Sepolia Explorer](https://sepolia.basescan.org/)
- **Faucet:** [Base Sepolia Faucet](https://www.coinbase.com/faucets/base-ethereum-sepolia-faucet)

### Base Mainnet

- **Chain ID:** 8453
- **RPC URL:** `https://mainnet.base.org`
- **Explorer:** [BaseScan](https://basescan.org/)

## Deployment

### Deploy CampaignFactory

```bash
npx hardhat run scripts/deploy.js --network baseSepolia
```

### Initialize CampaignFactory

```bash
npx hardhat run scripts/initialize.js --network baseSepolia
```

### Verify Contracts

```bash
npx hardhat verify --network baseSepolia <CONTRACT_ADDRESS> <CONSTRUCTOR_ARGS>
```

## Testing

```bash
# Run all tests
npx hardhat test

# Run specific test file
npx hardhat test test/Campaign.test.js

# Run tests with gas reporting
REPORT_GAS=true npx hardhat test

# Coverage report
npx hardhat coverage
```

## Scalability Considerations

- **L2 Deployment**: Deploy on Base L2 for low fees (critical for African users)
- **Chainlink Oracles**: Use for fiat conversions (USD to NGN)
- **Gas Optimization**: Optimize contract code for minimal gas usage
- **Batch Operations**: Consider batching for multiple donations/withdrawals

## Contributing

We welcome contributions! Please see [CONTRIBUTION.md](../CONTRIBUTION.md) for guidelines.

## License

MIT License - see LICENSE file for details.
