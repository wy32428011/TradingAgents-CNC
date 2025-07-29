import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": os.path.join(os.path.expanduser("~"), "Documents", "TradingAgents", "data"),
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings
    # "llm_provider": "ollama",
    # "deep_think_llm": "o4-mini",
    # "quick_think_llm": "gpt-4o-mini",
    "llm_provider": "Qwen3-235B-A22B",
    "deep_think_llm": "Qwen3-235B-A22B",
    "quick_think_llm": "Qwen3-235B-A22B",
    "backend_url": "http://x48876e7.natappfree.cc/v1",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Tool settings
    "online_tools": True,
    "llm_base_url": "http://x48876e7.natappfree.cc/v1",
    "embed_base_url": "http://embedding.flashsoft.top/v1",
    "llm_model_name": "Qwen3-235B-A22B",
    "embed_model_name": "bge-m3",
    "llm_api_key": "test_qwen",
    "embed_api_key": "test_bge",

    # Note: Database and cache configuration is now managed by .env file and config.database_manager
    # No database/cache settings in default config to avoid configuration conflicts
}
