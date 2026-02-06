# AfrikFund Project Issues & Tasks

This document outlines all the development tasks needed to build **AfrikFund (DiasporaDAO)**. This is a living document used to track the implementation of the decentralized funding platform.

---

## 🏗️ Workflow Overviews

### 1. Fundraising Lifecycle
1. **Creation**: Admin creates a campaign on-chain with a target goal (USDC/ETH) and deadline.
2. **Donation**: Global diaspora users connect wallets and donate assets to the campaign vault.
3. **Tracking**: On-chain events update the frontend progress bars and donor lists in real-time.
4. **Milestone**: Once the goal is met or project phases begin, funds are moved to governance status.

### 2. Transparency & Impact Lifecycle
1. **Proof Submission**: Project managers upload photos/receipts to IPFS and submit the hash to the contract.
2. **Withdrawal Request**: Admin requests a specific amount for a project milestone.
3. **DAO Approval**: Community (donors or multi-sig) votes to approve the release of funds.
4. **Disbursement**: Funds are released only to verified beneficiary addresses upon approval.

---

## 🛠️ Smart Contract Issues (Solidity)

### Phase 1: Setup & Constants
- [ ] **Issue #1**: Initialize Hardhat Environment
  - [ ] Configure `hardhat.config.ts` for Base Sepolia and Mainnet.
  - [ ] Implement `.env` management for private keys and API URLs.
  - [ ] Setup `tsconfig.json` for strictly typed contract scripts.
- [ ] **Issue #2**: OpenZeppelin Integration
  - [ ] Install `@openzeppelin/contracts`.
  - [ ] Import `Ownable`, `Pausable`, `ReentrancyGuard`, and `IERC20`.

### Phase 2: Core Campaign Logic
- [ ] **Issue #3**: Define Campaign Data Structures
  - [ ] Implement `Campaign` struct: `id`, `beneficiary`, `goal`, `deadline`, `totalRaised`, `metadataHash`, `status`.
  - [ ] Implement `Donation` struct for tracking user-level contributions.
- [ ] **Issue #4**: Implement `createCampaign` function
  - [ ] Add input validation (deadline must be in the future, goal > 0).
  - [ ] Implement incremental `campaignId` logic.
  - [ ] Emit `CampaignCreated` event with indexed ID and beneficiary.
- [ ] **Issue #5**: Implement Native ETH Donation
  - [ ] Add `donateETH` function with `payable` modifier.
  - [ ] Add reentrancy protection.
  - [ ] Update campaign state and donor mappings.
- [ ] **Issue #6**: Implement ERC-20 (USDC) Donation
  - [ ] Add `donateToken` function.
  - [ ] Implement `SafeERC20` for reliable token transfers.
  - [ ] Support specific stablecoin address configured at deployment.

### Phase 3: Governance & Withdrawals
- [ ] **Issue #7**: Implement Proof-of-Impact Storage
  - [ ] Define `WithdrawalRequest` struct: `amount`, `proofHash` (IPFS), `approvals`, `executed`.
  - [ ] Implement `submitWithdrawalRequest` (Admin only).
- [ ] **Issue #8**: Community Approval Logic
  - [ ] Implement `approveWithdrawal` function.
  - [ ] Setup threshold logic (e.g., 3-of-5 signers or majority of weight).
- [ ] **Issue #9**: Execute Withdrawal
  - [ ] Verify approval status and threshold before transfer.
  - [ ] Implement fund release to beneficiary principal.
  - [ ] Emit `FundsDisbursed` event.

---

## 💻 Frontend Issues (Next.js)

### Phase 4: Setup & Architecture
- [ ] **Issue #10**: Refine Next.js Project Structure
  - [ ] Create `components/ui`, `components/shared`, and `components/dashboard` folders.
  - [ ] Configure Tailwind CSS 4 with custom palette (African Gold: `#FFD700`, Earth Red: `#8B0000`).
- [ ] **Issue #11**: Web3 Provider Configuration
  - [ ] Setup `WagmiConfig` with Base network support.
  - [ ] Configure `Viem` public clients for read-only operations.
  - [ ] Integrate `ConnectKit` or `RainbowKit` for the modal interface.

### Phase 5: Core UI Components
- [ ] **Issue #12**: Navigation & Page Shell
  - [ ] Build `Navbar` with wallet connection and network switcher.
  - [ ] Build `Sidebar` for dashboard navigation.
  - [ ] Implement `Footer` with social links and documentation.
- [ ] **Issue #13**: Campaign Discovery UI
  - [ ] Build `CampaignGrid` with pagination/infinite scroll.
  - [ ] Build `CampaignCard` with:
    - [ ] Dynamic progress bar (percentage of goal).
    - [ ] Days remaining countdown.
    - [ ] "Impact Badge" based on category.
- [ ] **Issue #14**: Campaign Detail Page (`[id]/page.tsx`)
  - [ ] Implement dynamic data fetching via Wagmi hooks.
  - [ ] Build `DonationPanel` with asset toggle.
  - [ ] Display `ImpactGallery` (fetching from IPFS).

### Phase 6: User & Admin Dashboards
- [ ] **Issue #15**: Donor Impact Dashboard
  - [ ] Build `StatsCard` for "Total Contributed" and "Carbon Offset/Impact Score".
  - [ ] Build `ContributionHistory` table with links to BaseScan.
- [ ] **Issue #16**: Admin Campaign Management
  - [ ] Build `CreateCampaignForm` using `react-hook-form` and `zod`.
  - [ ] Implement IPFS upload for metadata (using Pinata/Infura).
  - [ ] Build `WithdrawalManager` for proof submission.

---

## 🧪 Testing & Quality Assurance

- [ ] **Issue #17**: Contract Unit Tests
  - [ ] Test successful campaign initialization.
  - [ ] Test edge cases: expired deadlines, zero-value donations.
  - [ ] Test unauthorized withdrawal attempts.
- [ ] **Issue #18**: E2E Flow Testing
  - [ ] Mock wallet connection and donation flow.
  - [ ] Verify IPFS data retrieval on the frontend.
  - [ ] Test mobile responsiveness on small-screen viewports.

---

## 🚀 Deployment & CI/CD

- [ ] **Issue #19**: Smart Contract Deployment
  - [ ] Create deployment scripts using Hardhat Ignition.
  - [ ] Verify contracts on BaseScan.
- [ ] **Issue #20**: Frontend Production Setup
  - [ ] Configure Vercel deployment.
  - [ ] Set up GitHub Actions for linting and type-checking.

---

## 📊 Priority Levels

- **P0 (Critical)**: Issues #1, #4, #5, #11, #13
- **P1 (High)**: Issues #6, #7, #9, #14, #16
- **P2 (Medium)**: Issues #8, #15, #17, #19
- **P3 (Low)**: Issues #10, #18, #20

---

**Authored by: bbkenny <jouleself@gmail.com>**
