#!/usr/bin/env bash
# Sench - Competitive Intelligence Sub-Agent
# Install: curl -fsSL https://sench.ai/install | bash

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
DIM='\033[2m'
NC='\033[0m'

SENCH_VERSION="1.0.0"

echo -e "${DIM}/sench${NC} v${SENCH_VERSION}"
echo ""

# Detect environment
detect_environment() {
    if [ -n "${CLAUDE_CODE:-}" ] || [ -d "$HOME/.claude" ]; then
        echo "claude-code"
    elif [ -n "${CODEX_ENV:-}" ] || [ -d "$HOME/.codex" ]; then
        echo "codex"
    elif [ -n "${CURSOR_ENV:-}" ] || [ -d "$HOME/.cursor" ]; then
        echo "cursor"
    else
        echo "standalone"
    fi
}

ENV=$(detect_environment)
echo -e "Environment: ${BLUE}${ENV}${NC}"

# Check Python
check_python() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}Error:${NC} Python 3.11+ required"
        exit 1
    fi

    PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')
    if [ "$PYTHON_MINOR" -lt 11 ]; then
        echo -e "${RED}Error:${NC} Python 3.11+ required (found 3.${PYTHON_MINOR})"
        exit 1
    fi
    echo -e "${GREEN}✓${NC} Python 3.${PYTHON_MINOR}"
}

# Install Playwright
install_playwright() {
    echo -e "${DIM}Installing Playwright...${NC}"

    pip install playwright -q 2>/dev/null || pip install playwright --user -q

    # Install chromium browser
    python3 -m playwright install chromium 2>/dev/null || true

    echo -e "${GREEN}✓${NC} Playwright installed"
}

# Install sench package
install_sench() {
    echo -e "${DIM}Installing sench...${NC}"

    # Install from PyPI when published, for now just playwright
    pip install playwright -q 2>/dev/null || pip install playwright --user -q

    echo -e "${GREEN}✓${NC} sench installed"
}

# Create command wrapper
create_wrapper() {
    local INSTALL_DIR="${HOME}/.local/bin"
    mkdir -p "$INSTALL_DIR"

    cat > "$INSTALL_DIR/sench" << 'EOF'
#!/usr/bin/env bash
python3 -m sench "$@"
EOF

    chmod +x "$INSTALL_DIR/sench"

    # Add to PATH if needed
    if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
        SHELL_RC=""
        case "$(basename "$SHELL")" in
            zsh) SHELL_RC="$HOME/.zshrc" ;;
            bash) SHELL_RC="$HOME/.bashrc" ;;
            *) SHELL_RC="$HOME/.profile" ;;
        esac

        if [ -n "$SHELL_RC" ] && ! grep -q '.local/bin' "$SHELL_RC" 2>/dev/null; then
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
        fi
    fi

    echo -e "${GREEN}✓${NC} Command: sench"
}

# Main
main() {
    check_python
    install_playwright
    create_wrapper

    echo ""
    echo -e "${GREEN}Installed!${NC}"
    echo ""
    echo "Usage in ${ENV}:"
    echo -e "  ${BLUE}/sench stripe.com${NC}"
    echo -e "  ${BLUE}/sench stripe.com --gtm${NC}"
    echo ""
}

main
