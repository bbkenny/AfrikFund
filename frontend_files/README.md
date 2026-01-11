# AfrikFund — Frontend

Next.js 14 frontend application for AfrikFund (DiasporaDAO) - a decentralized platform empowering African diaspora communities to transparently fund real-world projects back home.

## Overview

The AfrikFund frontend is a modern Web3 dApp built with Next.js 14, featuring:

- **Wallet Integration**: MetaMask/WalletConnect support via Wagmi and Viem
- **Campaign Management**: Create and manage fundraising campaigns
- **Donation Interface**: Donate via ETH/USDC with real-time tracking
- **Donor Dashboards**: Track donations and impact reports
- **IPFS Integration**: Upload and view proof-of-impact documents
- **Real-time Updates**: Live campaign statistics and funding progress

## Tech Stack

- **Framework:** Next.js 14
- **Web3 Libraries:** Wagmi, Viem
- **Styling:** Tailwind CSS
- **State Management:** React Context / Zustand (as needed)
- **IPFS:** Pinata/NFT.Storage integration
- **Network:** Base L2 (Testnet/Mainnet)

## Prerequisites

- Node.js v18+
- Yarn or npm
- MetaMask wallet
- Alchemy/Base API key (free)

## Quick Start

```bash
# Install dependencies
npm install
# or
yarn install

# Run development server
npm run dev
# or
yarn dev

# Build for production
npm run build
# or
yarn build

# Start production server
npm start
# or
yarn start
```

Open [http://localhost:3000](http://localhost:3000) to view the application.

## Environment Variables

Create a `.env.local` file:

```env
NEXT_PUBLIC_RPC_URL=https://sepolia.base.org
NEXT_PUBLIC_CHAIN_ID=84532
NEXT_PUBLIC_CONTRACT_ADDRESS=your_contract_address
NEXT_PUBLIC_IPFS_API_KEY=your_ipfs_api_key
NEXT_PUBLIC_IPFS_API_SECRET=your_ipfs_api_secret
NEXT_PUBLIC_ALCHEMY_API_KEY=your_alchemy_api_key
```

**Note:** Never commit `.env.local` to version control! Use `.env.example` for reference.

## Project Structure

```
frontend_files/
├── src/
│   ├── app/                      # Next.js 14 App Router
│   │   ├── layout.tsx            # Root layout
│   │   ├── page.tsx              # Home page
│   │   ├── campaigns/            # Campaign pages
│   │   ├── donate/               # Donation pages
│   │   └── dashboard/            # Donor dashboard
│   ├── components/               # React components
│   │   ├── CampaignCard.jsx      # Campaign display card
│   │   ├── DonationForm.jsx      # Donation interface
│   │   ├── WalletConnect.jsx     # Wallet connection
│   │   └── ImpactReport.jsx      # Impact visualization
│   ├── hooks/                    # Custom React hooks
│   │   ├── useCampaigns.ts       # Campaign data hook
│   │   ├── useDonations.ts       # Donation hook
│   │   └── useIPFS.ts            # IPFS upload hook
│   ├── lib/                      # Utilities
│   │   ├── wagmi.ts              # Wagmi configuration
│   │   ├── ipfs.ts               # IPFS client
│   │   └── contracts.ts          # Contract ABIs and addresses
│   └── styles/                   # Global styles
│       └── globals.css           # Tailwind CSS imports
├── public/                       # Static assets
├── package.json
├── tailwind.config.js
├── next.config.js
└── tsconfig.json
```

## Features

### Wallet Integration

- **MetaMask**: Primary wallet support
- **WalletConnect**: Mobile wallet support
- **Multi-chain**: Base L2 (testnet/mainnet)
- **Network Switching**: Automatic network detection and switching

### Campaign Features

- **Create Campaigns**: Set goals, deadlines, and beneficiaries
- **Browse Campaigns**: View all active campaigns
- **Campaign Details**: Detailed campaign information with progress tracking
- **Real-time Updates**: Live funding progress and statistics

### Donation Features

- **ETH/USDC Donations**: Support for multiple currencies
- **Real-time Tracking**: Live donation tracking and updates
- **Donation History**: View personal donation history
- **Impact Reports**: See how donations are being used

### Dashboard Features

- **Donor Dashboard**: Personal donation tracking
- **Campaign Management**: Manage your created campaigns
- **Impact Visualization**: Charts and graphs showing impact
- **Proof-of-Impact**: View IPFS-stored proofs (photos/receipts)

## Development

### Running Locally

```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

The application will be available at [http://localhost:3000](http://localhost:3000).

### Building for Production

```bash
# Build the application
npm run build

# Start production server
npm start
```

## Deployment

### Vercel (Recommended)

1. Push your code to GitHub
2. Import project in Vercel
3. Configure environment variables
4. Deploy

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

### Cloudflare Pages

1. Push code to GitHub
2. Create new Pages site in Cloudflare
3. Configure build settings:
   - Build command: `npm run build`
   - Build output: `.next`
4. Set environment variables
5. Deploy

### Other Platforms

The application can be deployed to any platform that supports Next.js:
- Netlify
- AWS Amplify
- Railway
- Render

## Web3 Integration

### Wagmi Configuration

Wagmi is configured to connect to Base L2 networks. Configuration can be found in `src/lib/wagmi.ts`.

### Contract Integration

Contract ABIs and addresses are stored in `src/lib/contracts.ts`. Update contract addresses when deploying new contracts.

### IPFS Integration

IPFS is used for storing proof-of-impact documents. Integration is handled via Pinata/NFT.Storage in `src/lib/ipfs.ts`.

## UX Considerations

- **Mobile-First**: Responsive design for mobile and desktop
- **Low-Data Users**: Optimized for users in Africa with limited data
- **KYC-Optional**: Simplified onboarding for diaspora senders
- **SMS/2FA**: Optional SMS/2FA integration for security
- **Multi-language**: Support for multiple languages (future)

## Testing

```bash
# Run tests (if configured)
npm test

# Run tests in watch mode
npm test:watch

# Run E2E tests
npm test:e2e
```

## Contributing

We welcome contributions! Please see [CONTRIBUTION.md](../CONTRIBUTION.md) for guidelines.

## License

MIT License - see LICENSE file for details.
