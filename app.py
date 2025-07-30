# app.py - BuyXanBot Python Implementation
# This is a Python version of the BuyXanBot for reference and testing purposes
# The main implementation uses Node.js (see server.js and bot/ directory)

import os
import json
import requests
from datetime import datetime
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Configuration ---
# Environment variables (should be set in your deployment environment)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8209650246:AAH8OEEWFmvI1RMqilzU5DOHWRgmcTdPiLY")
ALCHEMY_API_KEY_ETH = os.getenv("ALCHEMY_API_KEY_ETH", "your_alchemy_eth_api_key")
ALCHEMY_API_KEY_BASE = os.getenv("ALCHEMY_API_KEY_BASE", "your_alchemy_base_api_key")
MORALIS_API_KEY = os.getenv("MORALIS_API_KEY", "your_moralis_api_key")
HELIUS_API_KEY = os.getenv("HELIUS_API_KEY", "your_helius_solana_api_key")

# Supported chains configuration
SUPPORTED_CHAINS = {
    'ETH': {
        'name': 'Ethereum',
        'symbol': 'ETH',
        'explorer': 'https://etherscan.io',
        'rpc_url': f'https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY_ETH}',
        'native_price': 3500  # Placeholder - should be fetched from price API
    },
    'SOLANA': {
        'name': 'Solana',
        'symbol': 'SOL',
        'explorer': 'https://solscan.io',
        'rpc_url': f'https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}',
        'native_price': 150
    },
    'BNB': {
        'name': 'BNB Chain',
        'symbol': 'BNB',
        'explorer': 'https://bscscan.com',
        'rpc_url': 'https://bsc-dataseed.binance.org/',
        'native_price': 600
    },
    'BASE': {
        'name': 'Base',
        'symbol': 'ETH',
        'explorer': 'https://basescan.org',
        'rpc_url': f'https://base-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY_BASE}',
        'native_price': 3500
    }
}

# --- Mock Database (In production, use a real database like Supabase) ---
# This simulates the bot_configs table structure
bot_configs = {
    # Example structure:
    # chat_id: {
    #     'watched_tokens': {
    #         'ETH': ['0xContractAddress1', '0xContractAddress2'],
    #         'BNB': ['0xContractAddress3']
    #     },
    #     'custom_gif_url': 'https://example.com/buy_gif.gif',
    #     'custom_emoji': '💸'
    # }
}

# --- Telegram API Functions ---
def send_telegram_message(chat_id, text, parse_mode="HTML", reply_markup=None):
    """Send a text message to a Telegram chat."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": parse_mode
    }
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Message sent to {chat_id}: Success")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending message to {chat_id}: {e}")
        return None

def send_telegram_animation(chat_id, animation_url):
    """Send an animation (GIF) to a Telegram chat."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendAnimation"
    payload = {
        "chat_id": chat_id,
        "animation": animation_url
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Animation sent to {chat_id}: Success")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending animation to {chat_id}: {e}")
        return None

