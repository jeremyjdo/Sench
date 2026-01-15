"""Sench - Competitive intelligence sub-agent for Claude Code, Codex & Cursor."""

__version__ = "1.0.0"
__author__ = "Sench Team"

from sench.core.scraper import Scraper, ScrapeResult, scrape_sync
from sench.modules import (
    DEFAULT_MODULE_ORDER,
    MODULE_FLAGS,
    MODULE_INFO,
    ModuleKey,
    get_prompt,
    get_system_prompt,
)

__all__ = [
    "__version__",
    "Scraper",
    "ScrapeResult",
    "scrape_sync",
    "ModuleKey",
    "MODULE_FLAGS",
    "MODULE_INFO",
    "DEFAULT_MODULE_ORDER",
    "get_prompt",
    "get_system_prompt",
]
