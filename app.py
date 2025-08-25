// === NOUVELLES FONCTIONS ANALYSE FONDAMENTALE ===

        // Récupération des news crypto
        function fetchNews() {
            showStatus('📰 Récupération des news crypto...');
            
            const newsList = document.getElementById('news-list');
            const newsHTML = CRYPTO_SIGNALS_DB.news.map(news => `
                <div class="news-item">
                    <div class="news-title">${news.title}</div>
                    <div class="news-summary">${news.summary}</div>
                    <div class="news-meta">
                        <span class="news-source">${news.source}</span>
                        <span>${news.time}</span>
                    </div>
                </div>
            `).join('');
            
            newsList.innerHTML = newsHTML;
            showStatus('✅ News chargées');
        }

        // Mise à jour des métriques fondamentales
        function updateFundamentalMetrics() {
            // Simulation de données en temps réel
            const fearGreed = Math.floor(Math.random() * 100);
            const btcDom = (45 + Math.random() * 10).toFixed(1);
            const totalMcap = (2.1 + Math.random() * 0.5).toFixed(1);
            const defiTvl = (45 + Math.random() * 10).toFixed(0);
            
            document.getElementById('fear-greed').textContent = fearGreed;
            document.getElementById('btc-dominance').textContent = btcDom + '%';
            document.getElementById('total-mcap').textContent = '<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Crypto Sophistiqué</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/date-fns/2.29.3/index.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
            min-height: 100vh;
            overflow-x: hidden;
        }

        .navbar {
            background: rgba(15, 15, 35, 0.9);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .navbar h1 {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(45deg, #00d4ff, #7c3aed, #f59e0b);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { filter: brightness(1); }
            to { filter: brightness(1.2) drop-shadow(0 0 10px rgba(0, 212, 255, 0.3)); }
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .stat-card {
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02));
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            border-color: rgba(0, 212, 255, 0.5);
            box-shadow: 0 20px 40px rgba(0, 212, 255, 0.1);
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #00d4ff, #7c3aed, #f59e0b);
        }

        .stat-header {
            display: flex;
            justify-content: between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .stat-icon {
            width: 50px;
            height: 50px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .bitcoin-icon { background: linear-gradient(145deg, #f7931a, #ff6b35); }
        .ethereum-icon { background: linear-gradient(145deg, #627eea, #3c4ccd); }
        .solana-icon { background: linear-gradient(145deg, #00d18c, #7c3aed); }
        .nft-icon { background: linear-gradient(145deg, #ff6b6b, #ee5a24); }

        .stat-value {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .change-indicator {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-top: 1rem;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
        }

        .positive { background: rgba(34, 197, 94, 0.2); color: #22c55e; }
        .negative { background: rgba(239, 68, 68, 0.2); color: #ef4444; }

        .charts-section {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .chart-container {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
        }

        .chart-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 2rem;
            text-align: center;
        }

        .transactions-table {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
        }

        .table-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .transactions-list {
            max-height: 400px;
            overflow-y: auto;
        }

        .transaction-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
        }

        .transaction-item:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(0, 212, 255, 0.3);
        }

        .tx-hash {
            font-family: 'Monaco', monospace;
            color: #00d4ff;
            font-size: 0.8rem;
            margin-bottom: 0.5rem;
        }

        .tx-amount {
            font-size: 1.2rem;
            font-weight: 600;
            color: #22c55e;
        }

        .tx-time {
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.6);
        }

        .controls {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        /* Nouvelles sections */
        .fundamental-section, .signals-section, .nft-analytics {
            margin-bottom: 3rem;
        }

        .section-title {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
            background: linear-gradient(45deg, #00d4ff, #7c3aed, #f59e0b);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .fundamental-grid, .signals-grid, .analytics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .news-panel, .metrics-panel, .calls-detector, .whale-tracker, 
        .defi-tracker, .meme-tracker, .nft-trends, .social-sentiment,
        .onchain-metrics, .ai-predictions {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
        }

        .panel-title {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: #00d4ff;
            border-bottom: 2px solid rgba(0, 212, 255, 0.2);
            padding-bottom: 0.5rem;
        }

        .news-list, .calls-list, .whale-list, .defi-list, .meme-list,
        .nft-trends-list, .onchain-list, .predictions-list {
            max-height: 400px;
            overflow-y: auto;
        }

        .news-item, .call-item, .whale-item, .trend-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
        }

        .news-item:hover, .call-item:hover, .whale-item:hover, .trend-item:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(0, 212, 255, 0.3);
            transform: translateX(5px);
        }

        .news-title {
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 0.5rem;
            line-height: 1.3;
        }

        .news-summary {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            line-height: 1.4;
            margin-bottom: 0.5rem;
        }

        .news-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.5);
        }

        .news-source {
            background: linear-gradient(45deg, #f59e0b, #ef4444);
            padding: 0.2rem 0.5rem;
            border-radius: 12px;
            font-weight: 600;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
        }

        .metric-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .metric-card:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateY(-2px);
        }

        .metric-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: #00d4ff;
            margin-bottom: 0.5rem;
        }

        .metric-label {
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.7);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .call-signal {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .call-bullish {
            background: rgba(34, 197, 94, 0.2);
            color: #22c55e;
            border: 1px solid rgba(34, 197, 94, 0.3);
        }

        .call-bearish {
            background: rgba(239, 68, 68, 0.2);
            color: #ef4444;
            border: 1px solid rgba(239, 68, 68, 0.3);
        }

        .call-neutral {
            background: rgba(245, 158, 11, 0.2);
            color: #f59e0b;
            border: 1px solid rgba(245, 158, 11, 0.3);
        }

        .whale-amount {
            font-size: 1.2rem;
            font-weight: 700;
            color: #7c3aed;
            margin-bottom: 0.5rem;
        }

        .trending-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            padding: 0.2rem 0.6rem;
            border-radius: 15px;
            font-size: 0.7rem;
            font-weight: 600;
        }

        .sentiment-chart-container {
            height: 300px;
            padding: 1rem;
        }

        .prediction-confidence {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-top: 0.5rem;
        }

        .confidence-bar {
            flex: 1;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            overflow: hidden;
        }

        .confidence-fill {
            height: 100%;
            background: linear-gradient(90deg, #ef4444, #f59e0b, #22c55e);
            border-radius: 3px;
            transition: width 0.3s ease;
        }

        .alert-badge {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: linear-gradient(45deg, #ef4444, #dc2626);
            color: white;
            padding: 0.3rem 0.6rem;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: 600;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.8; transform: scale(1.05); }
        }

        .risk-indicator {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .risk-low { color: #22c55e; }
        .risk-medium { color: #f59e0b; }
        .risk-high { color: #ef4444; }

        .btn {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.2), rgba(124, 58, 237, 0.2));
            border: 1px solid rgba(0, 212, 255, 0.3);
            color: #ffffff;
            padding: 0.8rem 1.5rem;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .btn:hover {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.4), rgba(124, 58, 237, 0.4));
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0, 212, 255, 0.2);
        }

        .loading {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }

        .spinner {
            width: 40px;
            height: 40px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-top: 3px solid #00d4ff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .status-indicator {
            position: fixed;
            top: 100px;
            right: 20px;
            background: rgba(34, 197, 94, 0.9);
            color: white;
            padding: 1rem;
            border-radius: 12px;
            border-left: 4px solid #22c55e;
            transform: translateX(100%);
            transition: transform 0.3s ease;
        }

        .status-indicator.show {
            transform: translateX(0);
        }

        @media (max-width: 768px) {
            .charts-section {
                grid-template-columns: 1fr;
            }
            
            .container {
                padding: 1rem;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <h1>🚀 Dashboard Crypto Sophistiqué</h1>
    </nav>

    <div class="container">
        <div class="controls">
            <button class="btn" onclick="updatePrices()">🔄 Actualiser Prix</button>
            <button class="btn" onclick="fetchNews()">📰 News Crypto</button>
            <button class="btn" onclick="detectCalls()">🚨 Détecter Calls</button>
            <button class="btn" onclick="trackWhales()">🐋 Whale Tracker</button>
            <button class="btn" onclick="analyzeDeFi()">🌊 DeFi Analysis</button>
            <button class="btn" onclick="scanMemeCoins()">🔥 Meme Scanner</button>
            <button class="btn" onclick="fetchNFTTrends()">🎨 NFT Trends</button>
            <button class="btn" onclick="toggleAutoRefresh()">⚡ Auto-Refresh</button>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-icon bitcoin-icon">₿</div>
                <div class="stat-value" id="btc-price">$0</div>
                <div class="stat-label">Bitcoin (BTC)</div>
                <div class="change-indicator" id="btc-change">
                    <span>📈</span>
                    <span>+0.00%</span>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon ethereum-icon">Ξ</div>
                <div class="stat-value" id="eth-price">$0</div>
                <div class="stat-label">Ethereum (ETH)</div>
                <div class="change-indicator" id="eth-change">
                    <span>📈</span>
                    <span>+0.00%</span>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon solana-icon">◎</div>
                <div class="stat-value" id="sol-price">$0</div>
                <div class="stat-label">Solana (SOL)</div>
                <div class="change-indicator" id="sol-change">
                    <span>📈</span>
                    <span>+0.00%</span>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon nft-icon">🎨</div>
                <div class="stat-value" id="nft-volume">$0</div>
                <div class="stat-label">NFT Volume 24h</div>
                <div class="change-indicator positive">
                    <span>🔥</span>
                    <span>Volume élevé</span>
                </div>
            </div>
        </div>

        <div class="charts-section">
            <div class="chart-container">
                <div class="chart-title">📊 Évolution des Prix (24h)</div>
                <canvas id="priceChart" width="400" height="200"></canvas>
            </div>

            <div class="chart-container">
                <div class="chart-title">🥧 Répartition Portfolio</div>
                <canvas id="portfolioChart" width="300" height="300"></canvas>
            </div>
        </div>

        <!-- Section Analyse Fondamentale -->
        <div class="fundamental-section">
            <div class="section-title">📊 Analyse Fondamentale Crypto</div>
            
            <div class="fundamental-grid">
                <div class="news-panel">
                    <div class="panel-title">📰 News CoinDesk & Crypto.com</div>
                    <div class="news-list" id="news-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="metrics-panel">
                    <div class="panel-title">📈 Métriques Clés</div>
                    <div class="metrics-grid" id="metrics-grid">
                        <div class="metric-card">
                            <div class="metric-value" id="fear-greed">50</div>
                            <div class="metric-label">Fear & Greed Index</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value" id="btc-dominance">45%</div>
                            <div class="metric-label">BTC Dominance</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value" id="total-mcap">$2.1T</div>
                            <div class="metric-label">Total Market Cap</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value" id="defi-tvl">$45B</div>
                            <div class="metric-label">DeFi TVL</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section Détection Calls/Signaux -->
        <div class="signals-section">
            <div class="section-title">🚨 Détection de Signaux & Calls</div>
            
            <div class="signals-grid">
                <div class="calls-detector">
                    <div class="panel-title">📢 Crypto Calls Détectés</div>
                    <div class="calls-list" id="calls-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="whale-tracker">
                    <div class="panel-title">🐋 Whale Tracker</div>
                    <div class="whale-list" id="whale-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="defi-tracker">
                    <div class="panel-title">🌊 DeFi Pulse</div>
                    <div class="defi-list" id="defi-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="meme-tracker">
                    <div class="panel-title">🔥 Meme Coins Trending</div>
                    <div class="meme-list" id="meme-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section NFT & Analytics -->
        <div class="nft-analytics">
            <div class="section-title">🎨 NFT & Analyse Avancée</div>
            
            <div class="analytics-grid">
                <div class="nft-trends">
                    <div class="panel-title">🖼️ NFT Trends</div>
                    <div class="nft-trends-list" id="nft-trends-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="social-sentiment">
                    <div class="panel-title">💬 Social Sentiment</div>
                    <div class="sentiment-chart-container">
                        <canvas id="sentimentChart" width="400" height="200"></canvas>
                    </div>
                </div>
                
                <div class="onchain-metrics">
                    <div class="panel-title">⛓️ On-Chain Metrics</div>
                    <div class="onchain-list" id="onchain-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="ai-predictions">
                    <div class="panel-title">🤖 AI Predictions</div>
                    <div class="predictions-list" id="predictions-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="transactions-table">
            <div class="table-title">
                <span>💎</span>
                <span>Grandes Transactions Récentes</span>
            </div>
            <div class="transactions-list" id="transactions-list">
                <div class="loading">
                    <div class="spinner"></div>
                </div>
            </div>
        </div>
    </div>

    <div class="status-indicator" id="status-indicator">
        ✅ Données mises à jour
    </div>

    <script>
        // Configuration
        const API_CONFIG = {
            coingecko: 'https://api.coingecko.com/api/v3',
            newsapi: 'https://newsapi.org/v2',
            alternative: 'https://api.alternative.me/v1',
            defipulse: 'https://api.defipulse.com/api/v1',
            fallbackPrices: {
                bitcoin: 45000,
                ethereum: 2800,
                solana: 95
            }
        };

        // État global
        let autoRefresh = false;
        let refreshInterval;
        let priceChart, portfolioChart, sentimentChart;
        let priceHistory = {
            bitcoin: [],
            ethereum: [],
            solana: []
        };

        // Base de données de signaux simulés
        const CRYPTO_SIGNALS_DB = {
            calls: [
                { coin: 'BTC', signal: 'BULLISH', confidence: 85, source: 'Technical Analysis', target: '$48000' },
                { coin: 'ETH', signal: 'BULLISH', confidence: 78, source: 'Whale Activity', target: '$3200' },
                { coin: 'SOL', signal: 'NEUTRAL', confidence: 65, source: 'Social Sentiment', target: '$110' },
                { coin: 'ADA', signal: 'BEARISH', confidence: 72, source: 'Volume Analysis', target: '$0.35' },
                { coin: 'MATIC', signal: 'BULLISH', confidence: 90, source: 'Fundamental', target: '$1.20' }
            ],
            whales: [
                { amount: '$12.5M', coin: 'BTC', action: 'ACCUMULATION', exchange: 'Coinbase', confidence: 'HIGH' },
                { amount: '$8.2M', coin: 'ETH', action: 'DISTRIBUTION', exchange: 'Binance', confidence: 'MEDIUM' },
                { amount: '$5.7M', coin: 'SOL', action: 'ACCUMULATION', exchange: 'FTX', confidence: 'HIGH' },
                { amount: '$3.1M', coin: 'AVAX', action: 'ACCUMULATION', exchange: 'Kraken', confidence: 'MEDIUM' }
            ],
            defi: [
                { protocol: 'Uniswap', tvl: '$4.2B', change: '+5.2%', apy: '12.5%' },
                { protocol: 'Aave', tvl: '$7.8B', change: '+2.1%', apy: '8.9%' },
                { protocol: 'Compound', tvl: '$3.1B', change: '-1.5%', apy: '6.2%' },
                { protocol: 'MakerDAO', tvl: '$9.5B', change: '+3.8%', apy: '4.1%' }
            ],
            memes: [
                { name: 'PEPE', price: '$0.00001234', change: '+156.7%', volume: '$45M', trend: 'VIRAL' },
                { name: 'DOGE', price: '$0.0789', change: '+12.3%', volume: '$234M', trend: 'STABLE' },
                { name: 'SHIB', price: '$0.000008', change: '+45.6%', volume: '$123M', trend: 'RISING' },
                { name: 'FLOKI', price: '$0.000023', change: '+89.2%', volume: '$67M', trend: 'EXPLOSIVE' }
            ],
            news: [
                { title: 'Bitcoin ETF Approval Drives Institutional Adoption', summary: 'Major financial institutions increase crypto exposure following regulatory clarity...', source: 'CoinDesk', time: '2h ago' },
                { title: 'Ethereum Layer 2 Solutions See Record Usage', summary: 'Polygon and Arbitrum report unprecedented transaction volumes as gas fees drop...', source: 'Crypto.com', time: '4h ago' },
                { title: 'Solana DeFi Ecosystem Expands with New Protocols', summary: 'Several new DeFi projects launch on Solana, bringing innovative yield farming opportunities...', source: 'CoinTelegraph', time: '6h ago' },
                { title: 'NFT Market Shows Signs of Recovery', summary: 'Blue chip NFT collections see increased trading volume and floor price stability...', source: 'The Block', time: '8h ago' }
            ],
            nftTrends: [
                { collection: 'CryptoPunks', floor: '45.2 ETH', volume: '234 ETH', change: '+12.5%' },
                { collection: 'Bored Apes', floor: '32.1 ETH', volume: '456 ETH', change: '+8.7%' },
                { collection: 'Azuki', floor: '18.5 ETH', volume: '123 ETH', change: '+23.1%' },
                { collection: 'Pudgy Penguins', floor: '8.9 ETH', volume: '89 ETH', change: '+15.6%' }
            ]
        };

        // Initialisation
        document.addEventListener('DOMContentLoaded', function() {
            initCharts();
            updatePrices();
            fetchNews();
            updateFundamentalMetrics();
            detectCalls();
            trackWhales();
            analyzeDeFi();
            scanMemeCoins();
            fetchNFTTrends();
            updateOnChainMetrics();
            generateAIPredictions();
            showStatus('🚀 Dashboard crypto sophistiqué initialisé');
        });

        // Initialisation des graphiques
        function initCharts() {
            // Graphique des prix
            const ctx1 = document.getElementById('priceChart').getContext('2d');
            priceChart = new Chart(ctx1, {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [
                        {
                            label: 'Bitcoin',
                            data: [],
                            borderColor: '#f7931a',
                            backgroundColor: 'rgba(247, 147, 26, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'Ethereum',
                            data: [],
                            borderColor: '#627eea',
                            backgroundColor: 'rgba(98, 126, 234, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'Solana',
                            data: [],
                            borderColor: '#00d18c',
                            backgroundColor: 'rgba(0, 209, 140, 0.1)',
                            tension: 0.4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: '#ffffff' }
                        }
                    },
                    scales: {
                        x: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        },
                        y: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        }
                    }
                }
            });

            // Graphique portfolio
            const ctx2 = document.getElementById('portfolioChart').getContext('2d');
            portfolioChart = new Chart(ctx2, {
                type: 'doughnut',
                data: {
                    labels: ['Bitcoin', 'Ethereum', 'Solana', 'Autres'],
                    datasets: [{
                        data: [40, 30, 20, 10],
                        backgroundColor: [
                            '#f7931a',
                            '#627eea',
                            '#00d18c',
                            '#7c3aed'
                        ],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: '#ffffff' }
                        }
                    }
                }
            });

            // Graphique sentiment
            const ctx3 = document.getElementById('sentimentChart').getContext('2d');
            sentimentChart = new Chart(ctx3, {
                type: 'bar',
                data: {
                    labels: ['Twitter', 'Reddit', 'Telegram', 'Discord', 'News'],
                    datasets: [{
                        label: 'Sentiment Score',
                        data: [75, 60, 85, 70, 80],
                        backgroundColor: [
                            'rgba(29, 161, 242, 0.8)',
                            'rgba(255, 69, 0, 0.8)',
                            'rgba(0, 136, 204, 0.8)',
                            'rgba(114, 137, 218, 0.8)',
                            'rgba(0, 212, 255, 0.8)'
                        ],
                        borderWidth: 2,
                        borderColor: '#ffffff'
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: '#ffffff' }
                        }
                    },
                    scales: {
                        x: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        },
                        y: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' },
                            max: 100
                        }
                    }
                }
            });
        }

        // Mise à jour des prix
        async function updatePrices() {
            try {
                showStatus('🔄 Mise à jour des prix...');
                
                const response = await fetch(`${API_CONFIG.coingecko}/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true`);
                
                if (!response.ok) {
                    throw new Error('API non disponible');
                }
                
                const data = await response.json();
                
                // Mise à jour des prix
                updatePriceDisplay('btc', data.bitcoin);
                updatePriceDisplay('eth', data.ethereum);
                updatePriceDisplay('sol', data.solana);
                
                // Mise à jour de l'historique
                const now = new Date().toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
                updatePriceHistory(now, data);
                
                // Volume NFT simulé
                document.getElementById('nft-volume').textContent = '$' + (Math.random() * 10000000).toLocaleString('fr-FR', { maximumFractionDigits: 0 });
                
                showStatus('✅ Prix mis à jour');
                
            } catch (error) {
                console.error('Erreur prix:', error);
                // Utiliser les prix de fallback
                updatePriceDisplay('btc', { usd: API_CONFIG.fallbackPrices.bitcoin, usd_24h_change: Math.random() * 10 - 5 });
                updatePriceDisplay('eth', { usd: API_CONFIG.fallbackPrices.ethereum, usd_24h_change: Math.random() * 10 - 5 });
                updatePriceDisplay('sol', { usd: API_CONFIG.fallbackPrices.solana, usd_24h_change: Math.random() * 10 - 5 });
                
                showStatus('⚠️ Mode hors ligne');
            }
        }

        function updatePriceDisplay(coin, data) {
            const price = data.usd || 0;
            const change = data.usd_24h_change || 0;
            
            document.getElementById(`${coin}-price`).textContent = '$' + price.toLocaleString('fr-FR');
            
            const changeElement = document.getElementById(`${coin}-change`);
            const isPositive = change >= 0;
            changeElement.className = `change-indicator ${isPositive ? 'positive' : 'negative'}`;
            changeElement.innerHTML = `
                <span>${isPositive ? '📈' : '📉'}</span>
                <span>${isPositive ? '+' : ''}${change.toFixed(2)}%</span>
            `;
        }

        function updatePriceHistory(time, data) {
            const maxPoints = 20;
            
            // Ajouter les nouveaux points
            priceHistory.bitcoin.push(data.bitcoin.usd);
            priceHistory.ethereum.push(data.ethereum.usd);
            priceHistory.solana.push(data.solana.usd);
            
            // Limiter le nombre de points
            if (priceHistory.bitcoin.length > maxPoints) {
                priceHistory.bitcoin.shift();
                priceHistory.ethereum.shift();
                priceHistory.solana.shift();
            }
            
            // Mettre à jour le graphique
            if (priceChart.data.labels.length >= maxPoints) {
                priceChart.data.labels.shift();
            }
            priceChart.data.labels.push(time);
            
            priceChart.data.datasets[0].data = [...priceHistory.bitcoin];
            priceChart.data.datasets[1].data = [...priceHistory.ethereum];
            priceChart.data.datasets[2].data = [...priceHistory.solana];
            
            priceChart.update('none');
        }

        // Simulation de transactions
        function fetchTransactions() {
            showStatus('💸 Récupération des transactions...');
            
            const transactions = generateMockTransactions(5);
            const transactionsList = document.getElementById('transactions-list');
            
            transactionsList.innerHTML = transactions.map(tx => `
                <div class="transaction-item">
                    <div class="tx-hash">${tx.hash}</div>
                    <div class="tx-amount">$${tx.amount.toLocaleString('fr-FR')}</div>
                    <div class="tx-time">${tx.time} • ${tx.chain}</div>
                </div>
            `).join('');
            
            showStatus('✅ Transactions chargées');
        }

        function generateMockTransactions(count) {
            const chains = ['Bitcoin', 'Ethereum', 'Solana', 'BNB'];
            const transactions = [];
            
            for (let i = 0; i < count; i++) {
                transactions.push({
                    hash: '0x' + Math.random().toString(16).substr(2, 8) + '...' + Math.random().toString(16).substr(2, 4),
                    amount: Math.random() * 1000000 + 100000,
                    time: new Date(Date.now() - Math.random() * 3600000).toLocaleTimeString('fr-FR'),
                    chain: chains[Math.floor(Math.random() * chains.length)]
                });
            }
            
            return transactions.sort((a, b) => b.amount - a.amount);
        }

        // Simulation NFTs
        function fetchNFTs() {
            showStatus('🎨 Récupération des NFTs...');
            
            setTimeout(() => {
                const mockNFTs = [
                    'CryptoPunks #1234',
                    'Bored Ape #5678',
                    'Azuki #9012',
                    'Pudgy Penguins #3456',
                    'Doodles #7890'
                ];
                
                const nftList = mockNFTs.map(nft => `
                    <div class="transaction-item">
                        <div style="color: #ff6b6b; font-weight: 600;">${nft}</div>
                        <div class="tx-amount">$${(Math.random() * 100000 + 10000).toLocaleString('fr-FR')}</div>
                        <div class="tx-time">Vendu il y a ${Math.floor(Math.random() * 120)} minutes</div>
                    </div>
                `).join('');
                
                document.getElementById('transactions-list').innerHTML = `
                    <div style="margin-bottom: 1rem; color: #ff6b6b; font-weight: 600;">🎨 Top NFT Sales</div>
                    ${nftList}
                `;
                
                showStatus('✅ NFTs chargés');
            }, 1000);
        }

        // Auto-refresh amélioré
        function toggleAutoRefresh() {
            autoRefresh = !autoRefresh;
            
            if (autoRefresh) {
                refreshInterval = setInterval(() => {
                    updatePrices();
                    updateFundamentalMetrics();
                    detectCalls();
                    trackWhales();
                    analyzeDeFi();
                    scanMemeCoins();
                    updateOnChainMetrics();
                    
                    // Mise à jour du sentiment
                    const newSentimentData = [
                        Math.floor(Math.random() * 40) + 60,
                        Math.floor(Math.random() * 40) + 50,
                        Math.floor(Math.random() * 30) + 70,
                        Math.floor(Math.random() * 35) + 55,
                        Math.floor(Math.random() * 25) + 75
                    ];
                    sentimentChart.data.datasets[0].data = newSentimentData;
                    sentimentChart.update('none');
                    
                }, 30000); // Toutes les 30 secondes
                showStatus('⚡ Auto-refresh activé - Mode Pro (30s)');
            } else {
                clearInterval(refreshInterval);
                showStatus('⏸️ Auto-refresh désactivé');
            }
        }

        // Amélioration de l'affichage des transactions
        function fetchTransactions() {
            showStatus('💸 Analyse des grandes transactions...');
            
            const transactions = [
                { 
                    hash: '0x7d2a...f8c4', 
                    amount: 2500000, 
                    time: '3 min ago', 
                    chain: 'Ethereum',
                    type: 'DEX Swap',
                    from: 'Whale Wallet',
                    to: 'Uniswap V3'
                },
                { 
                    hash: 'bc1q...7x9p', 
                    amount: 5200000, 
                    time: '8 min ago', 
                    chain: 'Bitcoin',
                    type: 'Exchange Transfer',
                    from: 'Coinbase',
                    to: 'Cold Storage'
                },
                { 
                    hash: '9WzD...K2mQ', 
                    amount: 890000, 
                    time: '12 min ago', 
                    chain: 'Solana',
                    type: 'DeFi Staking',
                    from: 'Phantom Wallet',
                    to: 'Marinade Finance'
                },
                { 
                    hash: '0xa1b2...c3d4', 
                    amount: 1750000, 
                    time: '18 min ago', 
                    chain: 'Ethereum',
                    type: 'NFT Purchase',
                    from: 'OpenSea',
                    to: 'Collector'
                }
            ];
            
            const transactionsList = document.getElementById('transactions-list');
            transactionsList.innerHTML = transactions.map(tx => `
                <div class="transaction-item">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <div class="tx-hash">${tx.hash}</div>
                        <span class="trending-badge">${tx.type}</span>
                    </div>
                    <div class="tx-amount">${tx.amount.toLocaleString('fr-FR')}</div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 0.5rem 0; font-size: 0.8rem; color: rgba(255,255,255,0.7);">
                        <div>From: <strong>${tx.from}</strong></div>
                        <div>To: <strong>${tx.to}</strong></div>
                    </div>
                    <div class="tx-time">${tx.time} • ${tx.chain}</div>
                </div>
            `).join('');
            
            showStatus('✅ Transactions analysées');
        }

        // Fonction d'analyse de risque
        function analyzeRisk(amount, volatility, sentiment) {
            const riskScore = (amount / 1000000) * volatility * (100 - sentiment);
            if (riskScore > 50) return { level: 'HIGH', color: '#ef4444', icon: '🔴' };
            if (riskScore > 25) return { level: 'MEDIUM', color: '#f59e0b', icon: '🟡' };
            return { level: 'LOW', color: '#22c55e', icon: '🟢' };
        }

        // Fonction d'alerte intelligente
        function triggerSmartAlert(type, data) {
            const alertDiv = document.createElement('div');
            alertDiv.className = 'alert-badge';
            alertDiv.innerHTML = `🚨 ${type}: ${data}`;
            
            // Ajouter l'alerte temporairement
            document.body.appendChild(alertDiv);
            
            setTimeout(() => {
                if (document.body.contains(alertDiv)) {
                    document.body.removeChild(alertDiv);
                }
            }, 5000);
        }

        // Détection d'anomalies de marché
        function detectMarketAnomalies() {
            // Simulation de détection d'anomalies
            const anomalies = [
                { type: 'VOLUME_SPIKE', coin: 'BTC', increase: '450%' },
                { type: 'WHALE_MOVEMENT', coin: 'ETH', amount: '$15M' },
                { type: 'SOCIAL_BUZZ', coin: 'SOL', mentions: '+1200%' }
            ];
            
            anomalies.forEach(anomaly => {
                if (Math.random() > 0.7) { // 30% de chance de déclencher
                    triggerSmartAlert(anomaly.type, `${anomaly.coin} - ${anomaly.increase || anomaly.amount || anomaly.mentions}`);
                }
            });
        }

        // Calculateur de corrélations
        function calculateCorrelations() {
            return {
                'BTC-ETH': 0.85,
                'BTC-SOL': 0.72,
                'ETH-SOL': 0.78,
                'BTC-NASDAQ': 0.45,
                'BTC-GOLD': -0.12
            };
        }

        // Export des données (simulation)
        function exportData() {
            const data = {
                timestamp: new Date().toISOString(),
                prices: {
                    bitcoin: document.getElementById('btc-price').textContent,
                    ethereum: document.getElementById('eth-price').textContent,
                    solana: document.getElementById('sol-price').textContent
                },
                metrics: {
                    fearGreed: document.getElementById('fear-greed').textContent,
                    btcDominance: document.getElementById('btc-dominance').textContent,
                    totalMcap: document.getElementById('total-mcap').textContent
                },
                signals: CRYPTO_SIGNALS_DB.calls
            };
            
            // Créer un fichier de téléchargement
            const dataStr = JSON.stringify(data, null, 2);
            const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
            
            const exportFileDefaultName = `crypto_data_${new Date().toISOString().split('T')[0]}.json`;
            
            const linkElement = document.createElement('a');
            linkElement.setAttribute('href', dataUri);
            linkElement.setAttribute('download', exportFileDefaultName);
            linkElement.click();
            
            showStatus('💾 Données exportées');
        }

        // Ajout d'un bouton d'export dans les contrôles
        document.addEventListener('DOMContentLoaded', function() {
            const controls = document.querySelector('.controls');
            const exportBtn = document.createElement('button');
            exportBtn.className = 'btn';
            exportBtn.innerHTML = '💾 Export Data';
            exportBtn.onclick = exportData;
            controls.appendChild(exportBtn);
            
            // Démarrer la détection d'anomalies
            setInterval(detectMarketAnomalies, 60000); // Chaque minute
        });

        // Amélioration de la fonction showStatus avec différents types
        function showStatus(message, type = 'info') {
            const statusIndicator = document.getElementById('status-indicator');
            statusIndicator.textContent = message;
            
            // Changer la couleur selon le type
            switch(type) {
                case 'success':
                    statusIndicator.style.background = 'rgba(34, 197, 94, 0.9)';
                    statusIndicator.style.borderLeftColor = '#22c55e';
                    break;
                case 'warning':
                    statusIndicator.style.background = 'rgba(245, 158, 11, 0.9)';
                    statusIndicator.style.borderLeftColor = '#f59e0b';
                    break;
                case 'error':
                    statusIndicator.style.background = 'rgba(239, 68, 68, 0.9)';
                    statusIndicator.style.borderLeftColor = '#ef4444';
                    break;
                default:
                    statusIndicator.style.background = 'rgba(0, 212, 255, 0.9)';
                    statusIndicator.style.borderLeftColor = '#00d4ff';
            }
            
            statusIndicator.classList.add('show');
            
            setTimeout(() => {
                statusIndicator.classList.remove('show');
            }, 3000);
        }

        // Affichage du status
        function showStatus(message) {
            const statusIndicator = document.getElementById('status-indicator');
            statusIndicator.textContent = message;
            statusIndicator.classList.add('show');
            
            setTimeout(() => {
                statusIndicator.classList.remove('show');
            }, 3000);
        }

        // Nettoyage au déchargement de la page
        window.addEventListener('beforeunload', function() {
            if (refreshInterval) {
                clearInterval(refreshInterval);
            }
        });
    </script>
</body>
</html> + totalMcap + 'T';
            document.getElementById('defi-tvl').textContent = '<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Crypto Sophistiqué</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/date-fns/2.29.3/index.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
            min-height: 100vh;
            overflow-x: hidden;
        }

        .navbar {
            background: rgba(15, 15, 35, 0.9);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .navbar h1 {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(45deg, #00d4ff, #7c3aed, #f59e0b);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { filter: brightness(1); }
            to { filter: brightness(1.2) drop-shadow(0 0 10px rgba(0, 212, 255, 0.3)); }
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .stat-card {
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02));
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            border-color: rgba(0, 212, 255, 0.5);
            box-shadow: 0 20px 40px rgba(0, 212, 255, 0.1);
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #00d4ff, #7c3aed, #f59e0b);
        }

        .stat-header {
            display: flex;
            justify-content: between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .stat-icon {
            width: 50px;
            height: 50px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .bitcoin-icon { background: linear-gradient(145deg, #f7931a, #ff6b35); }
        .ethereum-icon { background: linear-gradient(145deg, #627eea, #3c4ccd); }
        .solana-icon { background: linear-gradient(145deg, #00d18c, #7c3aed); }
        .nft-icon { background: linear-gradient(145deg, #ff6b6b, #ee5a24); }

        .stat-value {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .change-indicator {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-top: 1rem;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
        }

        .positive { background: rgba(34, 197, 94, 0.2); color: #22c55e; }
        .negative { background: rgba(239, 68, 68, 0.2); color: #ef4444; }

        .charts-section {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .chart-container {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
        }

        .chart-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 2rem;
            text-align: center;
        }

        .transactions-table {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
        }

        .table-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .transactions-list {
            max-height: 400px;
            overflow-y: auto;
        }

        .transaction-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
        }

        .transaction-item:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(0, 212, 255, 0.3);
        }

        .tx-hash {
            font-family: 'Monaco', monospace;
            color: #00d4ff;
            font-size: 0.8rem;
            margin-bottom: 0.5rem;
        }

        .tx-amount {
            font-size: 1.2rem;
            font-weight: 600;
            color: #22c55e;
        }

        .tx-time {
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.6);
        }

        .controls {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        /* Nouvelles sections */
        .fundamental-section, .signals-section, .nft-analytics {
            margin-bottom: 3rem;
        }

        .section-title {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
            background: linear-gradient(45deg, #00d4ff, #7c3aed, #f59e0b);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .fundamental-grid, .signals-grid, .analytics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .news-panel, .metrics-panel, .calls-detector, .whale-tracker, 
        .defi-tracker, .meme-tracker, .nft-trends, .social-sentiment,
        .onchain-metrics, .ai-predictions {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
        }

        .panel-title {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: #00d4ff;
            border-bottom: 2px solid rgba(0, 212, 255, 0.2);
            padding-bottom: 0.5rem;
        }

        .news-list, .calls-list, .whale-list, .defi-list, .meme-list,
        .nft-trends-list, .onchain-list, .predictions-list {
            max-height: 400px;
            overflow-y: auto;
        }

        .news-item, .call-item, .whale-item, .trend-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
        }

        .news-item:hover, .call-item:hover, .whale-item:hover, .trend-item:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(0, 212, 255, 0.3);
            transform: translateX(5px);
        }

        .news-title {
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 0.5rem;
            line-height: 1.3;
        }

        .news-summary {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            line-height: 1.4;
            margin-bottom: 0.5rem;
        }

        .news-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.5);
        }

        .news-source {
            background: linear-gradient(45deg, #f59e0b, #ef4444);
            padding: 0.2rem 0.5rem;
            border-radius: 12px;
            font-weight: 600;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
        }

        .metric-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .metric-card:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateY(-2px);
        }

        .metric-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: #00d4ff;
            margin-bottom: 0.5rem;
        }

        .metric-label {
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.7);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .call-signal {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .call-bullish {
            background: rgba(34, 197, 94, 0.2);
            color: #22c55e;
            border: 1px solid rgba(34, 197, 94, 0.3);
        }

        .call-bearish {
            background: rgba(239, 68, 68, 0.2);
            color: #ef4444;
            border: 1px solid rgba(239, 68, 68, 0.3);
        }

        .call-neutral {
            background: rgba(245, 158, 11, 0.2);
            color: #f59e0b;
            border: 1px solid rgba(245, 158, 11, 0.3);
        }

        .whale-amount {
            font-size: 1.2rem;
            font-weight: 700;
            color: #7c3aed;
            margin-bottom: 0.5rem;
        }

        .trending-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            padding: 0.2rem 0.6rem;
            border-radius: 15px;
            font-size: 0.7rem;
            font-weight: 600;
        }

        .sentiment-chart-container {
            height: 300px;
            padding: 1rem;
        }

        .prediction-confidence {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-top: 0.5rem;
        }

        .confidence-bar {
            flex: 1;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            overflow: hidden;
        }

        .confidence-fill {
            height: 100%;
            background: linear-gradient(90deg, #ef4444, #f59e0b, #22c55e);
            border-radius: 3px;
            transition: width 0.3s ease;
        }

        .alert-badge {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: linear-gradient(45deg, #ef4444, #dc2626);
            color: white;
            padding: 0.3rem 0.6rem;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: 600;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.8; transform: scale(1.05); }
        }

        .risk-indicator {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .risk-low { color: #22c55e; }
        .risk-medium { color: #f59e0b; }
        .risk-high { color: #ef4444; }

        .btn {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.2), rgba(124, 58, 237, 0.2));
            border: 1px solid rgba(0, 212, 255, 0.3);
            color: #ffffff;
            padding: 0.8rem 1.5rem;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .btn:hover {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.4), rgba(124, 58, 237, 0.4));
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0, 212, 255, 0.2);
        }

        .loading {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }

        .spinner {
            width: 40px;
            height: 40px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-top: 3px solid #00d4ff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .status-indicator {
            position: fixed;
            top: 100px;
            right: 20px;
            background: rgba(34, 197, 94, 0.9);
            color: white;
            padding: 1rem;
            border-radius: 12px;
            border-left: 4px solid #22c55e;
            transform: translateX(100%);
            transition: transform 0.3s ease;
        }

        .status-indicator.show {
            transform: translateX(0);
        }

        @media (max-width: 768px) {
            .charts-section {
                grid-template-columns: 1fr;
            }
            
            .container {
                padding: 1rem;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <h1>🚀 Dashboard Crypto Sophistiqué</h1>
    </nav>

    <div class="container">
        <div class="controls">
            <button class="btn" onclick="updatePrices()">🔄 Actualiser Prix</button>
            <button class="btn" onclick="fetchNews()">📰 News Crypto</button>
            <button class="btn" onclick="detectCalls()">🚨 Détecter Calls</button>
            <button class="btn" onclick="trackWhales()">🐋 Whale Tracker</button>
            <button class="btn" onclick="analyzeDeFi()">🌊 DeFi Analysis</button>
            <button class="btn" onclick="scanMemeCoins()">🔥 Meme Scanner</button>
            <button class="btn" onclick="fetchNFTTrends()">🎨 NFT Trends</button>
            <button class="btn" onclick="toggleAutoRefresh()">⚡ Auto-Refresh</button>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-icon bitcoin-icon">₿</div>
                <div class="stat-value" id="btc-price">$0</div>
                <div class="stat-label">Bitcoin (BTC)</div>
                <div class="change-indicator" id="btc-change">
                    <span>📈</span>
                    <span>+0.00%</span>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon ethereum-icon">Ξ</div>
                <div class="stat-value" id="eth-price">$0</div>
                <div class="stat-label">Ethereum (ETH)</div>
                <div class="change-indicator" id="eth-change">
                    <span>📈</span>
                    <span>+0.00%</span>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon solana-icon">◎</div>
                <div class="stat-value" id="sol-price">$0</div>
                <div class="stat-label">Solana (SOL)</div>
                <div class="change-indicator" id="sol-change">
                    <span>📈</span>
                    <span>+0.00%</span>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon nft-icon">🎨</div>
                <div class="stat-value" id="nft-volume">$0</div>
                <div class="stat-label">NFT Volume 24h</div>
                <div class="change-indicator positive">
                    <span>🔥</span>
                    <span>Volume élevé</span>
                </div>
            </div>
        </div>

        <div class="charts-section">
            <div class="chart-container">
                <div class="chart-title">📊 Évolution des Prix (24h)</div>
                <canvas id="priceChart" width="400" height="200"></canvas>
            </div>

            <div class="chart-container">
                <div class="chart-title">🥧 Répartition Portfolio</div>
                <canvas id="portfolioChart" width="300" height="300"></canvas>
            </div>
        </div>

        <!-- Section Analyse Fondamentale -->
        <div class="fundamental-section">
            <div class="section-title">📊 Analyse Fondamentale Crypto</div>
            
            <div class="fundamental-grid">
                <div class="news-panel">
                    <div class="panel-title">📰 News CoinDesk & Crypto.com</div>
                    <div class="news-list" id="news-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="metrics-panel">
                    <div class="panel-title">📈 Métriques Clés</div>
                    <div class="metrics-grid" id="metrics-grid">
                        <div class="metric-card">
                            <div class="metric-value" id="fear-greed">50</div>
                            <div class="metric-label">Fear & Greed Index</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value" id="btc-dominance">45%</div>
                            <div class="metric-label">BTC Dominance</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value" id="total-mcap">$2.1T</div>
                            <div class="metric-label">Total Market Cap</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value" id="defi-tvl">$45B</div>
                            <div class="metric-label">DeFi TVL</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section Détection Calls/Signaux -->
        <div class="signals-section">
            <div class="section-title">🚨 Détection de Signaux & Calls</div>
            
            <div class="signals-grid">
                <div class="calls-detector">
                    <div class="panel-title">📢 Crypto Calls Détectés</div>
                    <div class="calls-list" id="calls-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="whale-tracker">
                    <div class="panel-title">🐋 Whale Tracker</div>
                    <div class="whale-list" id="whale-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="defi-tracker">
                    <div class="panel-title">🌊 DeFi Pulse</div>
                    <div class="defi-list" id="defi-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="meme-tracker">
                    <div class="panel-title">🔥 Meme Coins Trending</div>
                    <div class="meme-list" id="meme-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section NFT & Analytics -->
        <div class="nft-analytics">
            <div class="section-title">🎨 NFT & Analyse Avancée</div>
            
            <div class="analytics-grid">
                <div class="nft-trends">
                    <div class="panel-title">🖼️ NFT Trends</div>
                    <div class="nft-trends-list" id="nft-trends-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="social-sentiment">
                    <div class="panel-title">💬 Social Sentiment</div>
                    <div class="sentiment-chart-container">
                        <canvas id="sentimentChart" width="400" height="200"></canvas>
                    </div>
                </div>
                
                <div class="onchain-metrics">
                    <div class="panel-title">⛓️ On-Chain Metrics</div>
                    <div class="onchain-list" id="onchain-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="ai-predictions">
                    <div class="panel-title">🤖 AI Predictions</div>
                    <div class="predictions-list" id="predictions-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="transactions-table">
            <div class="table-title">
                <span>💎</span>
                <span>Grandes Transactions Récentes</span>
            </div>
            <div class="transactions-list" id="transactions-list">
                <div class="loading">
                    <div class="spinner"></div>
                </div>
            </div>
        </div>
    </div>

    <div class="status-indicator" id="status-indicator">
        ✅ Données mises à jour
    </div>

    <script>
        // Configuration
        const API_CONFIG = {
            coingecko: 'https://api.coingecko.com/api/v3',
            newsapi: 'https://newsapi.org/v2',
            alternative: 'https://api.alternative.me/v1',
            defipulse: 'https://api.defipulse.com/api/v1',
            fallbackPrices: {
                bitcoin: 45000,
                ethereum: 2800,
                solana: 95
            }
        };

        // État global
        let autoRefresh = false;
        let refreshInterval;
        let priceChart, portfolioChart, sentimentChart;
        let priceHistory = {
            bitcoin: [],
            ethereum: [],
            solana: []
        };

        // Base de données de signaux simulés
        const CRYPTO_SIGNALS_DB = {
            calls: [
                { coin: 'BTC', signal: 'BULLISH', confidence: 85, source: 'Technical Analysis', target: '$48000' },
                { coin: 'ETH', signal: 'BULLISH', confidence: 78, source: 'Whale Activity', target: '$3200' },
                { coin: 'SOL', signal: 'NEUTRAL', confidence: 65, source: 'Social Sentiment', target: '$110' },
                { coin: 'ADA', signal: 'BEARISH', confidence: 72, source: 'Volume Analysis', target: '$0.35' },
                { coin: 'MATIC', signal: 'BULLISH', confidence: 90, source: 'Fundamental', target: '$1.20' }
            ],
            whales: [
                { amount: '$12.5M', coin: 'BTC', action: 'ACCUMULATION', exchange: 'Coinbase', confidence: 'HIGH' },
                { amount: '$8.2M', coin: 'ETH', action: 'DISTRIBUTION', exchange: 'Binance', confidence: 'MEDIUM' },
                { amount: '$5.7M', coin: 'SOL', action: 'ACCUMULATION', exchange: 'FTX', confidence: 'HIGH' },
                { amount: '$3.1M', coin: 'AVAX', action: 'ACCUMULATION', exchange: 'Kraken', confidence: 'MEDIUM' }
            ],
            defi: [
                { protocol: 'Uniswap', tvl: '$4.2B', change: '+5.2%', apy: '12.5%' },
                { protocol: 'Aave', tvl: '$7.8B', change: '+2.1%', apy: '8.9%' },
                { protocol: 'Compound', tvl: '$3.1B', change: '-1.5%', apy: '6.2%' },
                { protocol: 'MakerDAO', tvl: '$9.5B', change: '+3.8%', apy: '4.1%' }
            ],
            memes: [
                { name: 'PEPE', price: '$0.00001234', change: '+156.7%', volume: '$45M', trend: 'VIRAL' },
                { name: 'DOGE', price: '$0.0789', change: '+12.3%', volume: '$234M', trend: 'STABLE' },
                { name: 'SHIB', price: '$0.000008', change: '+45.6%', volume: '$123M', trend: 'RISING' },
                { name: 'FLOKI', price: '$0.000023', change: '+89.2%', volume: '$67M', trend: 'EXPLOSIVE' }
            ],
            news: [
                { title: 'Bitcoin ETF Approval Drives Institutional Adoption', summary: 'Major financial institutions increase crypto exposure following regulatory clarity...', source: 'CoinDesk', time: '2h ago' },
                { title: 'Ethereum Layer 2 Solutions See Record Usage', summary: 'Polygon and Arbitrum report unprecedented transaction volumes as gas fees drop...', source: 'Crypto.com', time: '4h ago' },
                { title: 'Solana DeFi Ecosystem Expands with New Protocols', summary: 'Several new DeFi projects launch on Solana, bringing innovative yield farming opportunities...', source: 'CoinTelegraph', time: '6h ago' },
                { title: 'NFT Market Shows Signs of Recovery', summary: 'Blue chip NFT collections see increased trading volume and floor price stability...', source: 'The Block', time: '8h ago' }
            ],
            nftTrends: [
                { collection: 'CryptoPunks', floor: '45.2 ETH', volume: '234 ETH', change: '+12.5%' },
                { collection: 'Bored Apes', floor: '32.1 ETH', volume: '456 ETH', change: '+8.7%' },
                { collection: 'Azuki', floor: '18.5 ETH', volume: '123 ETH', change: '+23.1%' },
                { collection: 'Pudgy Penguins', floor: '8.9 ETH', volume: '89 ETH', change: '+15.6%' }
            ]
        };

        // Initialisation
        document.addEventListener('DOMContentLoaded', function() {
            initCharts();
            updatePrices();
            fetchNews();
            updateFundamentalMetrics();
            detectCalls();
            trackWhales();
            analyzeDeFi();
            scanMemeCoins();
            fetchNFTTrends();
            updateOnChainMetrics();
            generateAIPredictions();
            showStatus('🚀 Dashboard crypto sophistiqué initialisé');
        });

        // Initialisation des graphiques
        function initCharts() {
            // Graphique des prix
            const ctx1 = document.getElementById('priceChart').getContext('2d');
            priceChart = new Chart(ctx1, {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [
                        {
                            label: 'Bitcoin',
                            data: [],
                            borderColor: '#f7931a',
                            backgroundColor: 'rgba(247, 147, 26, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'Ethereum',
                            data: [],
                            borderColor: '#627eea',
                            backgroundColor: 'rgba(98, 126, 234, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'Solana',
                            data: [],
                            borderColor: '#00d18c',
                            backgroundColor: 'rgba(0, 209, 140, 0.1)',
                            tension: 0.4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: '#ffffff' }
                        }
                    },
                    scales: {
                        x: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        },
                        y: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        }
                    }
                }
            });

            // Graphique portfolio
            const ctx2 = document.getElementById('portfolioChart').getContext('2d');
            portfolioChart = new Chart(ctx2, {
                type: 'doughnut',
                data: {
                    labels: ['Bitcoin', 'Ethereum', 'Solana', 'Autres'],
                    datasets: [{
                        data: [40, 30, 20, 10],
                        backgroundColor: [
                            '#f7931a',
                            '#627eea',
                            '#00d18c',
                            '#7c3aed'
                        ],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: '#ffffff' }
                        }
                    }
                }
            });

            // Graphique sentiment
            const ctx3 = document.getElementById('sentimentChart').getContext('2d');
            sentimentChart = new Chart(ctx3, {
                type: 'bar',
                data: {
                    labels: ['Twitter', 'Reddit', 'Telegram', 'Discord', 'News'],
                    datasets: [{
                        label: 'Sentiment Score',
                        data: [75, 60, 85, 70, 80],
                        backgroundColor: [
                            'rgba(29, 161, 242, 0.8)',
                            'rgba(255, 69, 0, 0.8)',
                            'rgba(0, 136, 204, 0.8)',
                            'rgba(114, 137, 218, 0.8)',
                            'rgba(0, 212, 255, 0.8)'
                        ],
                        borderWidth: 2,
                        borderColor: '#ffffff'
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: '#ffffff' }
                        }
                    },
                    scales: {
                        x: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        },
                        y: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' },
                            max: 100
                        }
                    }
                }
            });
        }

        // Mise à jour des prix
        async function updatePrices() {
            try {
                showStatus('🔄 Mise à jour des prix...');
                
                const response = await fetch(`${API_CONFIG.coingecko}/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true`);
                
                if (!response.ok) {
                    throw new Error('API non disponible');
                }
                
                const data = await response.json();
                
                // Mise à jour des prix
                updatePriceDisplay('btc', data.bitcoin);
                updatePriceDisplay('eth', data.ethereum);
                updatePriceDisplay('sol', data.solana);
                
                // Mise à jour de l'historique
                const now = new Date().toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
                updatePriceHistory(now, data);
                
                // Volume NFT simulé
                document.getElementById('nft-volume').textContent = '$' + (Math.random() * 10000000).toLocaleString('fr-FR', { maximumFractionDigits: 0 });
                
                showStatus('✅ Prix mis à jour');
                
            } catch (error) {
                console.error('Erreur prix:', error);
                // Utiliser les prix de fallback
                updatePriceDisplay('btc', { usd: API_CONFIG.fallbackPrices.bitcoin, usd_24h_change: Math.random() * 10 - 5 });
                updatePriceDisplay('eth', { usd: API_CONFIG.fallbackPrices.ethereum, usd_24h_change: Math.random() * 10 - 5 });
                updatePriceDisplay('sol', { usd: API_CONFIG.fallbackPrices.solana, usd_24h_change: Math.random() * 10 - 5 });
                
                showStatus('⚠️ Mode hors ligne');
            }
        }

        function updatePriceDisplay(coin, data) {
            const price = data.usd || 0;
            const change = data.usd_24h_change || 0;
            
            document.getElementById(`${coin}-price`).textContent = '$' + price.toLocaleString('fr-FR');
            
            const changeElement = document.getElementById(`${coin}-change`);
            const isPositive = change >= 0;
            changeElement.className = `change-indicator ${isPositive ? 'positive' : 'negative'}`;
            changeElement.innerHTML = `
                <span>${isPositive ? '📈' : '📉'}</span>
                <span>${isPositive ? '+' : ''}${change.toFixed(2)}%</span>
            `;
        }

        function updatePriceHistory(time, data) {
            const maxPoints = 20;
            
            // Ajouter les nouveaux points
            priceHistory.bitcoin.push(data.bitcoin.usd);
            priceHistory.ethereum.push(data.ethereum.usd);
            priceHistory.solana.push(data.solana.usd);
            
            // Limiter le nombre de points
            if (priceHistory.bitcoin.length > maxPoints) {
                priceHistory.bitcoin.shift();
                priceHistory.ethereum.shift();
                priceHistory.solana.shift();
            }
            
            // Mettre à jour le graphique
            if (priceChart.data.labels.length >= maxPoints) {
                priceChart.data.labels.shift();
            }
            priceChart.data.labels.push(time);
            
            priceChart.data.datasets[0].data = [...priceHistory.bitcoin];
            priceChart.data.datasets[1].data = [...priceHistory.ethereum];
            priceChart.data.datasets[2].data = [...priceHistory.solana];
            
            priceChart.update('none');
        }

        // Simulation de transactions
        function fetchTransactions() {
            showStatus('💸 Récupération des transactions...');
            
            const transactions = generateMockTransactions(5);
            const transactionsList = document.getElementById('transactions-list');
            
            transactionsList.innerHTML = transactions.map(tx => `
                <div class="transaction-item">
                    <div class="tx-hash">${tx.hash}</div>
                    <div class="tx-amount">$${tx.amount.toLocaleString('fr-FR')}</div>
                    <div class="tx-time">${tx.time} • ${tx.chain}</div>
                </div>
            `).join('');
            
            showStatus('✅ Transactions chargées');
        }

        function generateMockTransactions(count) {
            const chains = ['Bitcoin', 'Ethereum', 'Solana', 'BNB'];
            const transactions = [];
            
            for (let i = 0; i < count; i++) {
                transactions.push({
                    hash: '0x' + Math.random().toString(16).substr(2, 8) + '...' + Math.random().toString(16).substr(2, 4),
                    amount: Math.random() * 1000000 + 100000,
                    time: new Date(Date.now() - Math.random() * 3600000).toLocaleTimeString('fr-FR'),
                    chain: chains[Math.floor(Math.random() * chains.length)]
                });
            }
            
            return transactions.sort((a, b) => b.amount - a.amount);
        }

        // Simulation NFTs
        function fetchNFTs() {
            showStatus('🎨 Récupération des NFTs...');
            
            setTimeout(() => {
                const mockNFTs = [
                    'CryptoPunks #1234',
                    'Bored Ape #5678',
                    'Azuki #9012',
                    'Pudgy Penguins #3456',
                    'Doodles #7890'
                ];
                
                const nftList = mockNFTs.map(nft => `
                    <div class="transaction-item">
                        <div style="color: #ff6b6b; font-weight: 600;">${nft}</div>
                        <div class="tx-amount">$${(Math.random() * 100000 + 10000).toLocaleString('fr-FR')}</div>
                        <div class="tx-time">Vendu il y a ${Math.floor(Math.random() * 120)} minutes</div>
                    </div>
                `).join('');
                
                document.getElementById('transactions-list').innerHTML = `
                    <div style="margin-bottom: 1rem; color: #ff6b6b; font-weight: 600;">🎨 Top NFT Sales</div>
                    ${nftList}
                `;
                
                showStatus('✅ NFTs chargés');
            }, 1000);
        }

        // Auto-refresh
        function toggleAutoRefresh() {
            autoRefresh = !autoRefresh;
            
            if (autoRefresh) {
                refreshInterval = setInterval(() => {
                    updatePrices();
                }, 30000); // Toutes les 30 secondes
                showStatus('⚡ Auto-refresh activé (30s)');
            } else {
                clearInterval(refreshInterval);
                showStatus('⏸️ Auto-refresh désactivé');
            }
        }

        // Affichage du status
        function showStatus(message) {
            const statusIndicator = document.getElementById('status-indicator');
            statusIndicator.textContent = message;
            statusIndicator.classList.add('show');
            
            setTimeout(() => {
                statusIndicator.classList.remove('show');
            }, 3000);
        }

        // Nettoyage au déchargement de la page
        window.addEventListener('beforeunload', function() {
            if (refreshInterval) {
                clearInterval(refreshInterval);
            }
        });
    </script>
</body>
</html> + defiTvl + 'B';
        }

        // Détection de calls crypto
        function detectCalls() {
            showStatus('🚨 Analyse des signaux crypto...');
            
            const callsList = document.getElementById('calls-list');
            const callsHTML = CRYPTO_SIGNALS_DB.calls.map(call => `
                <div class="call-item">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="font-weight: 600; font-size: 1.1rem;">${call.coin}</span>
                        <span class="call-signal call-${call.signal.toLowerCase()}">
                            ${call.signal === 'BULLISH' ? '🟢' : call.signal === 'BEARISH' ? '🔴' : '🟡'} ${call.signal}
                        </span>
                    </div>
                    <div style="color: rgba(255,255,255,0.8); margin-bottom: 0.5rem;">
                        🎯 Target: <strong style="color: #00d4ff;">${call.target}</strong>
                    </div>
                    <div style="color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                        📊 Source: ${call.source} | 🎯 Confiance: ${call.confidence}%
                    </div>
                    <div class="prediction-confidence">
                        <div class="confidence-bar">
                            <div class="confidence-fill" style="width: ${call.confidence}%;"></div>
                        </div>
                        <span style="font-size: 0.8rem; color: rgba(255,255,255,0.6);">${call.confidence}%</span>
                    </div>
                </div>
            `).join('');
            
            callsList.innerHTML = callsHTML;
            showStatus('✅ Signaux détectés');
        }

        // Tracking des baleines
        function trackWhales() {
            showStatus('🐋 Tracking des mouvements baleines...');
            
            const whaleList = document.getElementById('whale-list');
            const whalesHTML = CRYPTO_SIGNALS_DB.whales.map(whale => `
                <div class="whale-item">
                    <div class="whale-amount">${whale.amount} ${whale.coin}</div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="color: ${whale.action === 'ACCUMULATION' ? '#22c55e' : '#ef4444'}; font-weight: 600;">
                            ${whale.action === 'ACCUMULATION' ? '📈 ACCUMULATION' : '📉 DISTRIBUTION'}
                        </span>
                        <span class="risk-indicator risk-${whale.confidence.toLowerCase()}">
                            ${whale.confidence === 'HIGH' ? '🔥' : '⚠️'} ${whale.confidence} RISK
                        </span>
                    </div>
                    <div style="color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                        🏢 Exchange: ${whale.exchange} | ⏰ ${Math.floor(Math.random() * 60)} min ago
                    </div>
                </div>
            `).join('');
            
            whaleList.innerHTML = whalesHTML;
            showStatus('✅ Baleines trackées');
        }

        // Analyse DeFi
        function analyzeDeFi() {
            showStatus('🌊 Analyse de l\'écosystème DeFi...');
            
            const defiList = document.getElementById('defi-list');
            const defiHTML = CRYPTO_SIGNALS_DB.defi.map(protocol => `
                <div class="trend-item">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="font-weight: 600; color: #00d4ff;">${protocol.protocol}</span>
                        <span class="trending-badge">💎 TOP</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 0.5rem;">
                        <div>
                            <div style="color: rgba(255,255,255,0.7); font-size: 0.8rem;">TVL</div>
                            <div style="font-weight: 600;">${protocol.tvl}</div>
                        </div>
                        <div>
                            <div style="color: rgba(255,255,255,0.7); font-size: 0.8rem;">APY</div>
                            <div style="font-weight: 600; color: #22c55e;">${protocol.apy}</div>
                        </div>
                    </div>
                    <div style="color: ${protocol.change.startsWith('+') ? '#22c55e' : '#ef4444'}; font-weight: 600;">
                        ${protocol.change.startsWith('+') ? '📈' : '📉'} ${protocol.change} (24h)
                    </div>
                </div>
            `).join('');
            
            defiList.innerHTML = defiHTML;
            showStatus('✅ DeFi analysé');
        }

        // Scanner meme coins
        function scanMemeCoins() {
            showStatus('🔥 Scan des meme coins trending...');
            
            const memeList = document.getElementById('meme-list');
            const memesHTML = CRYPTO_SIGNALS_DB.memes.map(meme => `
                <div class="trend-item">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="font-weight: 600; font-size: 1.1rem;">${meme.name}</span>
                        <span class="trending-badge">
                            ${meme.trend === 'VIRAL' ? '🚀 VIRAL' : 
                              meme.trend === 'EXPLOSIVE' ? '💥 EXPLOSIVE' : 
                              meme.trend === 'RISING' ? '📈 RISING' : '⚡ STABLE'}
                        </span>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                        <span style="color: #00d4ff; font-weight: 600;">${meme.price}</span>
                        <span style="color: ${meme.change.startsWith('+') ? '#22c55e' : '#ef4444'}; font-weight: 600;">
                            ${meme.change}
                        </span>
                    </div>
                    <div style="color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                        📊 Volume 24h: <strong>${meme.volume}</strong>
                    </div>
                </div>
            `).join('');
            
            memeList.innerHTML = memesHTML;
            showStatus('✅ Meme coins scannés');
        }

        // Trends NFT
        function fetchNFTTrends() {
            showStatus('🎨 Analyse des trends NFT...');
            
            const nftList = document.getElementById('nft-trends-list');
            const nftHTML = CRYPTO_SIGNALS_DB.nftTrends.map(nft => `
                <div class="trend-item">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="font-weight: 600; color: #ff6b6b;">${nft.collection}</span>
                        <span style="color: ${nft.change.startsWith('+') ? '#22c55e' : '#ef4444'}; font-weight: 600;">
                            ${nft.change}
                        </span>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                        <div>
                            <div style="color: rgba(255,255,255,0.7); font-size: 0.8rem;">Floor Price</div>
                            <div style="font-weight: 600; color: #00d4ff;">${nft.floor}</div>
                        </div>
                        <div>
                            <div style="color: rgba(255,255,255,0.7); font-size: 0.8rem;">Volume 24h</div>
                            <div style="font-weight: 600;">${nft.volume}</div>
                        </div>
                    </div>
                </div>
            `).join('');
            
            nftList.innerHTML = nftHTML;
            showStatus('✅ NFT trends analysés');
        }

        // Métriques on-chain
        function updateOnChainMetrics() {
            const onchainList = document.getElementById('onchain-list');
            const onchainHTML = `
                <div class="trend-item">
                    <div style="font-weight: 600; color: #00d4ff; margin-bottom: 0.5rem;">📊 Bitcoin Network</div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-size: 0.9rem;">
                        <div>Hash Rate: <strong>450 EH/s</strong></div>
                        <div>Difficulty: <strong>62.46T</strong></div>
                        <div>Mempool: <strong>12,543</strong></div>
                        <div>Fee Rate: <strong>15 sat/vB</strong></div>
                    </div>
                </div>
                <div class="trend-item">
                    <div style="font-weight: 600; color: #627eea; margin-bottom: 0.5rem;">⚡ Ethereum Network</div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-size: 0.9rem;">
                        <div>Gas Price: <strong>25 gwei</strong></div>
                        <div>TPS: <strong>13.2</strong></div>
                        <div>ETH Burned: <strong>1,234 ETH</strong></div>
                        <div>Staked ETH: <strong>28.5M</strong></div>
                    </div>
                </div>
            `;
            
            onchainList.innerHTML = onchainHTML;
        }

        // Prédictions IA
        function generateAIPredictions() {
            const predictionsList = document.getElementById('predictions-list');
            const predictions = [
                { coin: 'BTC', prediction: '$52,000', timeframe: '7 days', confidence: 78, trend: 'BULLISH' },
                { coin: 'ETH', prediction: '$3,100', timeframe: '5 days', confidence: 85, trend: 'BULLISH' },
                { coin: 'SOL', prediction: '$105', timeframe: '3 days', confidence: 72, trend: 'NEUTRAL' },
                { coin: 'ADA', prediction: '$0.42', timeframe: '10 days', confidence: 65, trend: 'BEARISH' }
            ];
            
            const predictionsHTML = predictions.map(pred => `
                <div class="trend-item">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="font-weight: 600; font-size: 1.1rem;">${pred.coin}</span>
                        <span class="call-signal call-${pred.trend.toLowerCase()}">
                            🤖 ${pred.trend}
                        </span>
                    </div>
                    <div style="color: #00d4ff; font-weight: 600; margin-bottom: 0.5rem;">
                        🎯 Target: ${pred.prediction} (${pred.timeframe})
                    </div>
                    <div class="prediction-confidence">
                        <span style="font-size: 0.8rem; color: rgba(255,255,255,0.7);">AI Confidence</span>
                        <div class="confidence-bar">
                            <div class="confidence-fill" style="width: ${pred.confidence}%;"></div>
                        </div>
                        <span style="font-size: 0.8rem; color: rgba(255,255,255,0.6);">${pred.confidence}%</span>
                    </div>
                </div>
            `).join('');
            
            predictionsList.innerHTML = predictionsHTML;
        }<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Crypto Sophistiqué</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/date-fns/2.29.3/index.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
            min-height: 100vh;
            overflow-x: hidden;
        }

        .navbar {
            background: rgba(15, 15, 35, 0.9);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .navbar h1 {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(45deg, #00d4ff, #7c3aed, #f59e0b);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { filter: brightness(1); }
            to { filter: brightness(1.2) drop-shadow(0 0 10px rgba(0, 212, 255, 0.3)); }
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .stat-card {
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02));
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            border-color: rgba(0, 212, 255, 0.5);
            box-shadow: 0 20px 40px rgba(0, 212, 255, 0.1);
        }

        .stat-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #00d4ff, #7c3aed, #f59e0b);
        }

        .stat-header {
            display: flex;
            justify-content: between;
            align-items: center;
            margin-bottom: 1rem;
        }

        .stat-icon {
            width: 50px;
            height: 50px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .bitcoin-icon { background: linear-gradient(145deg, #f7931a, #ff6b35); }
        .ethereum-icon { background: linear-gradient(145deg, #627eea, #3c4ccd); }
        .solana-icon { background: linear-gradient(145deg, #00d18c, #7c3aed); }
        .nft-icon { background: linear-gradient(145deg, #ff6b6b, #ee5a24); }

        .stat-value {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .change-indicator {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-top: 1rem;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: 600;
        }

        .positive { background: rgba(34, 197, 94, 0.2); color: #22c55e; }
        .negative { background: rgba(239, 68, 68, 0.2); color: #ef4444; }

        .charts-section {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .chart-container {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
        }

        .chart-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 2rem;
            text-align: center;
        }

        .transactions-table {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
        }

        .table-title {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .transactions-list {
            max-height: 400px;
            overflow-y: auto;
        }

        .transaction-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
        }

        .transaction-item:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(0, 212, 255, 0.3);
        }

        .tx-hash {
            font-family: 'Monaco', monospace;
            color: #00d4ff;
            font-size: 0.8rem;
            margin-bottom: 0.5rem;
        }

        .tx-amount {
            font-size: 1.2rem;
            font-weight: 600;
            color: #22c55e;
        }

        .tx-time {
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.6);
        }

        .controls {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        /* Nouvelles sections */
        .fundamental-section, .signals-section, .nft-analytics {
            margin-bottom: 3rem;
        }

        .section-title {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 2rem;
            text-align: center;
            background: linear-gradient(45deg, #00d4ff, #7c3aed, #f59e0b);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .fundamental-grid, .signals-grid, .analytics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .news-panel, .metrics-panel, .calls-detector, .whale-tracker, 
        .defi-tracker, .meme-tracker, .nft-trends, .social-sentiment,
        .onchain-metrics, .ai-predictions {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
        }

        .panel-title {
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: #00d4ff;
            border-bottom: 2px solid rgba(0, 212, 255, 0.2);
            padding-bottom: 0.5rem;
        }

        .news-list, .calls-list, .whale-list, .defi-list, .meme-list,
        .nft-trends-list, .onchain-list, .predictions-list {
            max-height: 400px;
            overflow-y: auto;
        }

        .news-item, .call-item, .whale-item, .trend-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            transition: all 0.3s ease;
        }

        .news-item:hover, .call-item:hover, .whale-item:hover, .trend-item:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(0, 212, 255, 0.3);
            transform: translateX(5px);
        }

        .news-title {
            font-weight: 600;
            color: #ffffff;
            margin-bottom: 0.5rem;
            line-height: 1.3;
        }

        .news-summary {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            line-height: 1.4;
            margin-bottom: 0.5rem;
        }

        .news-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.5);
        }

        .news-source {
            background: linear-gradient(45deg, #f59e0b, #ef4444);
            padding: 0.2rem 0.5rem;
            border-radius: 12px;
            font-weight: 600;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 1rem;
        }

        .metric-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .metric-card:hover {
            background: rgba(255, 255, 255, 0.08);
            transform: translateY(-2px);
        }

        .metric-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: #00d4ff;
            margin-bottom: 0.5rem;
        }

        .metric-label {
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.7);
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .call-signal {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .call-bullish {
            background: rgba(34, 197, 94, 0.2);
            color: #22c55e;
            border: 1px solid rgba(34, 197, 94, 0.3);
        }

        .call-bearish {
            background: rgba(239, 68, 68, 0.2);
            color: #ef4444;
            border: 1px solid rgba(239, 68, 68, 0.3);
        }

        .call-neutral {
            background: rgba(245, 158, 11, 0.2);
            color: #f59e0b;
            border: 1px solid rgba(245, 158, 11, 0.3);
        }

        .whale-amount {
            font-size: 1.2rem;
            font-weight: 700;
            color: #7c3aed;
            margin-bottom: 0.5rem;
        }

        .trending-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            padding: 0.2rem 0.6rem;
            border-radius: 15px;
            font-size: 0.7rem;
            font-weight: 600;
        }

        .sentiment-chart-container {
            height: 300px;
            padding: 1rem;
        }

        .prediction-confidence {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-top: 0.5rem;
        }

        .confidence-bar {
            flex: 1;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            overflow: hidden;
        }

        .confidence-fill {
            height: 100%;
            background: linear-gradient(90deg, #ef4444, #f59e0b, #22c55e);
            border-radius: 3px;
            transition: width 0.3s ease;
        }

        .alert-badge {
            position: absolute;
            top: 1rem;
            right: 1rem;
            background: linear-gradient(45deg, #ef4444, #dc2626);
            color: white;
            padding: 0.3rem 0.6rem;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: 600;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.8; transform: scale(1.05); }
        }

        .risk-indicator {
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .risk-low { color: #22c55e; }
        .risk-medium { color: #f59e0b; }
        .risk-high { color: #ef4444; }

        .btn {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.2), rgba(124, 58, 237, 0.2));
            border: 1px solid rgba(0, 212, 255, 0.3);
            color: #ffffff;
            padding: 0.8rem 1.5rem;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .btn:hover {
            background: linear-gradient(145deg, rgba(0, 212, 255, 0.4), rgba(124, 58, 237, 0.4));
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0, 212, 255, 0.2);
        }

        .loading {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }

        .spinner {
            width: 40px;
            height: 40px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-top: 3px solid #00d4ff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .status-indicator {
            position: fixed;
            top: 100px;
            right: 20px;
            background: rgba(34, 197, 94, 0.9);
            color: white;
            padding: 1rem;
            border-radius: 12px;
            border-left: 4px solid #22c55e;
            transform: translateX(100%);
            transition: transform 0.3s ease;
        }

        .status-indicator.show {
            transform: translateX(0);
        }

        @media (max-width: 768px) {
            .charts-section {
                grid-template-columns: 1fr;
            }
            
            .container {
                padding: 1rem;
            }
            
            .stats-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <h1>🚀 Dashboard Crypto Sophistiqué</h1>
    </nav>

    <div class="container">
        <div class="controls">
            <button class="btn" onclick="updatePrices()">🔄 Actualiser Prix</button>
            <button class="btn" onclick="fetchNews()">📰 News Crypto</button>
            <button class="btn" onclick="detectCalls()">🚨 Détecter Calls</button>
            <button class="btn" onclick="trackWhales()">🐋 Whale Tracker</button>
            <button class="btn" onclick="analyzeDeFi()">🌊 DeFi Analysis</button>
            <button class="btn" onclick="scanMemeCoins()">🔥 Meme Scanner</button>
            <button class="btn" onclick="fetchNFTTrends()">🎨 NFT Trends</button>
            <button class="btn" onclick="toggleAutoRefresh()">⚡ Auto-Refresh</button>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-icon bitcoin-icon">₿</div>
                <div class="stat-value" id="btc-price">$0</div>
                <div class="stat-label">Bitcoin (BTC)</div>
                <div class="change-indicator" id="btc-change">
                    <span>📈</span>
                    <span>+0.00%</span>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon ethereum-icon">Ξ</div>
                <div class="stat-value" id="eth-price">$0</div>
                <div class="stat-label">Ethereum (ETH)</div>
                <div class="change-indicator" id="eth-change">
                    <span>📈</span>
                    <span>+0.00%</span>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon solana-icon">◎</div>
                <div class="stat-value" id="sol-price">$0</div>
                <div class="stat-label">Solana (SOL)</div>
                <div class="change-indicator" id="sol-change">
                    <span>📈</span>
                    <span>+0.00%</span>
                </div>
            </div>

            <div class="stat-card">
                <div class="stat-icon nft-icon">🎨</div>
                <div class="stat-value" id="nft-volume">$0</div>
                <div class="stat-label">NFT Volume 24h</div>
                <div class="change-indicator positive">
                    <span>🔥</span>
                    <span>Volume élevé</span>
                </div>
            </div>
        </div>

        <div class="charts-section">
            <div class="chart-container">
                <div class="chart-title">📊 Évolution des Prix (24h)</div>
                <canvas id="priceChart" width="400" height="200"></canvas>
            </div>

            <div class="chart-container">
                <div class="chart-title">🥧 Répartition Portfolio</div>
                <canvas id="portfolioChart" width="300" height="300"></canvas>
            </div>
        </div>

        <!-- Section Analyse Fondamentale -->
        <div class="fundamental-section">
            <div class="section-title">📊 Analyse Fondamentale Crypto</div>
            
            <div class="fundamental-grid">
                <div class="news-panel">
                    <div class="panel-title">📰 News CoinDesk & Crypto.com</div>
                    <div class="news-list" id="news-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="metrics-panel">
                    <div class="panel-title">📈 Métriques Clés</div>
                    <div class="metrics-grid" id="metrics-grid">
                        <div class="metric-card">
                            <div class="metric-value" id="fear-greed">50</div>
                            <div class="metric-label">Fear & Greed Index</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value" id="btc-dominance">45%</div>
                            <div class="metric-label">BTC Dominance</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value" id="total-mcap">$2.1T</div>
                            <div class="metric-label">Total Market Cap</div>
                        </div>
                        <div class="metric-card">
                            <div class="metric-value" id="defi-tvl">$45B</div>
                            <div class="metric-label">DeFi TVL</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section Détection Calls/Signaux -->
        <div class="signals-section">
            <div class="section-title">🚨 Détection de Signaux & Calls</div>
            
            <div class="signals-grid">
                <div class="calls-detector">
                    <div class="panel-title">📢 Crypto Calls Détectés</div>
                    <div class="calls-list" id="calls-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="whale-tracker">
                    <div class="panel-title">🐋 Whale Tracker</div>
                    <div class="whale-list" id="whale-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="defi-tracker">
                    <div class="panel-title">🌊 DeFi Pulse</div>
                    <div class="defi-list" id="defi-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="meme-tracker">
                    <div class="panel-title">🔥 Meme Coins Trending</div>
                    <div class="meme-list" id="meme-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Section NFT & Analytics -->
        <div class="nft-analytics">
            <div class="section-title">🎨 NFT & Analyse Avancée</div>
            
            <div class="analytics-grid">
                <div class="nft-trends">
                    <div class="panel-title">🖼️ NFT Trends</div>
                    <div class="nft-trends-list" id="nft-trends-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="social-sentiment">
                    <div class="panel-title">💬 Social Sentiment</div>
                    <div class="sentiment-chart-container">
                        <canvas id="sentimentChart" width="400" height="200"></canvas>
                    </div>
                </div>
                
                <div class="onchain-metrics">
                    <div class="panel-title">⛓️ On-Chain Metrics</div>
                    <div class="onchain-list" id="onchain-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
                
                <div class="ai-predictions">
                    <div class="panel-title">🤖 AI Predictions</div>
                    <div class="predictions-list" id="predictions-list">
                        <div class="loading"><div class="spinner"></div></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="transactions-table">
            <div class="table-title">
                <span>💎</span>
                <span>Grandes Transactions Récentes</span>
            </div>
            <div class="transactions-list" id="transactions-list">
                <div class="loading">
                    <div class="spinner"></div>
                </div>
            </div>
        </div>
    </div>

    <div class="status-indicator" id="status-indicator">
        ✅ Données mises à jour
    </div>

    <script>
        // Configuration
        const API_CONFIG = {
            coingecko: 'https://api.coingecko.com/api/v3',
            newsapi: 'https://newsapi.org/v2',
            alternative: 'https://api.alternative.me/v1',
            defipulse: 'https://api.defipulse.com/api/v1',
            fallbackPrices: {
                bitcoin: 45000,
                ethereum: 2800,
                solana: 95
            }
        };

        // État global
        let autoRefresh = false;
        let refreshInterval;
        let priceChart, portfolioChart, sentimentChart;
        let priceHistory = {
            bitcoin: [],
            ethereum: [],
            solana: []
        };

        // Base de données de signaux simulés
        const CRYPTO_SIGNALS_DB = {
            calls: [
                { coin: 'BTC', signal: 'BULLISH', confidence: 85, source: 'Technical Analysis', target: '$48000' },
                { coin: 'ETH', signal: 'BULLISH', confidence: 78, source: 'Whale Activity', target: '$3200' },
                { coin: 'SOL', signal: 'NEUTRAL', confidence: 65, source: 'Social Sentiment', target: '$110' },
                { coin: 'ADA', signal: 'BEARISH', confidence: 72, source: 'Volume Analysis', target: '$0.35' },
                { coin: 'MATIC', signal: 'BULLISH', confidence: 90, source: 'Fundamental', target: '$1.20' }
            ],
            whales: [
                { amount: '$12.5M', coin: 'BTC', action: 'ACCUMULATION', exchange: 'Coinbase', confidence: 'HIGH' },
                { amount: '$8.2M', coin: 'ETH', action: 'DISTRIBUTION', exchange: 'Binance', confidence: 'MEDIUM' },
                { amount: '$5.7M', coin: 'SOL', action: 'ACCUMULATION', exchange: 'FTX', confidence: 'HIGH' },
                { amount: '$3.1M', coin: 'AVAX', action: 'ACCUMULATION', exchange: 'Kraken', confidence: 'MEDIUM' }
            ],
            defi: [
                { protocol: 'Uniswap', tvl: '$4.2B', change: '+5.2%', apy: '12.5%' },
                { protocol: 'Aave', tvl: '$7.8B', change: '+2.1%', apy: '8.9%' },
                { protocol: 'Compound', tvl: '$3.1B', change: '-1.5%', apy: '6.2%' },
                { protocol: 'MakerDAO', tvl: '$9.5B', change: '+3.8%', apy: '4.1%' }
            ],
            memes: [
                { name: 'PEPE', price: '$0.00001234', change: '+156.7%', volume: '$45M', trend: 'VIRAL' },
                { name: 'DOGE', price: '$0.0789', change: '+12.3%', volume: '$234M', trend: 'STABLE' },
                { name: 'SHIB', price: '$0.000008', change: '+45.6%', volume: '$123M', trend: 'RISING' },
                { name: 'FLOKI', price: '$0.000023', change: '+89.2%', volume: '$67M', trend: 'EXPLOSIVE' }
            ],
            news: [
                { title: 'Bitcoin ETF Approval Drives Institutional Adoption', summary: 'Major financial institutions increase crypto exposure following regulatory clarity...', source: 'CoinDesk', time: '2h ago' },
                { title: 'Ethereum Layer 2 Solutions See Record Usage', summary: 'Polygon and Arbitrum report unprecedented transaction volumes as gas fees drop...', source: 'Crypto.com', time: '4h ago' },
                { title: 'Solana DeFi Ecosystem Expands with New Protocols', summary: 'Several new DeFi projects launch on Solana, bringing innovative yield farming opportunities...', source: 'CoinTelegraph', time: '6h ago' },
                { title: 'NFT Market Shows Signs of Recovery', summary: 'Blue chip NFT collections see increased trading volume and floor price stability...', source: 'The Block', time: '8h ago' }
            ],
            nftTrends: [
                { collection: 'CryptoPunks', floor: '45.2 ETH', volume: '234 ETH', change: '+12.5%' },
                { collection: 'Bored Apes', floor: '32.1 ETH', volume: '456 ETH', change: '+8.7%' },
                { collection: 'Azuki', floor: '18.5 ETH', volume: '123 ETH', change: '+23.1%' },
                { collection: 'Pudgy Penguins', floor: '8.9 ETH', volume: '89 ETH', change: '+15.6%' }
            ]
        };

        // Initialisation
        document.addEventListener('DOMContentLoaded', function() {
            initCharts();
            updatePrices();
            fetchNews();
            updateFundamentalMetrics();
            detectCalls();
            trackWhales();
            analyzeDeFi();
            scanMemeCoins();
            fetchNFTTrends();
            updateOnChainMetrics();
            generateAIPredictions();
            showStatus('🚀 Dashboard crypto sophistiqué initialisé');
        });

        // Initialisation des graphiques
        function initCharts() {
            // Graphique des prix
            const ctx1 = document.getElementById('priceChart').getContext('2d');
            priceChart = new Chart(ctx1, {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [
                        {
                            label: 'Bitcoin',
                            data: [],
                            borderColor: '#f7931a',
                            backgroundColor: 'rgba(247, 147, 26, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'Ethereum',
                            data: [],
                            borderColor: '#627eea',
                            backgroundColor: 'rgba(98, 126, 234, 0.1)',
                            tension: 0.4
                        },
                        {
                            label: 'Solana',
                            data: [],
                            borderColor: '#00d18c',
                            backgroundColor: 'rgba(0, 209, 140, 0.1)',
                            tension: 0.4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: '#ffffff' }
                        }
                    },
                    scales: {
                        x: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        },
                        y: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        }
                    }
                }
            });

            // Graphique portfolio
            const ctx2 = document.getElementById('portfolioChart').getContext('2d');
            portfolioChart = new Chart(ctx2, {
                type: 'doughnut',
                data: {
                    labels: ['Bitcoin', 'Ethereum', 'Solana', 'Autres'],
                    datasets: [{
                        data: [40, 30, 20, 10],
                        backgroundColor: [
                            '#f7931a',
                            '#627eea',
                            '#00d18c',
                            '#7c3aed'
                        ],
                        borderWidth: 0
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: '#ffffff' }
                        }
                    }
                }
            });

            // Graphique sentiment
            const ctx3 = document.getElementById('sentimentChart').getContext('2d');
            sentimentChart = new Chart(ctx3, {
                type: 'bar',
                data: {
                    labels: ['Twitter', 'Reddit', 'Telegram', 'Discord', 'News'],
                    datasets: [{
                        label: 'Sentiment Score',
                        data: [75, 60, 85, 70, 80],
                        backgroundColor: [
                            'rgba(29, 161, 242, 0.8)',
                            'rgba(255, 69, 0, 0.8)',
                            'rgba(0, 136, 204, 0.8)',
                            'rgba(114, 137, 218, 0.8)',
                            'rgba(0, 212, 255, 0.8)'
                        ],
                        borderWidth: 2,
                        borderColor: '#ffffff'
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: '#ffffff' }
                        }
                    },
                    scales: {
                        x: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' }
                        },
                        y: { 
                            ticks: { color: '#ffffff' },
                            grid: { color: 'rgba(255, 255, 255, 0.1)' },
                            max: 100
                        }
                    }
                }
            });
        }

        // Mise à jour des prix
        async function updatePrices() {
            try {
                showStatus('🔄 Mise à jour des prix...');
                
                const response = await fetch(`${API_CONFIG.coingecko}/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true`);
                
                if (!response.ok) {
                    throw new Error('API non disponible');
                }
                
                const data = await response.json();
                
                // Mise à jour des prix
                updatePriceDisplay('btc', data.bitcoin);
                updatePriceDisplay('eth', data.ethereum);
                updatePriceDisplay('sol', data.solana);
                
                // Mise à jour de l'historique
                const now = new Date().toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
                updatePriceHistory(now, data);
                
                // Volume NFT simulé
                document.getElementById('nft-volume').textContent = '$' + (Math.random() * 10000000).toLocaleString('fr-FR', { maximumFractionDigits: 0 });
                
                showStatus('✅ Prix mis à jour');
                
            } catch (error) {
                console.error('Erreur prix:', error);
                // Utiliser les prix de fallback
                updatePriceDisplay('btc', { usd: API_CONFIG.fallbackPrices.bitcoin, usd_24h_change: Math.random() * 10 - 5 });
                updatePriceDisplay('eth', { usd: API_CONFIG.fallbackPrices.ethereum, usd_24h_change: Math.random() * 10 - 5 });
                updatePriceDisplay('sol', { usd: API_CONFIG.fallbackPrices.solana, usd_24h_change: Math.random() * 10 - 5 });
                
                showStatus('⚠️ Mode hors ligne');
            }
        }

        function updatePriceDisplay(coin, data) {
            const price = data.usd || 0;
            const change = data.usd_24h_change || 0;
            
            document.getElementById(`${coin}-price`).textContent = '$' + price.toLocaleString('fr-FR');
            
            const changeElement = document.getElementById(`${coin}-change`);
            const isPositive = change >= 0;
            changeElement.className = `change-indicator ${isPositive ? 'positive' : 'negative'}`;
            changeElement.innerHTML = `
                <span>${isPositive ? '📈' : '📉'}</span>
                <span>${isPositive ? '+' : ''}${change.toFixed(2)}%</span>
            `;
        }

        function updatePriceHistory(time, data) {
            const maxPoints = 20;
            
            // Ajouter les nouveaux points
            priceHistory.bitcoin.push(data.bitcoin.usd);
            priceHistory.ethereum.push(data.ethereum.usd);
            priceHistory.solana.push(data.solana.usd);
            
            // Limiter le nombre de points
            if (priceHistory.bitcoin.length > maxPoints) {
                priceHistory.bitcoin.shift();
                priceHistory.ethereum.shift();
                priceHistory.solana.shift();
            }
            
            // Mettre à jour le graphique
            if (priceChart.data.labels.length >= maxPoints) {
                priceChart.data.labels.shift();
            }
            priceChart.data.labels.push(time);
            
            priceChart.data.datasets[0].data = [...priceHistory.bitcoin];
            priceChart.data.datasets[1].data = [...priceHistory.ethereum];
            priceChart.data.datasets[2].data = [...priceHistory.solana];
            
            priceChart.update('none');
        }

        // Simulation de transactions
        function fetchTransactions() {
            showStatus('💸 Récupération des transactions...');
            
            const transactions = generateMockTransactions(5);
            const transactionsList = document.getElementById('transactions-list');
            
            transactionsList.innerHTML = transactions.map(tx => `
                <div class="transaction-item">
                    <div class="tx-hash">${tx.hash}</div>
                    <div class="tx-amount">$${tx.amount.toLocaleString('fr-FR')}</div>
                    <div class="tx-time">${tx.time} • ${tx.chain}</div>
                </div>
            `).join('');
            
            showStatus('✅ Transactions chargées');
        }

        function generateMockTransactions(count) {
            const chains = ['Bitcoin', 'Ethereum', 'Solana', 'BNB'];
            const transactions = [];
            
            for (let i = 0; i < count; i++) {
                transactions.push({
                    hash: '0x' + Math.random().toString(16).substr(2, 8) + '...' + Math.random().toString(16).substr(2, 4),
                    amount: Math.random() * 1000000 + 100000,
                    time: new Date(Date.now() - Math.random() * 3600000).toLocaleTimeString('fr-FR'),
                    chain: chains[Math.floor(Math.random() * chains.length)]
                });
            }
            
            return transactions.sort((a, b) => b.amount - a.amount);
        }

        // Simulation NFTs
        function fetchNFTs() {
            showStatus('🎨 Récupération des NFTs...');
            
            setTimeout(() => {
                const mockNFTs = [
                    'CryptoPunks #1234',
                    'Bored Ape #5678',
                    'Azuki #9012',
                    'Pudgy Penguins #3456',
                    'Doodles #7890'
                ];
                
                const nftList = mockNFTs.map(nft => `
                    <div class="transaction-item">
                        <div style="color: #ff6b6b; font-weight: 600;">${nft}</div>
                        <div class="tx-amount">$${(Math.random() * 100000 + 10000).toLocaleString('fr-FR')}</div>
                        <div class="tx-time">Vendu il y a ${Math.floor(Math.random() * 120)} minutes</div>
                    </div>
                `).join('');
                
                document.getElementById('transactions-list').innerHTML = `
                    <div style="margin-bottom: 1rem; color: #ff6b6b; font-weight: 600;">🎨 Top NFT Sales</div>
                    ${nftList}
                `;
                
                showStatus('✅ NFTs chargés');
            }, 1000);
        }

        // Auto-refresh
        function toggleAutoRefresh() {
            autoRefresh = !autoRefresh;
            
            if (autoRefresh) {
                refreshInterval = setInterval(() => {
                    updatePrices();
                }, 30000); // Toutes les 30 secondes
                showStatus('⚡ Auto-refresh activé (30s)');
            } else {
                clearInterval(refreshInterval);
                showStatus('⏸️ Auto-refresh désactivé');
            }
        }

        // Affichage du status
        function showStatus(message) {
            const statusIndicator = document.getElementById('status-indicator');
            statusIndicator.textContent = message;
            statusIndicator.classList.add('show');
            
            setTimeout(() => {
                statusIndicator.classList.remove('show');
            }, 3000);
        }

        // Nettoyage au déchargement de la page
        window.addEventListener('beforeunload', function() {
            if (refreshInterval) {
                clearInterval(refreshInterval);
            }
        });
    </script>
</body>
</html>