def set_telegram_webhook(webhook_url):
    """Set the webhook URL for the Telegram bot."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setWebhook"
    payload = {"url": webhook_url}
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Webhook set: {response.json()}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error setting webhook: {e}")
        return None

# --- Blockchain Interaction Functions ---
def get_latest_token_purchases(chain, contract_addresses):
    """
    Simulate getting the latest token purchases for a chain and contracts.
    In a real implementation, this would interact with blockchain APIs.
    """
    purchases = []
    logger.info(f"Simulating purchase detection for {chain} contracts: {contract_addresses}")

    # Simulation logic - in production, integrate with real blockchain APIs
    for contract_address in contract_addresses:
        # Simulate a 10% chance of finding a purchase per contract
        if len(contract_addresses) > 0 and hash(contract_address) % 10 == 0:
            purchase = generate_mock_purchase(chain, contract_address)
            purchases.append(purchase)
            logger.info(f"Mock purchase generated for {contract_address} on {chain}")
    
    return purchases

def generate_mock_purchase(chain, contract_address):
    """Generate mock purchase data for testing."""
    chain_config = SUPPORTED_CHAINS.get(chain, SUPPORTED_CHAINS['ETH'])
    
    # Generate realistic mock data
    native_amount = round(0.1 + (hash(contract_address) % 100) / 20, 3)  # 0.1 to 5.1
    token_amount = 1000 + (hash(contract_address) % 50000)  # 1000 to 51000
    
    return {
        'token_name': f'Mock{chain}Token',
        'token_symbol': f'M{chain[:3]}T',
        'token_address': contract_address,
        'chain': chain,
        'native_amount': native_amount,
        'token_amount': token_amount,
        'buyer_address': generate_mock_address(chain),
        'txn_hash': generate_mock_tx_hash(chain),
        'timestamp': datetime.now().timestamp(),
        'price_usd': round(0.01 + (hash(contract_address) % 1000) / 100, 4),
        'market_cap_usd': 100000 + (hash(contract_address) % 900000),
        'total_supply': 1000000000
    }

def generate_mock_address(chain):
    """Generate a mock wallet address for the given chain."""
    if chain == 'SOLANA':
        # Solana addresses are base58 encoded, typically 44 characters
        return 'So11111111111111111111111111111111111111112'
    else:
        # Ethereum-style addresses (ETH, BNB, BASE)
        return '0x' + ''.join([hex(i % 16)[2:] for i in range(40)])

def generate_mock_tx_hash(chain):
    """Generate a mock transaction hash for the given chain."""
    if chain == 'SOLANA':
        # Solana transaction signatures are typically 88 characters
        return ''.join([hex(i % 16)[2:] for i in range(88)])
    else:
        # Ethereum-style transaction hashes
        return '0x' + ''.join([hex(i % 16)[2:] for i in range(64)])

def get_token_price_and_market_cap(token_address, chain):
    """
    Get current token price, market cap, and total supply.
    This would require a market data API (e.g., CoinGecko, CoinMarketCap, Moralis).
    """
    logger.info(f"Getting price/MC for {token_address} on {chain}")
    
    # Mock data based on contract address hash for consistency
    address_hash = hash(token_address)
    return {
        'price_usd': round(0.01 + (address_hash % 1000) / 1000, 4),
        'market_cap_usd': 100000 + (address_hash % 10000000),
        'total_supply': 1000000000 + (address_hash % 1000000000)
    }

def get_wallet_token_balance(wallet_address, token_address, chain):
    """
    Get the balance of a specific token for a given wallet.
    This would require a blockchain API (e.g., Alchemy, Moralis).
    """
    logger.info(f"Getting balance for {wallet_address} of token {token_address} on {chain}")
    
    # Mock balance based on wallet and token hash
    balance_hash = hash(wallet_address + token_address)
    return 10000 + (balance_hash % 90000)  # Mock balance between 10k-100k

# --- Message Formatting ---
def format_purchase_message(purchase_data, config):
    """Format purchase data into a rich HTML Telegram message."""
    token_name = purchase_data.get('token_name', 'Unknown Token')
    token_symbol = purchase_data.get('token_symbol', 'TOK')
    chain = purchase_data.get('chain', 'ETH')
    native_amount = purchase_data.get('native_amount', 0)
    token_amount = purchase_data.get('token_amount', 0)
    buyer_address = purchase_data.get('buyer_address', 'N/A')
    txn_hash = purchase_data.get('txn_hash', 'N/A')
    token_address = purchase_data.get('token_address', 'N/A')

    # Get additional token information
    token_info = get_token_price_and_market_cap(token_address, chain)
    price_usd = token_info.get('price_usd', 0)
    market_cap_usd = token_info.get('market_cap_usd', 0)
    total_supply = token_info.get('total_supply', 0)

    # Get chain configuration
    chain_config = SUPPORTED_CHAINS.get(chain, SUPPORTED_CHAINS['ETH'])
    native_symbol = chain_config['symbol']
    explorer_url = chain_config['explorer']
    native_price = chain_config['native_price']
    
    # Calculate USD value
    usd_value = native_amount * native_price

    # Custom emojis based on purchase size
    custom_emoji = config.get('custom_emoji', '🟢')
    emoji_count = min(max(int(usd_value / 100), 1), 20)  # 1-20 emojis based on USD value
    emojis = custom_emoji * emoji_count

    # Calculate wallet position
    wallet_balance = get_wallet_token_balance(buyer_address, token_address, chain)
    position_percent = (wallet_balance / total_supply) * 100 if total_supply > 0 else 0

    # Format addresses for display
    short_buyer = f"{buyer_address[:6]}...{buyer_address[-4:]}" if len(buyer_address) > 10 else buyer_address
    
    # Build chart and trade links
    chart_link = build_chart_link(chain, token_address)
    trade_link = build_trade_link(chain, token_address)

    # Construct the message
    message = f"<b>{token_name}</b> ({token_symbol}) Buy!\n\n"
    message += f"{emojis}\n\n"
    message += f"💵 {native_amount:.3f} {native_symbol} (${usd_value:,.2f})\n"
    message += f"🪙 {token_amount:,.0f} {token_symbol}\n"
    message += f"🔷 <a href='{explorer_url}/address/{buyer_address}'>{short_buyer}</a> | "
    message += f"Txn <a href='{explorer_url}/tx/{txn_hash}'>🔗</a>\n"
    message += f"🔼 Position +{position_percent:.1f}%\n"
    message += f"🔼 Market Cap ${market_cap_usd:,.0f}\n\n"
    message += f"📊 <a href='{chart_link}'>Chart</a>\n"
    message += f"🦄 <a href='{trade_link}'>Trade</a>\n"
    message += "🔹 <a href='https://t.me/buyxanbot'>Join Community</a>"

    return message

def build_chart_link(chain, token_address):
    """Build chart link for the token."""
    base_url = 'https://www.geckoterminal.com'
    chain_mapping = {
        'ETH': 'eth',
        'SOLANA': 'solana',
        'BNB': 'bsc',
        'BASE': 'base'
    }
    chain_slug = chain_mapping.get(chain, 'eth')
    return f"{base_url}/{chain_slug}/pools/{token_address}"

def build_trade_link(chain, token_address):
    """Build trade link for the token."""
    if chain == 'SOLANA':
        return f"https://jup.ag/swap/SOL-{token_address}"
    elif chain == 'BNB':
        return f"https://pancakeswap.finance/swap?outputCurrency={token_address}"
    else:  # ETH, BASE
        chain_param = 'ethereum' if chain == 'ETH' else 'base'
        return f"https://app.uniswap.org/swap?chain={chain_param}&outputCurrency={token_address}"

# --- Command Handlers ---
def handle_start_command(chat_id):
    """Handle the /start and /help commands."""
    welcome_message = """
