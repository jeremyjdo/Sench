"""Prompt templates for Sench CLI."""

from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent / "templates"


def load_template(name: str) -> str:
    """Load a prompt template by name."""
    template_path = TEMPLATES_DIR / f"{name}.md"
    if not template_path.exists():
        raise FileNotFoundError(f"Template {name} not found at {template_path}")
    return template_path.read_text()


__all__ = ["load_template", "TEMPLATES_DIR"]
