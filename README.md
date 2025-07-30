# BuyXanBot - Multi-Chain Token Purchase Detection Bot

🤖 **BuyXanBot** is an advanced Telegram bot that detects token purchases on multiple blockchains (Ethereum, Solana, BNB Chain, Base) and sends custom alerts with rich formatting, custom GIFs, and real-time monitoring.

![BuyXanBot Banner](https://i.ibb.co/p66SKGRV/BLABLA.png)

## 🌟 Key Features

- **🔍 Real-Time Monitoring**: Continuous transaction monitoring every 10 seconds across multiple blockchains
- **⚡ Multi-Chain Support**: Ethereum, Solana, BNB Chain, and Base networks
- **🎨 Customizable Alerts**: Custom GIFs (URL or Telegram), emojis, stickers, and 5 message templates
- **🆓 Free APIs**: Uses DexScreener, CoinGecko, and public blockchain explorers
- **📊 Rich Analytics**: Supply percentage, market data, visual progress bars, and momentum indicators
- **🎯 Smart Filtering**: Configurable minimum amounts ($25-$2500+), quiet hours, and whale mode
- **👥 Group Support**: Works in both private chats and Telegram groups
- **🎭 Multiple Templates**: Classic, Minimal, Whale, Promotional, and Technical formats
- **📱 Interactive Interface**: Full button-based navigation with inline keyboards

## 🚀 Quick Start

### Prerequisites

- Node.js 18+ 
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Optional: API keys for enhanced features

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ThesirionOne/BuyXanBot.git
   cd BuyXanBot
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Start the bot**
   ```bash
   npm start
   ```

## 📋 Bot Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Initialize bot and show main menu | `/start` |
| `/addtoken` | Add token to monitor | `/addtoken ETH 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984` |
| `/removetoken` | Remove token from monitoring | `/removetoken ETH 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984` |
| `/listtokens` | View all monitored tokens | `/listtokens` |
| `/setgif` | Set custom GIF for alerts | `/setgif https://media.giphy.com/media/example.gif` |
| `/setemoji` | Set custom emoji | `/setemoji 💰` |
| `/setmotto` | Set custom motto/branding | `/setmotto "🚀 To The Moon!"` |
| `/test` | Send test purchase alert | `/test` |
| `/stop` | Stop bot monitoring | `/stop` |
| `/help` | Show help information | `/help` |

## 🎮 Interactive Interface

BuyXanBot features a complete button-based interface for easy navigation:

### **🏠 Main Menu:**
- 🪙 **Manage Tokens** - Add, remove, and view monitored tokens
- ⚙️ **Settings** - Customize GIFs, emojis, templates, and filters
- 🏆 **TOP TOKENS** - Browse featured tokens across all chains
- 📊 **View Stats** - See bot statistics and usage data
- ❓ **Help** - Access help information with visual banner

### **🪙 Token Management:**
- ➕ **Add Token** - Select chain and enter contract address
- 📋 **List Tokens** - View all monitored tokens by chain
- 🗑️ **Remove Token** - Select and remove specific tokens
- 🔍 **Token Info** - Get detailed token information

### **⚙️ Settings Menu:**
- 🎬 **Custom GIF** - Set from URL or Telegram library
- 😊 **Custom Emoji** - Standard, premium, animated, or stickers
- 📝 **Custom Motto** - Add personalized branding text
- 🎭 **Message Templates** - Choose from 5 different formats
- 💰 **Purchase Filters** - Set minimum amounts and conditions
- 🚀 **START/STOP BOT** - Control monitoring status

## 🔗 Supported Blockchains

| Chain | Symbol | Network | Token Standard |
|-------|--------|---------|----------------|
| Ethereum | ETH | Mainnet | ERC-20 |
| Solana | SOL | Mainnet | SPL |
| BNB Chain | BNB | BSC | BEP-20 |
| Base | ETH | Base | ERC-20 |

## 🎨 Message Templates

Choose from 5 professionally designed message templates:

### **🤖 Classic Template (Default)**
- Complete information with visual progress bars
- Supply percentage indicators
- Market momentum badges
- Rich formatting with emojis and separators

### **📱 Minimal Template**
- Compact format for essential information only
- Perfect for high-frequency alerts
- Clean and simple presentation

### **🐋 Whale Template**
- Designed for large purchases ($1000+)
- Premium styling with enhanced visuals
- Focus on buyer information and value

### **🚀 Promotional Template**
- Eye-catching format for marketing
- Emphasis on "Don't miss out" messaging
- Perfect for promoting specific tokens

### **📊 Technical Template**
- Detailed data for advanced traders
- Complete transaction information
- Market metrics and wallet analysis

## 🎯 Purchase Filtering

Configure smart filters to control which purchases trigger alerts:

### **💰 Minimum Amount Filters:**
- **$25+** - Small purchases (all significant buys)
- **$150+** - Medium purchases (meaningful investments) 
- **$1,500+** - Big purchases (substantial investments)
- **$2,500+** - Whale purchases (biggest players only)

### **⏰ Quiet Hours:**
- Set specific hours to pause notifications
- Configurable start/end times in UTC
- Perfect for avoiding alerts during sleep

### **🐋 Whale Mode:**
- Only show purchases above $1,000
- Focus on the most significant transactions
- Reduce notification frequency

## 🛠️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Required
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# Optional - Enhanced Features
DISABLE_BOT=false
NODE_ENV=production

# Optional - For enhanced features
ETHERSCAN_API_KEY=your_etherscan_api_key
BSCSCAN_API_KEY=your_bscscan_api_key
BASESCAN_API_KEY=your_basescan_api_key

# Server Configuration
PORT=3000
NODE_ENV=production
```

### **🎬 Custom GIF Setup:**
1. **From URL:** Any direct link to a GIF file
2. **From Telegram:** Send any GIF from your library to the bot
3. **Stickers:** Use stickers as unique visual elements

### **😊 Custom Emoji Options:**
- **Standard:** Classic emoji selection (🟢, 💎, 🚀, etc.)
- **Premium:** Enhanced combinations (💎✨, 🚀🔥, etc.)
- **Animated:** Multi-emoji effects (🔥🔥🔥, ⚡⚡⚡)
- **Dynamic:** Auto-changing based on value/time/chain
- **Stickers:** Use any Telegram sticker as emoji

### Free APIs Used

- **DexScreener API**: Token prices and trading data
- **CoinGecko API**: Cryptocurrency market data
- **Blockchain Explorers**: Transaction data (Etherscan, BSCScan, etc.)

## 📊 Project Structure

```
BuyXanBot/
├── 🤖 bot/                    # Core bot functionality
│   ├── config.js              # Chain configs & templates
│   ├── telegram.js            # Telegram API integration
│   ├── commands.js            # Command handlers (/start, /help, etc.)
│   ├── callback-handlers.js   # Button interaction handlers
│   ├── blockchain.js          # Real-time monitoring logic
│   ├── formatters.js          # Message formatting & templates
│   ├── free-apis.js           # DexScreener & API integrations
│   └── keyboards.js           # Interactive button layouts
├── 💾 database/               # In-memory data storage
│   ├── init.js               # Database initialization
│   └── queries.js            # Data operations
├── 🌐 public/                # Web interface
│   ├── index.html           # Landing page
│   └── admin.html           # Admin dashboard
├── ⚙️ server.js              # Main server & cron jobs
└── 📚 Documentation files
```

```
BuyXanBot/
├── bot/                    # Bot logic and handlers
│   ├── config.js          # Chain configurations
│   ├── telegram.js        # Telegram API integration
│   ├── commands.js        # Command handlers
│   ├── blockchain.js      # Blockchain monitoring
│   ├── formatters.js      # Message formatting
│   ├── free-apis.js       # Free API integrations
│   ├── keyboards.js       # Inline keyboards
│   └── callback-handlers.js # Callback query handlers
├── database/              # Database operations
│   ├── init.js           # Database initialization
│   └── queries.js        # Database queries
├── public/               # Web interface
│   ├── index.html       # Landing page
│   └── admin.html       # Admin panel
├── supabase/            # Supabase configuration
│   ├── migrations/      # Database migrations
│   └── functions/       # Edge functions
├── server.js            # Main server file
├── app.py              # Python reference implementation
└── README.md           # This file
```

## 🎯 Usage Examples

### **📱 Getting Started:**
1. Send `/start` to the bot
2. Click "🪙 Manage Tokens" 
3. Click "➕ Add Token"
4. Select blockchain (ETH, SOLANA, BNB, BASE)
5. Send contract address
6. Click "🚀 START BUY BOT"

### **🎨 Customization:**
1. Click "⚙️ Settings" from main menu
2. **For GIF:** Click "🎬 Set Custom GIF" → Choose URL or Telegram
3. **For Emoji:** Click "😊 Set Custom Emoji" → Select type and emoji
4. **For Template:** Click "📝 Message Template" → Choose style
5. **For Filters:** Click "💰 Purchase Filter" → Set minimum amount

### **🧪 Testing:**
1. Configure your settings
2. Click "🧪 Test Purchase Alert" 
3. Review the formatted message
4. Adjust settings if needed
5. Start monitoring with "🚀 START BUY BOT"

### **🏆 Browse Featured Tokens:**
1. Click "🏆 TOP TOKENS" from main menu
2. Select blockchain to explore
3. View promoted and community tokens
4. Click "➕ Monitorizar Token" to add directly

## 🚀 Deployment

### Railway (Recommended)

1. Fork this repository
2. Connect to [Railway](https://railway.app)
3. Add environment variables
4. Deploy automatically

### Docker

```bash
# Build image
docker build -t buyxanbot .

# Run container
docker run -d --name buyxanbot -p 3000:3000 --env-file .env buyxanbot
```

### Manual Deployment

1. Clone repository on your server
2. Install dependencies: `npm install`
3. Configure environment variables
4. Start with PM2: `pm2 start server.js --name buyxanbot`

## 🔧 Advanced Configuration

### **🎭 Custom Templates:**
Edit `bot/formatters.js` to create custom message formats:
- Modify existing templates
- Add new template types
- Customize visual elements and progress bars

### **⛓️ Adding New Chains:**
1. Update `bot/config.js` with chain configuration
2. Add API integration in `bot/free-apis.js`
3. Update formatters and keyboards
4. Test thoroughly before deployment

### **🔍 Monitoring Frequency:**
Default: Every 10 seconds (configurable in `server.js` cron schedule)

## 🎯 Usage Examples

### Adding Tokens

```bash
# Add Ethereum token
/addtoken ETH 0x6982508145454Ce325dDbE47a25d4ec3d2311933

# Add Solana token  
/addtoken SOLANA EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v

# Add BNB Chain token
/addtoken BNB 0x55d398326f99059fF775485246999027B3197955
```

### Customization

```bash
# Set custom GIF
/setgif https://media.giphy.com/media/your-gif.gif

# Set custom emoji
/setemoji 🚀

# Test configuration
/test
```

## 📈 Performance & Monitoring

### **⚡ Real-time Features:**
- **Monitoring Frequency:** Every 10 seconds
- **API Rate Limiting:** Smart throttling to prevent abuse
- **Response Time:** < 2 seconds for commands
- **Memory Usage:** ~50MB typical

### **📊 Built-in Analytics:**
- Total chats using the bot
- Total tokens being monitored
- Purchase alerts sent
- Chain distribution statistics

### **🔍 Debugging Features:**
- Comprehensive console logging
- Error handling with fallbacks
- Rate limiting status tracking
- API response monitoring

## 🎨 Visual Features

- **📊 Progress Bars:** Visual representation of purchase sizes
- **🎯 Supply Indicators:** Show percentage of token supply purchased
- **⚡ Momentum Badges:** Display market activity status
- **🎨 Dynamic Emojis:** Scale emoji count based on purchase value
- **📱 Responsive Design:** Works perfectly on mobile and desktop

## 📈 Features in Detail

### Real-Time Monitoring
- Monitors blockchain transactions every 10 seconds
- Detects token purchases using smart heuristics
- Filters out small transactions to prevent spam
- Uses free APIs to minimize costs
- Implements rate limiting for API protection

### Multi-Chain Support
- Native support for 4 major blockchains
- Automatic chain detection and configuration
- Optimized API calls for each network
- Chain-specific formatting and links
- Unified interface across all chains

### Customizable Alerts
- 5 different message templates
- Custom GIF and emoji support
- Configurable purchase filters
- Quiet hours functionality

### Interactive Interface
- Complete button-based navigation
- No need to remember commands
- Visual feedback and confirmations
- Intuitive menu structure

### Smart Filtering
- Minimum purchase amount filtering
- Whale mode for large transactions only
- Time-based filtering (quiet hours)
- Rate limiting to prevent API abuse

## 🔧 Development

### **🚀 Quick Development Setup:**
```bash
# Clone and setup
git clone <repository-url>
cd BuyXanBot
npm install
cp .env.example .env
# Edit .env with your bot token
npm run dev
```

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/ThesirionOne/BuyXanBot.git
cd BuyXanBot

# Install dependencies
npm install

# Start development server
npm run dev
```

### **🧪 Testing Features:**
- Use `/test` command to preview alerts
- Test different templates and settings
- Verify button interactions
- Check API integrations

### **📝 Code Structure:**
- **Modular design** with clear separation of concerns
- **ES6 modules** with proper imports/exports
- **Comprehensive error handling** throughout
- **Extensive logging** for debugging

### Adding New Chains

1. Update `bot/config.js` with new chain configuration
2. Add API integration in `bot/free-apis.js`
3. Update formatters and keyboards as needed
4. Test thoroughly before deployment

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit a Pull Request

## 🔒 Security & Privacy

### **🛡️ Security Features:**
- Environment variables for sensitive data
- Rate limiting on all API calls
- Input validation on user inputs
- Secure webhook handling
- No sensitive data stored in memory

### **🔐 Privacy:**
- Only stores necessary configuration data
- No personal information collected
- Temporary in-memory storage only
- No data persistence between restarts

## 📝 API Documentation

### Webhook Endpoint

```
POST /api/telegram/webhook
```

Receives Telegram updates and processes bot commands.

### Admin API

```
GET /api/admin/configs    # Get all bot configurations
GET /api/admin/stats      # Get bot statistics
```

## 🔒 Security

- Environment variables for sensitive data
- Rate limiting on API calls
- Input validation on all user inputs
- Secure webhook handling

## 🎯 Use Cases

### **👥 For Communities:**
- Monitor community token purchases
- Share buy alerts in Telegram groups
- Build excitement around token activity
- Track whale movements

### **📈 For Traders:**
- Get instant notifications of significant buys
- Monitor multiple tokens across chains
- Filter by purchase size and timing
- Technical analysis with detailed data

### **🚀 For Projects:**
- Promote your token with custom branding
- Show purchase activity to build confidence
- Use promotional templates for marketing
- Track adoption and trading activity

## 🐛 Troubleshooting

### Common Issues

**Bot not responding:**
- Check TELEGRAM_BOT_TOKEN is correct
- Verify bot is running: `pm2 status`
- Restart the bot: `npm run dev`
- Check console logs for errors

- Check logs: `pm2 logs buyxanbot`

**No purchase alerts:**
- Verify tokens are added correctly
- Check API rate limits
- Ensure minimum purchase amount is not too high
- Verify bot is active (green status)
- Check if tokens are properly added
- Test with `/test` command first


**API Errors:**
- Check API key configuration
- Verify network connectivity
- Monitor rate limiting

## 📊 Performance

### **⚡ Optimized Performance:**
- **Smart Caching:** Reduces API calls with intelligent rate limiting
- **Efficient Polling:** Only checks active tokens with recent activity
- **Memory Management:** Automatic cleanup of old data
- **Error Recovery:** Graceful handling of API failures

### **📈 Scalability:**
- **Multi-chat Support:** Handle unlimited Telegram chats
- **Chain Agnostic:** Easy to add new blockchains
- **Template System:** Flexible message formatting
- **Modular Architecture:** Easy to extend and maintain

- **Response Time**: < 2 seconds for commands
- **Monitoring Frequency**: Every 10 seconds
- **API Calls**: Optimized with rate limiting
- **Memory Usage**: ~50MB typical
- **Uptime**: 99.9% with proper deployment

## 🌟 Recent Updates

### **v1.2.0 - Enhanced User Experience**
- ✅ **Supply Percentage Metrics:** Show % of token supply purchased
- ✅ **Visual Progress Bars:** Dynamic bars based on purchase size
- ✅ **Help Banner Images:** Professional branding in help sections
- ✅ **Improved Templates:** Enhanced formatting and visual elements
- ✅ **Better Error Handling:** More robust API error management

### **v1.1.0 - Interactive Interface**
- ✅ **Button Navigation:** Complete inline keyboard system
- ✅ **Multiple Templates:** 5 different message formats
- ✅ **Custom Branding:** Mottos, GIFs, and emoji customization
- ✅ **Smart Filtering:** Advanced purchase filtering options

## 🤝 Support

- **Telegram**: [@ThesirionOne](https://t.me/ThesirionOne)
- **Issues**: [GitHub Issues](https://github.com/ThesirionOne/BuyXanBot/issues)
- **Documentation**: [Wiki](https://github.com/ThesirionOne/BuyXanBot/wiki)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Free API Providers:**
  - **DexScreener** for comprehensive token data
  - **CoinGecko** for cryptocurrency market information
  - **Blockchain Explorers** for transaction data
  - **Telegram** for the excellent Bot API

- **DexScreener** for providing free token data API
- **CoinGecko** for cryptocurrency market data
- **Telegram** for the Bot API
- **The crypto community** for inspiration and feedback

## 🔮 Roadmap

### **🎯 Planned Features:**
- [ ] **WebSocket Integration** for real-time data
- [ ] **Machine Learning** for better purchase detection
- [ ] **Mobile App** companion
- [ ] **Advanced Analytics** dashboard
- [ ] **Multi-language Support** (Spanish, French, etc.)
- [ ] **NFT Purchase Detection** across chains
- [ ] **DeFi Protocol Integration** (Uniswap, PancakeSwap)
- [ ] **Portfolio Tracking** features

- [ ] WebSocket integration for real-time data
- [ ] Machine learning for better purchase detection
- [ ] Mobile app companion
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] NFT purchase detection
- [ ] DeFi protocol integration

---

**Made with ❤️ for the crypto community by [TeamXanders](https://t.me/XandersOGCALLS) & [Thesirion](https://thesirion.io)**

⭐ **Star this repository if you find it useful!**