🚀 <b>¡Bienvenido a BuyXanBot!</b>

Soy tu bot de detección de compras de tokens multi-cadena. Puedo monitorizar compras de tokens en Ethereum, Solana, BNB Chain y Base.

<b>📋 Comandos disponibles:</b>
• /addtoken [CADENA] [CONTRATO] - Añadir token a monitorizar
• /removetoken [CADENA] [CONTRATO] - Eliminar token del monitoreo
• /listtokens - Mostrar todos los tokens monitorizados
• /setgif [URL] - Establecer GIF personalizado para alertas
• /setemoji [EMOJI] - Establecer emoji personalizado
• /help - Mostrar esta ayuda

<b>🔗 Cadenas soportadas:</b>
• ETH (Ethereum)
• SOLANA (Solana)
• BNB (BNB Chain)
• BASE (Base)

<b>📝 Ejemplo de uso:</b>
<code>/addtoken ETH 0x1234567890abcdef1234567890abcdef12345678</code>
<code>/setgif https://media.giphy.com/media/your-gif.gif</code>
<code>/setemoji 💰</code>

¡Listo para empezar a monitorizar! 🎯
"""
    
    send_telegram_message(chat_id, welcome_message)
    
    # Initialize bot configuration if it doesn't exist
    if chat_id not in bot_configs:
        bot_configs[chat_id] = {
            'watched_tokens': {'ETH': [], 'SOLANA': [], 'BNB': [], 'BASE': []},
            'custom_gif_url': None,
            'custom_emoji': '🟢'
        }

def handle_addtoken_command(chat_id, args):
    """Handle the /addtoken command."""
    if len(args) != 2:
        send_telegram_message(chat_id, 
            "❌ <b>Uso incorrecto.</b>\n\n"
            "Uso: <code>/addtoken [CADENA] [DIRECCION_CONTRATO]</code>\n"
            "Ejemplo: <code>/addtoken ETH 0x1234567890abcdef1234567890abcdef12345678</code>"
        )
        return

    chain = args[0].upper()
    contract_address = args[1]

    if chain not in SUPPORTED_CHAINS:
        send_telegram_message(chat_id, 
            f"❌ <b>Cadena no soportada:</b> {chain}\n\n"
            "Cadenas soportadas: ETH, SOLANA, BNB, BASE"
        )
        return

    # Initialize config if needed
    if chat_id not in bot_configs:
        bot_configs[chat_id] = {
            'watched_tokens': {'ETH': [], 'SOLANA': [], 'BNB': [], 'BASE': []},
            'custom_gif_url': None,
            'custom_emoji': '🟢'
        }

    if contract_address not in bot_configs[chat_id]['watched_tokens'][chain]:
        bot_configs[chat_id]['watched_tokens'][chain].append(contract_address)
        send_telegram_message(chat_id, 
            f"✅ <b>¡Token añadido exitosamente!</b>\n\n"
            f"🔗 Cadena: <b>{chain}</b>\n"
            f"📄 Contrato: <code>{contract_address}</code>\n\n"
            "¡Ahora monitorizaré las compras de este token! 🎯"
        )
    else:
        send_telegram_message(chat_id, 
            f"⚠️ <b>Token ya monitorizado</b>\n\n"
            f"Este token ya está siendo monitorizado en {chain}."
        )

def handle_removetoken_command(chat_id, args):
    """Handle the /removetoken command."""
    if len(args) != 2:
        send_telegram_message(chat_id, 
            "❌ <b>Uso incorrecto.</b>\n\n"
            "Uso: <code>/removetoken [CADENA] [DIRECCION_CONTRATO]</code>\n"
            "Ejemplo: <code>/removetoken ETH 0x1234567890abcdef1234567890abcdef12345678</code>"
        )
        return

    chain = args[0].upper()
    contract_address = args[1]

    if chain not in SUPPORTED_CHAINS:
        send_telegram_message(chat_id, 
            f"❌ <b>Cadena no soportada:</b> {chain}\n\n"
            "Cadenas soportadas: ETH, SOLANA, BNB, BASE"
        )
        return

    if (chat_id not in bot_configs or 
        contract_address not in bot_configs[chat_id]['watched_tokens'].get(chain, [])):
        send_telegram_message(chat_id, 
            f"⚠️ <b>Token no encontrado</b>\n\n"
            f"Este token no está siendo monitorizado en {chain}."
        )
        return

    bot_configs[chat_id]['watched_tokens'][chain].remove(contract_address)
    send_telegram_message(chat_id, 
        f"✅ <b>¡Token eliminado exitosamente!</b>\n\n"
        f"🔗 Cadena: <b>{chain}</b>\n"
        f"📄 Contrato: <code>{contract_address}</code>\n\n"
        "Ya no monitorizaré este token. 🗑️"
    )

def handle_listtokens_command(chat_id):
    """Handle the /listtokens command."""
    if chat_id not in bot_configs:
        send_telegram_message(chat_id, 
            "📋 <b>No hay tokens siendo monitorizados</b>\n\n"
            "Usa /addtoken para añadir tokens a monitorizar.\n\n"
            "Ejemplo: <code>/addtoken ETH 0x1234567890abcdef1234567890abcdef12345678</code>"
        )
        return

    watched_tokens = bot_configs[chat_id]['watched_tokens']
    total_tokens = sum(len(tokens) for tokens in watched_tokens.values())
    
    if total_tokens == 0:
        send_telegram_message(chat_id, 
            "📋 <b>No hay tokens siendo monitorizados</b>\n\n"
            "Usa /addtoken para añadir tokens a monitorizar.\n\n"
            "Ejemplo: <code>/addtoken ETH 0x1234567890abcdef1234567890abcdef12345678</code>"
        )
        return

    message = "📋 <b>Tokens Monitorizados:</b>\n\n"
    
    for chain, tokens in watched_tokens.items():
        if tokens:
            message += f"🔗 <b>{chain}:</b>\n"
            for token in tokens:
                message += f"  • <code>{token}</code>\n"
            message += "\n"
    
    message += f"<i>Total: {total_tokens} token(s) monitorizados</i>"
    send_telegram_message(chat_id, message)

def handle_setgif_command(chat_id, args):
    """Handle the /setgif command."""
    if len(args) != 1:
        send_telegram_message(chat_id, 
            "❌ <b>Uso incorrecto.</b>\n\n"
            "Uso: <code>/setgif [URL_GIF]</code>\n"
            "Ejemplo: <code>/setgif https://media.giphy.com/media/your-gif.gif</code>"
        )
        return

    gif_url = args[0]
    
    if chat_id not in bot_configs:
        bot_configs[chat_id] = {
            'watched_tokens': {'ETH': [], 'SOLANA': [], 'BNB': [], 'BASE': []},
            'custom_gif_url': None,
            'custom_emoji': '🟢'
        }
    
    bot_configs[chat_id]['custom_gif_url'] = gif_url
    send_telegram_message(chat_id, 
        f"✅ <b>¡GIF personalizado establecido exitosamente!</b>\n\n"
        f"🎬 URL del GIF: <a href='{gif_url}'>Vista previa</a>\n\n"
        "¡Este GIF se enviará antes de cada alerta de compra! 🎯"
    )

def handle_setemoji_command(chat_id, args):
    """Handle the /setemoji command."""
    if len(args) != 1:
        send_telegram_message(chat_id, 
            "❌ <b>Uso incorrecto.</b>\n\n"
            "Uso: <code>/setemoji [EMOJI]</code>\n"
            "Ejemplo: <code>/setemoji 💰</code>"
        )
        return

    emoji = args[0]
    
    if chat_id not in bot_configs:
        bot_configs[chat_id] = {
            'watched_tokens': {'ETH': [], 'SOLANA': [], 'BNB': [], 'BASE': []},
            'custom_gif_url': None,
            'custom_emoji': '🟢'
        }
    
    bot_configs[chat_id]['custom_emoji'] = emoji
    send_telegram_message(chat_id, 
        f"✅ <b>¡Emoji personalizado establecido exitosamente!</b>\n\n"
        f"😊 Emoji: {emoji}\n\n"
        "¡Este emoji se usará en las alertas de compra! 🎯"
    )

# --- Main Webhook Handler ---
def handle_telegram_webhook(request_body):
    """
    Process incoming Telegram updates (webhooks).
    This would be the main entry point for your serverless function.
    """
    try:
        if isinstance(request_body, str):
            update = json.loads(request_body)
        else:
            update = request_body
            
        logger.info(f"Telegram update received: {update}")

        if "message" in update:
            message = update["message"]
            chat_id = message["chat"]["id"]
            text = message.get("text", "")

            if text.startswith("/"):
                # Parse command and arguments
                command_parts = text.split(" ", 1)
                command = command_parts[0].lower()
                args = command_parts[1].split(" ") if len(command_parts) > 1 else []

                # Route to appropriate handler
                if command in ["/start", "/help"]:
                    handle_start_command(chat_id)
                elif command == "/addtoken":
                    handle_addtoken_command(chat_id, args)
                elif command == "/removetoken":
                    handle_removetoken_command(chat_id, args)
                elif command == "/listtokens":
                    handle_listtokens_command(chat_id)
                elif command == "/setgif":
                    handle_setgif_command(chat_id, args)
                elif command == "/setemoji":
                    handle_setemoji_command(chat_id, args)
                else:
                    send_telegram_message(chat_id, 
                        "❌ Comando desconocido. Usa /help para ver los comandos disponibles."
                    )

        return {"statusCode": 200, "body": "OK"}
    except Exception as e:
        logger.error(f"Error in handle_telegram_webhook: {e}")
        return {"statusCode": 500, "body": f"Internal server error: {e}"}

# --- Blockchain Monitoring Loop ---
def monitor_all_chains_for_purchases():
    """
    Function that would be triggered periodically to monitor all chains
    and tokens configured in all chats.
    """
    logger.info("Starting blockchain monitoring...")
    
    for chat_id, config in bot_configs.items():
        watched_tokens = config.get('watched_tokens', {})
        for chain, contracts in watched_tokens.items():
            if contracts:
                logger.info(f"Monitoring {chain} for contracts: {contracts} for chat {chat_id}")
                purchases = get_latest_token_purchases(chain, contracts)
                
                for purchase in purchases:
                    logger.info(f"Purchase detected: {purchase}")
                    
                    # Send custom GIF if configured
                    if config.get('custom_gif_url'):
                        send_telegram_animation(chat_id, config['custom_gif_url'])
                    
                    # Send formatted message
                    message = format_purchase_message(purchase, config)
                    send_telegram_message(chat_id, message)
                    
                    # Small delay to avoid flooding Telegram API
                    time.sleep(1)
    
    logger.info("Blockchain monitoring completed.")

# --- Main Entry Point (for testing) ---
if __name__ == "__main__":
    print("🤖 BuyXanBot Python Implementation")
    print("=" * 50)
    
    # Simulate user interactions for testing
    print("\n--- Simulation: /start ---")
    handle_telegram_webhook({
        "update_id": 1,
        "message": {
            "chat": {"id": 12345, "type": "private"},
            "text": "/start"
        }
    })
    
    print("\n--- Simulation: /addtoken ETH 0xDummyEthToken ---")
    handle_telegram_webhook({
        "update_id": 2,
        "message": {
            "chat": {"id": 12345, "type": "private"},
            "text": "/addtoken ETH 0xDummyEthToken"
        }
    })
    
    print("\n--- Simulation: /addtoken SOLANA SolanaDummyToken ---")
    handle_telegram_webhook({
        "update_id": 3,
        "message": {
            "chat": {"id": 12345, "type": "private"},
            "text": "/addtoken SOLANA SolanaDummyToken"
        }
    })
    
    print("\n--- Simulation: /setgif https://media.giphy.com/media/v1.gif ---")
    handle_telegram_webhook({
        "update_id": 4,
        "message": {
            "chat": {"id": 12345, "type": "private"},
            "text": "/setgif https://media.giphy.com/media/v1.gif"
        }
    })
    
    print("\n--- Simulation: /setemoji 💰 ---")
    handle_telegram_webhook({
        "update_id": 5,
        "message": {
            "chat": {"id": 12345, "type": "private"},
            "text": "/setemoji 💰"
        }
    })
    
    print("\n--- Simulation: /listtokens ---")
    handle_telegram_webhook({
        "update_id": 6,
        "message": {
            "chat": {"id": 12345, "type": "private"},
            "text": "/listtokens"
        }
    })
    
    print("\n--- Simulation: Blockchain Monitoring ---")
    monitor_all_chains_for_purchases()
    
    print("\n✅ Conceptual demonstration completed.")
    print("\nNote: This is a Python reference implementation.")
    print("The main bot runs on Node.js (see server.js and bot/ directory).")
